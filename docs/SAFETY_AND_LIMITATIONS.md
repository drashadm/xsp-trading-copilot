# Safety and Limitations

ASUMASNAM XSP is deterministic decision support, not automated execution.

## Current Safety Boundaries

- The operator makes every trading decision.
- Broker execution and options execution are disabled.
- AI output cannot override deterministic evidence, qualification, lifecycle, invalidation, or safety gates.
- Missing, stale, malformed, mismatched, contradictory, or non-authoritative evidence fails closed.
- Selected-contract economics independently constrain optimistic lifecycle language.
- Delayed evidence cannot resurrect a completed or invalidated decision.

## Evidence Limitations

Production market authority is AMEX:SPY using confirmed five-minute bars. BATS is not current production authority. Evidence from another source or timeframe cannot silently substitute for the approved contract.

Fail-closed rules can withhold a state that a human might still find interesting. That conservative posture is intentional: absence of validated evidence is not evidence of readiness.

## Lifecycle Limitations

WAIT, ENTRY, CONTRACT, PROTECT, TAKE PROFIT, INVALIDATED, and RESET are decision-support states.

PROTECT and TAKE PROFIT are risk guidance. They do not prove that a subscriber placed, modified, or closed a position. INVALIDATED means the thesis no longer qualifies under the system's evidence contract.

## Selected-Contract and Public-Proof Limitations

Public proof follows the exact selected contract from its authoritative alert basis and may describe post-alert contract behavior. It does not represent subscriber execution, realized P/L, account equity, or a guaranteed outcome.

Automatic X opening proof is production-proven. The repaired terminal posting route is deployed but still awaits natural production acceptance; autonomous terminal publication is not yet claimed as naturally proven.

## Replay Limitations

Backend v1.4 support preserves replay-capable OHLCV evidence, but evidence presence alone does not make a session replay-ready. Completeness and readiness checks must pass.

The next complete natural production session is intended to provide the first full natural replay-readiness acceptance opportunity. A production replay-video renderer is not currently shipped.

## AI Boundary

AI-assisted engineering or perception may support the system. Deterministic code governs production decisions, and the operator remains in control. AI is not a contract-selection, lifecycle, public-proof, or execution authority.

## Public Repository Scope

This repository intentionally excludes credentials, account data, private configuration, production paths, databases, raw operational receipts, exact thresholds, detailed predicates, proprietary selector logic, correlation identities, full private schemas, and reconstructable regression fixtures.
