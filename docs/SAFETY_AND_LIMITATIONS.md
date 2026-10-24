# Safety and limitations

ASUMASNAM supplies operator-controlled decision support and research. Broker and options execution are disabled. AI assistance cannot override deterministic validation, qualification, membership, economic protection, or terminal-state gates. The operator independently decides whether to trade.

## Evidence and continuity

XSP uses approved AMEX:SPY confirmed five-minute market evidence. Screenshot interpretation or another feed cannot silently substitute for that authority. Source validation and continuity are distinct: a recent valid bar cannot prove earlier completeness. Missing, stale, malformed, mismatched, contradictory, or non-authoritative evidence cannot justify unsupported escalation. Production can still lose sources or fail admission under SQLite contention.

Stock Scout requires a ready frozen Anchor, validated selection, and durable research membership. Later information cannot silently change that basis. AI ranking attribution is specific to each run; an operational selection workflow is not proof of universal autonomous model ranking.

## Lifecycle and measurement

`WAIT`, `ENTRY`, `CONTRACT`, `PROTECT`, `TAKE PROFIT`, `INVALIDATED`, and `RESET` describe decision-support states. PROTECT and TAKE PROFIT are risk guidance, not proof of an executed order. A later independently qualified generation cannot reopen the previous terminal lifecycle.

A reference ASK is not a fill. Sampled MFE/MAE measures accepted quote observations relative to a reference; it is not continuous market extrema, an executable exit, or realized P&L. A terminal lifecycle can lack a final terminal quote. The October 23 review retained this omission and treated terminal economics as unknown.

## Delivery and recovery

Source persistence, job custody, outbox presence, provider acknowledgement, and device display are different facts. An uncertain send cannot justify blind replay. These mechanisms do not warrant an exactly-once external-delivery guarantee.

Reconciliation covers persisted sources within its authorized scope. It cannot recover requests never accepted into storage. Audit-only recovery does not generate historical trading actions, acquire historical contracts, call providers, or deliver old alerts. Complete custody for one cohort does not eliminate admission failures or source loss.

## Status and operational limits

The [dated evidence register](PUBLIC_PROOF_RELEASE.md) preserves unresolved source gaps, admission contention, delivery ambiguity, research terminal-quote omissions, delayed historical reset reporting, incomplete telemetry, and resource constraints. Deployed code, inspected tests, and natural acceptance remain distinct. Older X-publication and replay-readiness claims have not been re-established for the reviewed release.

Existing screenshots are historical; sample reports and JSON are synthetic illustrations, not production records. Expanded intraday discovery, public read-only MCP, cloud hosting, and replay-video rendering are future directions, not claimed shipped features.

The public repository excludes private strategy rules, thresholds, weights, schemas, configuration, destinations, credentials, accounts, operational logs, databases, and raw receipts. See the [broker boundary](BROKER_SAFETY_BOUNDARY.md) and [disclaimer](../DISCLAIMER.md).
