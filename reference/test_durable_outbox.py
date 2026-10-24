"""Synthetic fixtures for the independently authored educational outbox."""

from pathlib import Path
import sqlite3
from tempfile import TemporaryDirectory
import threading
import unittest

from durable_outbox import Event, Outbox, TerminalStream, TransitionDenied


class OutboxTests(unittest.TestCase):
    def setUp(self):
        self.directory = TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.path = Path(self.directory.name) / "fixture.sqlite"
        self.box = Outbox(self.path)
        self.addCleanup(self.box.close)
        self.event = Event("event-a", "stream-a", "Synthetic notice")

    def test_admission_survives_reopen_with_its_outbox(self):
        self.assertTrue(self.box.admit(self.event))
        with Outbox(self.path) as reopened:
            row = reopened.get("event-a")
            self.assertEqual(row["body"], "Synthetic notice")
            self.assertEqual(row["delivery_phase"], "ready")

    def test_failed_outbox_insert_rolls_back_entire_admission(self):
        self.box.db.execute("""CREATE TRIGGER fail_admission BEFORE INSERT ON dispatch
            BEGIN SELECT RAISE(ABORT, 'injected admission failure'); END""")
        with self.assertRaises(sqlite3.IntegrityError):
            self.box.admit(self.event)
        with Outbox(self.path) as reopened:
            for table in ("streams", "messages", "dispatch"):
                self.assertEqual(reopened.db.execute(
                    f"SELECT COUNT(*) FROM {table}"
                ).fetchone()[0], 0)

    def test_identical_duplicate_does_not_create_work(self):
        self.box.admit(self.event)
        self.assertFalse(self.box.admit(self.event))
        self.assertEqual(self.box.db.execute(
            "SELECT COUNT(*) FROM dispatch"
        ).fetchone()[0], 1)

    def test_duplicate_identity_cannot_change_body_or_stream(self):
        self.box.admit(self.event)
        for changed in (Event("event-a", "stream-a", "Changed"),
                        Event("event-a", "stream-b", "Synthetic notice")):
            with self.subTest(changed=changed), self.assertRaises(ValueError):
                self.box.admit(changed)
        self.assertEqual(self.box.get("event-a")["body"], self.event.body)

    def test_two_connections_compete_for_one_claim(self):
        self.box.admit(self.event)
        barrier = threading.Barrier(2, timeout=2)
        results, failures = [], []

        def actor():
            try:
                with Outbox(self.path) as contender:
                    barrier.wait()
                    results.append(contender.claim("event-a"))
            except Exception as error:
                failures.append(error)

        workers = [threading.Thread(target=actor, daemon=True) for _ in range(2)]
        for worker in workers:
            worker.start()
        for worker in workers:
            worker.join(timeout=3)
        self.assertTrue(all(not worker.is_alive() for worker in workers))
        self.assertEqual(failures, [])
        self.assertEqual(sum(claim is not None for claim in results), 1)

    def test_wrong_claim_cannot_invoke_sender(self):
        self.box.admit(self.event)
        self.box.claim("event-a")
        calls = []
        with self.assertRaises(TransitionDenied):
            self.box.deliver("event-a", "wrong-claim", calls.append)
        self.assertEqual(calls, [])
        self.assertEqual(self.box.get("event-a")["delivery_phase"], "owned")

    def test_provider_io_holds_no_write_transaction(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")

        def sender(body):
            self.assertEqual(body, self.event.body)
            self.assertFalse(self.box.db.in_transaction)
            with Outbox(self.path) as other:
                self.assertTrue(other.admit(Event("event-b", "stream-a", "Other")))
            return "synthetic-ack"

        self.box.deliver("event-a", claim, sender)
        self.assertEqual(self.box.get("event-b")["delivery_phase"], "ready")

    def test_provider_acknowledgement_is_durable_and_final(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")
        self.box.deliver("event-a", claim, lambda body: "synthetic-ack")
        with Outbox(self.path) as reopened:
            self.assertEqual(reopened.get("event-a")["provider_ack"], "synthetic-ack")
            self.assertEqual(reopened.get("event-a")["delivery_phase"], "acknowledged")
            self.assertIsNone(reopened.claim("event-a"))
        with self.assertRaises(TransitionDenied):
            self.box.deliver("event-a", claim, lambda body: self.fail("replayed"))

    def test_timeout_after_possible_acceptance_stays_uncertain_without_replay(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")
        calls = []

        def accepted_then_timed_out(body):
            calls.append(body)
            raise TimeoutError("Synthetic provider outcome is unknown")

        with self.assertRaises(TimeoutError):
            self.box.deliver("event-a", claim, accepted_then_timed_out)
        with Outbox(self.path) as reopened:
            self.assertEqual(reopened.get("event-a")["delivery_phase"], "uncertain")
            self.assertIsNone(reopened.claim("event-a"))
            with self.assertRaises(TransitionDenied):
                reopened.deliver("event-a", claim, accepted_then_timed_out)
        self.assertEqual(calls, [self.event.body])

    def test_failure_saving_acknowledgement_keeps_pre_send_fence(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")
        self.box.db.execute("""CREATE TRIGGER fail_receipt BEFORE UPDATE ON dispatch
            WHEN NEW.phase = 'acknowledged'
            BEGIN SELECT RAISE(ABORT, 'injected receipt failure'); END""")
        calls = []

        def sender(body):
            calls.append(body)
            return "synthetic-ack"

        with self.assertRaises(sqlite3.IntegrityError):
            self.box.deliver("event-a", claim, sender)
        with Outbox(self.path) as reopened:
            self.assertEqual(reopened.get("event-a")["delivery_phase"], "uncertain")
            self.assertIsNone(reopened.claim("event-a"))
        self.assertEqual(len(calls), 1)

    def test_abandoned_claim_is_not_automatically_reassigned(self):
        self.box.admit(self.event)
        self.box.claim("event-a")
        with Outbox(self.path) as reopened:
            self.assertIsNone(reopened.claim("event-a"))
            self.assertEqual(reopened.get("event-a")["delivery_phase"], "owned")

    def test_terminal_stream_cancels_unsent_work_and_rejects_late_events(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")
        self.box.admit(Event("event-b", "stream-a", "Queued"))
        self.box.finish("stream-a")
        self.box.finish("stream-a")
        for key in ("event-a", "event-b"):
            self.assertEqual(self.box.get(key)["delivery_phase"], "cancelled")
            self.assertIsNone(self.box.claim(key))
        with self.assertRaises(TransitionDenied):
            self.box.deliver("event-a", claim, lambda body: self.fail("late send"))
        with self.assertRaises(TerminalStream):
            self.box.admit(Event("late-event", "stream-a", "Late"))
        self.assertFalse(self.box.admit(self.event))
        with self.assertRaises(KeyError):
            self.box.get("late-event")

    def test_closing_unknown_stream_also_blocks_future_admission(self):
        self.box.finish("stream-a")
        with Outbox(self.path) as reopened, self.assertRaises(TerminalStream):
            reopened.admit(self.event)

    def test_terminal_during_io_preserves_fence_and_records_actual_ack(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")

        def sender(body):
            with Outbox(self.path) as other:
                other.finish("stream-a")
                self.assertEqual(other.get("event-a")["delivery_phase"], "uncertain")
            return "synthetic-ack"

        self.box.deliver("event-a", claim, sender)
        row = self.box.get("event-a")
        self.assertEqual(row["stream_phase"], "closed")
        self.assertEqual(row["delivery_phase"], "acknowledged")

    def test_invalid_or_partial_input_is_rejected_before_storage(self):
        for payload in ({}, {"event_key": "a"},
                        {"event_key": "a", "stream_key": "b", "body": "x", "extra": 1}):
            with self.subTest(payload=payload), self.assertRaises(TypeError):
                Event(**payload)
        for body in (None, True, 2, "", "   ", "x" * 1025):
            with self.subTest(body=body), self.assertRaises(ValueError):
                Event("a", "b", body)
        for event in (lambda: Event(" ", "b", "x"),
                      lambda: Event("a", None, "x")):
            with self.assertRaises(ValueError):
                event()
        self.assertEqual(self.box.db.execute("SELECT COUNT(*) FROM messages").fetchone()[0], 0)

    def test_invalid_acknowledgement_remains_uncertain(self):
        self.box.admit(self.event)
        claim = self.box.claim("event-a")
        with self.assertRaises(ValueError):
            self.box.deliver("event-a", claim, lambda body: None)
        self.assertEqual(self.box.get("event-a")["delivery_phase"], "uncertain")


if __name__ == "__main__":
    unittest.main()
