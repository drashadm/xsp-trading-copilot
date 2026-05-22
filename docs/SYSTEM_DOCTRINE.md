# System Doctrine

This document captures the doctrine behind XSP Trading Copilot, designed around deterministic enforcement, operator control, and intraday only market structure interpretation.

## Instrument Roles

SPY is the reference instrument. XSP 0DTE is the recommendation context.

The system observes SPY structure as the primary market proxy for intraday interpretation. XSP contract recommendation artifacts are derived only after deterministic eligibility and read only recommendation gates are satisfied.

## OH / OL Structure Anchors

Opening high (OH) and opening low (OL) are the primary intraday structure anchors. The system evaluates where current price is relative to those boundaries and whether breaks, failures, or reclaims have occurred.

Key concepts:

- Above OH can support bullish continuation only when structure confirms.
- Below OL can support bearish continuation only when structure confirms.
- Inside range rotation weakens directional conviction.
- Failed breaks and returns to range increase chop risk.

## First Break Logic

The first break of the opening range is an initial bias candidate, not a final decision. First break direction must be supported by follow through structure before the system promotes a trend state.

The first break establishes the session's initial directional hypothesis. It is not sufficient by itself.

## Reclaim-Only Reversals

Reversals require reclaim behavior. A reversal is not valid merely because price moves away from an extreme. The broken level must be reclaimed in a way that supports a new directional interpretation.

This rule prevents premature reversal labels after weak counter-moves or noisy range rotation.

## Continuation Requirements

Continuation requires structure plus directional support. A trend label requires evidence such as higher highs for bullish continuation or lower lows for bearish continuation, along with directional confirmation from supporting signals such as DI bias or volume bias.

Weak continuation is suppressed rather than promoted.

## Fake Breakout Chop

`fake_breakout_chop` describes repeated failed breaks, inside-range rotation, or reclaim after break behavior that undermines continuation. It is a low conviction environment and should be treated as a warning state, not an opportunity label.

## No Cross-Day Bias

Each trading day starts as a blank slate. Prior session behavior is not carried forward as bias.

This avoids stale narrative drift and keeps the system anchored to current session structure.

## Intraday Memory Allowed

Intraday memory is allowed and important. The system may track same-day OH/OL breaks, failed breaks, returns inside range, and double failure behavior.

This memory is session scoped. It informs same day suppression and context without becoming a cross day prediction engine.

## Deterministic Authority

Deterministic services are the source of truth for classification and gating. LLMs may extract observations or provide optional verification, but they never override deterministic outputs.

Authoritative deterministic responsibilities include:

- regime classification
- structure enrichment
- setup clarity
- confidence scoring
- tradeability scoring
- contract selection
- recommendation issuance / suppression

## Operator Control

The system is not an auto trader. It does not place orders or execute trades. The human operator remains in control of all trading decisions.

The operating philosophy is simple: LLMs propose. Code enforces. The operator decides.