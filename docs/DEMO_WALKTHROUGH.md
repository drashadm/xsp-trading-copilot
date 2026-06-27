# Demo Walkthrough

## Purpose

This walkthrough shows how the public proof package should be reviewed. The system is best understood as a market evidence copilot: it ingests live TradingView evidence, validates and stores it, classifies market state through deterministic gates, and keeps execution authority separated, explicit, gated, and auditable.

## Reviewer Path

1. Read the README opening and safety boundaries.
2. Review the safety model in `docs/SAFETY_MODEL.md`.
3. Inspect the replay and rehearsal examples in `examples/`.
4. Check the alert outbox sample for suppression, cooldown, and duplicate protection.
5. Review the broker safety boundary before inferring anything about execution.

## Demo Narrative

1. TradingView sends structured evidence.
2. The app validates and stores it.
3. The Live Opportunity Tape turns evidence into conservative market posture.
4. Replay reports show whether the system saw opportunities early enough.
5. Alerts go to an outbox first, with suppression reasons and cooldowns.
6. Execution is separate, gated, explicit, and auditable.

## Step 1: TradingView Evidence Is Emitted

The system begins with live market evidence from TradingView. Public examples should describe the evidence shape without exposing private webhook URLs, alerts, chat IDs, screenshots, account identifiers, or raw payloads from a private environment.

## Step 2: Webhook Receiver Validates and Stores Evidence

Incoming evidence is treated as untrusted. The receiver validates required fields, rejects malformed payloads, and stores accepted records for replayable review.

Malformed or stale evidence fails closed. The system should never fabricate a market posture from missing or ambiguous input.

## Step 3: Live Opportunity Tape Surfaces Operator Posture

The Live Opportunity Tape is an operator-facing surface. It turns validated evidence into conservative posture language such as stand aside, observe, eligible for rehearsal, or suppressed.

This surface is not a broker order panel. It is a decision-support display.

## Step 4: Replay Reports Review the Session

Replay reports reconstruct what the system saw during a session and how evidence quality evolved over time. They support review of timing, missing evidence gaps, suppression reasons, and candidate eligibility.

Replay reports are review artifacts. They are not financial performance claims.

## Step 5: Alert Outbox Records Suppressed/Eligible Alert Transitions

Alerts move through an outbox before delivery. The outbox can record eligible dry-run alerts, cooldown suppression, stale-evidence suppression, and duplicate-transition suppression.

The outbox makes alert behavior auditable instead of invisible.

## Step 6: Paper Rehearsal and Broker Safety Lanes Remain Separated

Paper rehearsal can test decision packaging without live authority. Prepare-only live packages can assemble a supervised candidate but stop before execution.

Live options execution remains disabled/fail-closed unless official execution tooling and a separate safety policy exist.

## What to Look For

* Clear separation between evidence, analysis, rehearsal, preparation, approval, broker action, and audit.
* Conservative posture when evidence is stale, ambiguous, or low quality.
* No-lookahead review in point-in-time examples.
* Suppression reasons in alert examples.
* Synthetic public-safe values rather than private artifacts.

## What Not to Infer

* Do not infer guaranteed trading results.
* Do not infer autonomous trading.
* Do not infer broker execution authority from analysis or rehearsal artifacts.
* Do not infer that LLM output can override deterministic gates.
* Do not infer contract-level performance attribution from synthetic examples.
