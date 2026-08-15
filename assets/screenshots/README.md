# Public Screenshot Guidance

This folder contains public-safe visuals that demonstrate operator posture and safety boundaries without exposing private configuration, accounts, trading logic, or performance claims.

## Included Public Proof Screenshots

- `01_live_opportunity_tape_public.png` — a historical operator-cockpit view demonstrating read-only posture and explicit execution boundaries.
- `02_market_closed_safety_state_public.png` — a market-closed safety state demonstrating that unavailable evidence prevents escalation.

These assets illustrate safety concepts. They are not the current authoritative architecture, trading records, or subscriber-performance evidence.

The former replay scoreboard visual was retired because outcome labels could be read as realized-performance claims. It has not been replaced with a fabricated performance graphic.

## Preferred Future Visuals

- evidence-first architecture
- subscriber lifecycle
- selected-contract public-proof example using authoritative alert-basis semantics
- replay-capable evidence and readiness distinction

Prefer maintainable Mermaid diagrams in the documentation unless a screenshot adds unique public-proof value.

## Never Include

- broker, account, order, or subscriber identifiers
- tokens, credentials, webhook secrets, or private destinations
- provider configuration, production paths, databases, or raw operational receipts
- exact thresholds, private predicates, correlation identities, or selector logic
- winner, realized-profit, win-rate, account-return, or guarantee framing
- language implying autonomous broker or options execution
