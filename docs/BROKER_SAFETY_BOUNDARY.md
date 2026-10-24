# Broker Safety Boundary

ASUMASNAM provides XSP decision support and Stock Scout research. The operator decides whether to trade. Capability evidence is dated in the [status register](PUBLIC_PROOF_RELEASE.md).

## Current Product State

| Capability | Current status |
| --- | --- |
| Market-evidence validation | Enabled |
| Deterministic decision lifecycle | Enabled |
| Selected-contract research and context | Enabled |
| Telegram communication | Enabled within deterministic gates; delivery outcomes have separate evidence |
| X public posting | Current acceptance not re-established; see the dated register |
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

Historical architecture exploration involving broker integration is outside the current public product and must not be presented as active capability. A research activation, selected contract, risk-guidance label, or synthetic recommendation cannot authorize a broker action. The public [recommendation example](../examples/sample_automatic_contract_recommendation.json) explicitly disables execution.
