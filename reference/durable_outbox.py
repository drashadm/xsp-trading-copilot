"""Independent educational outbox; generic synthetic events, no network client.

This is not production code or a production schema. Only use a disposable DB.
"""

from dataclasses import dataclass
from pathlib import Path
import sqlite3
from typing import Callable
from uuid import uuid4


def _text(value: str) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > 1024:
        raise ValueError("Expected nonblank text of at most 1024 characters")


@dataclass(frozen=True)
class Event:
    """Exact constructor fields; missing/extra fields and invalid text fail closed."""

    event_key: str
    stream_key: str
    body: str

    def __post_init__(self):
        for value in (self.event_key, self.stream_key, self.body):
            _text(value)


class TerminalStream(ValueError):
    pass


class TransitionDenied(ValueError):
    pass


class Outbox:
    """One connection per actor; each mutation is a short serialized transaction."""

    def __init__(self, database: str | Path):
        self.db = sqlite3.connect(database, timeout=0.5)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS streams (
                stream_key TEXT PRIMARY KEY,
                phase TEXT NOT NULL CHECK (phase IN ('active', 'closed'))
            );
            CREATE TABLE IF NOT EXISTS messages (
                event_key TEXT PRIMARY KEY,
                stream_key TEXT NOT NULL REFERENCES streams(stream_key),
                body TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS dispatch (
                event_key TEXT PRIMARY KEY REFERENCES messages(event_key),
                phase TEXT NOT NULL CHECK (phase IN
                    ('ready', 'owned', 'uncertain', 'acknowledged', 'cancelled')),
                claim_key TEXT,
                provider_ack TEXT
            );
        """)

    def __enter__(self):
        return self

    def __exit__(self, *exception):
        self.close()

    def close(self):
        self.db.close()

    def admit(self, event: Event) -> bool:
        """Atomically persist message + intent; an exact duplicate is a no-op."""
        if not isinstance(event, Event):
            raise TypeError("Expected a validated Event")
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            prior = self.db.execute(
                "SELECT stream_key, body FROM messages WHERE event_key = ?",
                (event.event_key,),
            ).fetchone()
            if prior is not None:
                if tuple(prior) != (event.stream_key, event.body):
                    raise ValueError("Event identity conflicts with retained content")
                return False
            stream = self.db.execute(
                "SELECT phase FROM streams WHERE stream_key = ?", (event.stream_key,)
            ).fetchone()
            if stream is not None and stream["phase"] == "closed":
                raise TerminalStream("New events cannot reopen a closed stream")
            self.db.execute(
                "INSERT OR IGNORE INTO streams VALUES (?, 'active')", (event.stream_key,)
            )
            self.db.execute("INSERT INTO messages VALUES (?, ?, ?)",
                            (event.event_key, event.stream_key, event.body))
            self.db.execute("INSERT INTO dispatch VALUES (?, 'ready', NULL, NULL)",
                            (event.event_key,))
        return True

    def claim(self, event_key: str) -> str | None:
        """Only one ready/active intent can acquire a claim; no lease expiry."""
        _text(event_key)
        claim_key = uuid4().hex
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            changed = self.db.execute("""
                UPDATE dispatch SET phase = 'owned', claim_key = ?
                WHERE event_key = ? AND phase = 'ready' AND EXISTS (
                    SELECT 1 FROM messages m JOIN streams s USING (stream_key)
                    WHERE m.event_key = dispatch.event_key AND s.phase = 'active'
                )
            """, (claim_key, event_key)).rowcount
        return claim_key if changed == 1 else None

    def deliver(self, event_key: str, claim_key: str, sender: Callable[[str], str]) -> None:
        """Fence before I/O; any exception propagates and leaves uncertainty durable.

        Terminal closure after the fence cannot recall I/O already authorized.
        An acknowledgement can still be recorded without reopening the stream.
        """
        _text(event_key)
        _text(claim_key)
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            changed = self.db.execute("""
                UPDATE dispatch SET phase = 'uncertain'
                WHERE event_key = ? AND claim_key = ? AND phase = 'owned' AND EXISTS (
                    SELECT 1 FROM messages m JOIN streams s USING (stream_key)
                    WHERE m.event_key = dispatch.event_key AND s.phase = 'active'
                )
            """, (event_key, claim_key)).rowcount
            if changed != 1:
                raise TransitionDenied("No active owned intent authorizes this send")
            body = self.db.execute(
                "SELECT body FROM messages WHERE event_key = ?", (event_key,)
            ).fetchone()["body"]

        # The uncertainty fence is committed. No SQLite transaction spans this call.
        acknowledgement = sender(body)
        _text(acknowledgement)
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            changed = self.db.execute("""
                UPDATE dispatch SET phase = 'acknowledged', provider_ack = ?
                WHERE event_key = ? AND claim_key = ? AND phase = 'uncertain'
            """, (acknowledgement, event_key, claim_key)).rowcount
            if changed != 1:
                raise TransitionDenied("Acknowledgement no longer matches its fence")

    def finish(self, stream_key: str) -> None:
        """Close permanently, cancelling ready/owned work; preserve uncertain sends."""
        _text(stream_key)
        with self.db:
            self.db.execute("BEGIN IMMEDIATE")
            self.db.execute("""
                INSERT INTO streams VALUES (?, 'closed')
                ON CONFLICT (stream_key) DO UPDATE SET phase = 'closed'
            """, (stream_key,))
            self.db.execute("""
                UPDATE dispatch SET phase = 'cancelled', claim_key = NULL
                WHERE phase IN ('ready', 'owned') AND event_key IN (
                    SELECT event_key FROM messages WHERE stream_key = ?
                )
            """, (stream_key,))

    def get(self, event_key: str) -> dict:
        row = self.db.execute("""
            SELECT m.*, s.phase AS stream_phase, d.phase AS delivery_phase,
                   d.claim_key, d.provider_ack
            FROM messages m JOIN streams s USING (stream_key)
            JOIN dispatch d USING (event_key) WHERE m.event_key = ?
        """, (event_key,)).fetchone()
        if row is None:
            raise KeyError(event_key)
        return dict(row)


if __name__ == "__main__":
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as directory, Outbox(Path(directory) / "demo.sqlite") as box:
        box.admit(Event("demo-event", "demo-stream", "Synthetic notice"))
        claim = box.claim("demo-event")
        box.deliver("demo-event", claim, lambda body: "fake-provider-ack")
        box.finish("demo-stream")
        row = box.get("demo-event")
        print({key: row[key] for key in ("stream_phase", "delivery_phase", "provider_ack")})
