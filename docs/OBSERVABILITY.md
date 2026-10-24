# Evidence and auditability

The [canonical architecture](ARCHITECTURE.md) separates evidence, work custody, decisions, and communication. Observability must distinguish them too. The public description names responsibilities without publishing private schemas or raw receipts.

| Boundary | Question the retained evidence should answer | What it cannot establish alone |
| --- | --- | --- |
| Ingress | Was a request accepted, rejected, or unresolved? | A successful-looking response proves downstream completion |
| Source storage | Was approved evidence persisted with its source identity and time? | Persistence proves complete source continuity or job custody |
| Durable work | Does the source have exact downstream custody or an explicit disposition? | A completed job proves external delivery |
| Decision/research | Which validated evidence, policy, lifecycle, and selected contract produced this result? | A model summary grants decision or execution authority |
| Notification intent | Was publication eligible, withheld, claimed, or fenced? | An outbox row proves a recipient saw a message |
| Provider outcome | Was delivery acknowledged, definitively rejected, or uncertain? | Acknowledgement proves device display |
| Recovery | What persisted obligation was accounted for, and what side effects were excluded? | An audit disposition restores a missed historical action |

XSP observations remain attached to the selected contract and its reference basis. Stock research observations remain attached to authorized frozen membership and native lifecycle context. Late evidence must match its proper identity; it cannot rewrite a frozen decision basis or revive terminal work.

Installation identity, inspected tests, and natural observations receive separate entries in the [dated register](PUBLIC_PROOF_RELEASE.md). Exact operating-system dispatch, database commit instants, complete source coverage, and continuous quote extrema are not universally retained. Missing telemetry is reported as unknown rather than inferred from nearby successful events.

For a concrete example of custody evidence and its limits, see the [reliability case study](PRODUCTION_RELIABILITY.md). For independent runnable failure cases, see the [public reference](../reference/README.md). Neither is a benchmark or an end-to-end delivery guarantee.
