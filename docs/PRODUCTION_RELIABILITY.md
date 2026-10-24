# Case study: acknowledgement is not durable custody

Reviewed October 24, 2026. This sanitized account combines the retained October 14/16 reliability reviews with the operator-supplied October 23 forensic review. It publishes aggregate conclusions, not production payloads, schemas, logs, or private identities. Evidence classes and release relationships are recorded in the [register](PUBLIC_PROOF_RELEASE.md).

## The failure

A request can reach the application and persist source evidence without securing downstream job custody. A successful-looking request or a source row therefore cannot establish completed processing. SQLite enqueue contention made this distinction operationally important: an external acknowledgement and the durable work obligation could diverge.

The engineering problem was to account for accepted evidence without using recovery to manufacture historical live actions. A generic retry of every old source would risk duplicate notifications or inappropriate retrospective research.

## The correction and tradeoff

- **Make the boundaries visible.** Distinguish ingress outcome, source persistence, job custody, evaluation, notification intent, and provider outcome. Surface downstream admission failure instead of treating source persistence as end-to-end success.
- **Reconcile persisted obligations.** Forward reconciliation checks exact source/job custody within an authorized cohort and records explicit dispositions. Never-persisted requests remain outside its reach.
- **Constrain recovery effects.** Audit-only recovery accounts for historical work without delivery, entry creation, provider calls, contract acquisition, or terminal replay. It improves accountability without pretending to restore a missed live opportunity.
- **Reduce contention and constrain ownership.** Bounded work, targeted indexes, narrow write transactions, and external I/O outside inspected write scopes reduce pressure. Conditional claims and terminal guards prevent competing owners or stale work from becoming fresh authority.
- **Preserve uncertainty.** A possible send followed by a timeout is not safe to replay blindly. Fencing an ambiguous outcome sacrifices automatic progress until disposition; it does not pretend to guarantee exactly-once external delivery.

## Bounded production evidence

The October 16 independent review established custody for its inspected forward cohort and confirmed recovery dispositions without external delivery. That evidence concerned the predecessor deployment; the reviewed October successor preserved the mechanism under release-succession checks.

The October 23 forensic review reported **265 persisted Stock sources and 265 unique completed jobs: 255 normal jobs plus ten audit-only recoveries**. All required normal outboxes existed in that cohort. Recovery receipts recorded no delivery, entry, provider, contract-acquisition, or terminal-replay effects. Those results establish custody and dispositions for the examined persisted sources; an outbox is not proof of recipient display.

The same review retained **nine post-persistence admission failures**, all recovered into the cohort. Recovery did not erase those failures. It also found a missing SPY bar with an unknown loss boundary, missing research terminal-quote attempts, and unresolved October 22 ENTRY delivery ambiguity. Those findings block a claim of complete end-to-end acceptance.

## What an engineer can inspect publicly

The [independent SQLite reference](../reference/README.md) demonstrates atomic event/outbox admission, duplicate suppression, conditional claims, explicit uncertainty, and late-event rejection. Tests use disposable databases and a fake sender. It is educational code written for this portfolio, not a production export or proof that the private system passed these public tests.

No uptime, universal latency, profitability, or exactly-once delivery claim follows from this case. The operational achievement is a more precise account of custody, outcomes, and remaining gaps.
