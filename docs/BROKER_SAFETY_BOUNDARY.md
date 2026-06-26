# Broker Safety Boundary

Broker execution is separated from analysis because market evidence, deterministic posture, rehearsal, and live broker authority are different risk domains. The public proof package should make that separation obvious.

## Observe-Only Default

The default system posture is observe-only. Evidence can be ingested, classified, replayed, and reviewed without any broker execution authority.

## Paper Rehearsal Lane

Paper rehearsal tests decision packaging and timing without live order authority. It can help review whether the system had sufficient evidence at a point in time, but it does not place orders.

## Prepare-Only Live Package

A prepare-only package may assemble a supervised candidate for review. It stops before execution and does not create broker-side effects.

## Explicit Operator Approval

Any movement beyond preparation requires an explicit human decision point. Approval is not delegated to an LLM and should be recorded separately from analysis.

## Abandon / Release Lifecycle

Prepared-but-not-executed candidates must have an abandon or release path. If the operator does not approve, if evidence goes stale, or if policy is missing, the candidate is abandoned and any reserved budget is released.

## Broker Rejection Normalization

If broker interaction exists in a separately enabled environment, broker rejections should be normalized into safe audit states. Public artifacts should not expose raw account identifiers, broker IDs, order IDs, tokens, or raw MCP responses.

## Options Live Execution Boundary

Options live execution is disabled/fail-closed unless official tools and a separate safety stack exist. Analysis, paper rehearsal, and prepare-only packages must not be described as live options execution.

## Public Artifact Exclusions

No raw account numbers, broker IDs, order IDs, tokens, webhook secrets, chat IDs, or MCP responses belong in public artifacts.

| Lane | Purpose | Live authority? |
| --- | --- | --- |
| Analysis | classify evidence and posture | No |
| Paper rehearsal | test decision packaging | No |
| Prepare-only package | assemble supervised candidate | No |
| Operator approval | explicit human decision point | Yes, approval only |
| Broker call | one supervised action after approval | Yes, bounded |
| Audit | record result/rejection | No |
