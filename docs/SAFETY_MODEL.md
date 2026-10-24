# Safety model

**AI proposes; deterministic code enforces; the operator decides.** Broker and options execution are disabled.

The [architecture authority map](ARCHITECTURE.md#authority-map) is the canonical component description. These are its public safety invariants:

- Approved structured source authority must be established before qualification. Freshness does not erase source gaps.
- Native code owns qualification, membership validation, economic protection, lifecycle state, and publication eligibility. AI proposals cannot bypass those gates.
- Stock selection stays within its frozen Anchor. A ranking proposal alone grants no native research authority.
- Selected-contract observations must match the correct lifecycle and reference basis. Missing or mismatched evidence cannot be silently upgraded.
- Terminal state cannot be reopened by delayed work. A later XSP generation qualifies independently after ownership release where policy allows.
- Durable custody is distinct from delivery. Conditional ownership and uncertain-outcome fencing constrain retries.
- Recovery accounts for already-persisted obligations through its authorized audit-only path; it cannot create historical trading actions or notification delivery.
- A reference quote, lifecycle label, or provider acknowledgement cannot establish an order, fill, realized result, or human receipt.

These invariants describe intended enforcement boundaries, not perfect operation. See the [dated limitations](PUBLIC_PROOF_RELEASE.md), [XSP walkthrough](DEMO_WALKTHROUGH.md), [Stock Scout walkthrough](STOCK_SCOUT_WALKTHROUGH.md), and [broker boundary](BROKER_SAFETY_BOUNDARY.md).
