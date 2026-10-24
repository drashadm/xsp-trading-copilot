# Public Screenshot Guidance

This folder contains public-safe visuals that demonstrate operator posture and safety boundaries without exposing private configuration, accounts, trading logic, or performance claims.

## Historical screenshots

- `01_live_opportunity_tape_public.png` — a historical operator-cockpit view demonstrating read-only posture and explicit execution boundaries.
- `02_market_closed_safety_state_public.png` — a market-closed safety state demonstrating that unavailable evidence prevents escalation.

Both assets are historical public illustrations. Neither has been established as representative of the October release reviewed on October 24, 2026. They illustrate safety concepts, not current UI, authoritative architecture, trading records, or subscriber-performance evidence. No image pixels were changed for this portfolio candidate.

The former replay scoreboard visual was retired because outcome labels could be read as realized-performance claims. It has not been replaced with a fabricated performance graphic.

## Current architecture

Use the [canonical architecture SVG](../diagrams/production-architecture.svg) and its [editable Mermaid source](../diagrams/production-architecture.mmd) for current component responsibilities. See the [evidence register](../../docs/PUBLIC_PROOF_RELEASE.md) for dated capability claims. Any future UI screenshot needs its own release and disclosure review.

## Never Include

- broker, account, order, or subscriber identifiers
- tokens, credentials, webhook secrets, or private destinations
- provider configuration, production paths, databases, or raw operational receipts
- exact thresholds, private predicates, correlation identities, or selector logic
- winner, realized-profit, win-rate, account-return, or guarantee framing
- language implying autonomous broker or options execution
