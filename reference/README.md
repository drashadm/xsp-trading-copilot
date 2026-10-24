# Durable event/outbox ownership reference

An **independently authored educational example** using generic synthetic notices, Python 3.11+ and standard-library SQLite. This is structurally illustrative, not copied production code, a production schema, a deployable worker, or proof of private-system acceptance. It has no network client, provider credentials, trading rules, or production imports. Use disposable databases only.

From the repository root:

```console
python -B reference/durable_outbox.py
python -B -m unittest discover -s reference -p "test_*.py" -v
python -B tools/validate_portfolio.py
```

The demo creates and removes a temporary database. Its fake sender returns an invented acknowledgement. Tests also create disposable fixtures; they contact no external service.

## Contract and state transitions

`Event(event_key, stream_key, body)` requires three nonblank strings, each at most 1024 characters. Missing/extra constructor fields and malformed values are rejected. A retained identity must match its original stream and body. There is no historical-data migration contract: this example creates its own fresh schema.

| Operation | Preconditions | Durable result |
| --- | --- | --- |
| `admit(event)` | New identity; stream not closed | Message and ready notification intent commit together; an exact duplicate is a no-op |
| `claim(event_key)` | Ready intent, active stream | One conditional owner receives a random claim key; competitors receive no claim |
| `deliver(event_key, claim_key, sender)` | Matching owner and active stream | Commit `uncertain` **before** invoking the sender outside a database transaction |
| Sender returns a nonblank acknowledgement | Same retained uncertainty fence | Record `acknowledged`; this is provider acknowledgement, not device-display proof |
| Sender raises, returns an invalid receipt, or receipt persistence fails | Send may have occurred | Exception propagates; retained phase remains `uncertain`; automatic replay is blocked |
| `finish(stream_key)` | Any stream, including one not previously seen | Persist closed state; cancel ready/owned work; preserve uncertain and acknowledged outcomes |

Delivery phases are `ready → owned → uncertain → acknowledged`. Ready/owned work can instead become `cancelled`. There is no transition back to ready. Exact duplicate admission after closure remains a no-op; a new event is rejected. A later independent stream has independent authority.

The pre-send fence is deliberately conservative. A crash immediately after it commits can leave an uncertain record even if no send occurred. A lost acknowledgement can leave uncertainty after a provider accepted the notice. This example has no automatic lease expiry, retry daemon, or manual uncertainty-resolution API. Abandoned claims require disposition outside the example. Progress is sacrificed rather than guessing that replay is safe.

Terminal closure serializes with the pre-send fence. If closure wins first, sending is blocked. If the fence wins first, closure cannot recall already-authorized external I/O; the receipt can still be recorded without reopening the stream. Closing a stream does not pretend to unsend a notice.

## Focused verification and limits

The tests cover durable atomic admission (including rollback after an injected insert failure), duplicate/conflicting identities, two competing connections, claim mismatch, I/O outside write transactions, retained acknowledgements, timeout ambiguity, failed receipt persistence, abandoned ownership, terminal closure, and malformed/partial input. One bounded two-thread race uses separate connections; other cases are serial.

Schema constraints and short `BEGIN IMMEDIATE` transactions enforce the illustrated boundaries. SQLite lock errors propagate; they are not reported as accepted work. Tests reopen databases to check committed state and inject database failures with synthetic triggers. They do not simulate power loss, certify storage hardware, prove exactly-once external delivery, benchmark contention, or validate production concurrency.

The production relationship is explained in the [reliability case study](../docs/PRODUCTION_RELIABILITY.md). Its persisted-source reconciliation, release succession, live qualification, and full notification sequencing are outside this deliberately small example.
