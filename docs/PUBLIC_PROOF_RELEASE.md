# Public Proof and Production Lessons

Public proof exists to make the decision path visible without turning selected-contract behavior into a subscriber-performance claim.

## Performance Truth

Public proof reports selected-contract behavior from its authoritative alert basis, including post-alert behavior. It does not represent subscriber execution or realized P/L.

The selected contract and contract price at alert are persisted with the decision. Post-alert contract high and maximum post-alert move refer to that exact contract—not a hypothetical or reconstructed entry.

No win rate, account-equity return, guaranteed result, or subscriber outcome is claimed.

## X Public Proof

### Production-proven opening proof

Automatic opening public proof is production-proven for qualified selected contracts. The public opening record can report:

- CALL or PUT
- selected contract
- expiration
- contract price at alert

### Deployed terminal route

The repaired terminal setup-complete route is deployed and awaiting natural production acceptance. It must not be described as naturally production-proven until a qualifying production lifecycle completes through that path.

Terminal public semantics describe the selected contract, alert basis, post-alert contract high, and maximum post-alert move. They do not claim realized P/L.

## Replay-Capable Evidence

Backend v1.4 support is deployed. It preserves replay-capable open, high, low, close, and volume bar evidence together with source and timestamp identity.

Live validity and replay capability are separate. A completed session must pass completeness and readiness checks before it is considered replay-ready. Partial, mixed, duplicate, discontinuous, or otherwise insufficient sessions remain non-ready even when some replay evidence exists.

The next complete natural production session is intended to provide the first full natural replay-readiness acceptance opportunity.

Replay rendering is a planned consumer of the evidence archive. A production replay-video renderer is not currently shipped, and no daily-video cadence is promised.

## Production Lessons

These cases describe problem → invariant → improvement. They are not a winner gallery and do not claim subscriber P/L.

### August 11 — Measure the selected contract

**Problem:** A qualified selected contract made the need for an exact post-alert measurement basis clear.

**Invariant:** Contract behavior is measured from the actual selected-contract price recorded at alert.

**Improvement:** Public proof stays attached to the persisted contract rather than a hypothetical entry.

### August 12 — Contract economics constrain optimism

**Problem:** Production evidence showed that market-state optimism could conflict with the economics of the selected contract.

**Invariant:** Selected-contract economics act as an independent safety authority.

**Improvement:** Clearly contradictory contract behavior cannot be hidden by optimistic lifecycle language.

### August 13 — Compose asynchronous evidence

**Problem:** Valid contract evidence could arrive after the initial market evaluation and fail to compose with its decision.

**Invariant:** Late evidence must be deterministically matched to the decision it belongs to.

**Improvement:** Related evidence can enrich the correct lifecycle without being forgotten or attached to an unrelated state.

### August 14 — Preserve evidence authority

**Problem:** A schema migration failed closed and blocked authority until the known-good evidence contract was restored.

**Invariant:** Migration and replay enrichment cannot silently bypass production evidence trust.

**Improvement:** Authority recovered before a later qualified PUT was evaluated and measured from its persisted alert basis.

## Current Status

| Status | Capability |
| --- | --- |
| Production-proven | deterministic lifecycle, AMEX:SPY authority, selected-contract context, Telegram lifecycle, automatic X opening proof, fail-closed handling |
| Deployed / awaiting natural acceptance | repaired X terminal route, first full natural-session replay-readiness acceptance for v1.4 |
| Roadmap | deterministic replay renderer and prior-day public replay/video artifacts |

## Public-Safety Boundary

This public proof omits exact strategy predicates, thresholds, freshness windows, contract-selection internals, correlation identities, provider configuration, private schemas, raw fixtures, credentials, account data, and operational receipts.
