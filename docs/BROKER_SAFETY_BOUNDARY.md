# Broker Safety Boundary

ASUMASNAM XSP is decision support. The operator decides whether to trade.

## Current Product State

| Capability | Current status |
| --- | --- |
| Market-evidence validation | Enabled |
| Deterministic decision lifecycle | Enabled |
| Selected-contract research and context | Enabled |
| Subscriber communication and public proof | Enabled within deterministic gates |
| Broker execution | **Disabled** |
| Options execution | **Disabled** |

There is no active approval-to-broker-call path in the current product. Analysis, contract context, lifecycle guidance, communication, and public proof do not place orders or create broker-side effects.

## Operator Boundary

The operator independently decides whether to trade and, if so, acts outside ASUMASNAM XSP. No LLM, Telegram message, lifecycle state, public-proof artifact, or recommendation can grant execution authority.

## Failure Posture

- Missing or invalid evidence fails closed.
- Missing selected-contract context cannot be silently reconstructed into an execution claim.
- Communication failures remain communication failures; they cannot become order actions.
- Delayed evidence cannot reopen a terminal decision.

## Public Artifact Exclusions

Public materials must not include account identifiers, order identifiers, credentials, webhook secrets, Telegram destinations, provider configuration, private filesystem/database paths, raw operational receipts, or execution-shaped payloads.

Historical architecture exploration involving broker integration is outside the current public product and must not be presented as active capability.
