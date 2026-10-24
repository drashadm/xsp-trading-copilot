# Stock Scout research walkthrough

Stock Scout is a bounded research workflow built around a frozen decision basis. This account describes the reviewed release; it does not expose ranking weights, private candidate rules, payloads, or provider configuration. [Architecture](ARCHITECTURE.md) · [Dated evidence](PUBLIC_PROOF_RELEASE.md).

## Freeze, select, research

1. **Establish readiness.** Native checks determine whether evidence is ready for a candidate snapshot. Incomplete readiness cannot be converted into a valid Anchor by a ranking proposal.
2. **Freeze the Anchor.** The Anchor fixes the candidate pool and its evidence identity for that workflow. Later observations cannot silently rewrite it. Synthetic candidates `DEMO_ALPHA` and `DEMO_BETA` illustrate membership only; they are not securities recommendations.
3. **Propose a bounded ranking.** The operator or an AI-assisted workflow may rank within the frozen pool. AI participation must be attributed to the specific run. A ranking artifact alone does not prove that an autonomous model performed the selection.
4. **Validate and activate natively.** Native code checks snapshot identity and selected membership before accepting the research universe. A proposal that includes `DEMO_GAMMA` from outside the pool cannot expand authorization. Accepted activation locks the decision basis; conflicting requests are not alternative authority.
5. **Start authorized research.** A research start must match durable universe membership and source authority. Native services persist the chosen contract and immutable reference quote before following that contract. A research start is neither a fill nor trading approval.
6. **Monitor and terminalize.** Native workers refresh selected-contract observations and communicate permitted research states through durable notification work. Confirmed invalidation or other terminal conditions close the lifecycle. A terminal record and a final terminal quote are separate facts: one can exist while the other is missing.

## Persistence and recovery are separate from research

Persisted Stock sources can be reconciled against downstream job custody. A source that lacks custody receives bounded treatment or an explicit disposition. Audit-only recovery cannot replay historical research entries, acquire old contracts, call providers, or send old alerts. It cannot recreate an incoming request that never reached storage.

| Situation | Required boundary |
| --- | --- |
| Snapshot not ready or its identity mismatches | Do not accept a proposed research universe |
| Ranking contains an outside candidate | Do not broaden frozen membership |
| Activation submission has an uncertain response | Verify durable acceptance before assuming absence or submitting conflicting work |
| Research quote is absent or stale | Keep the limitation visible; do not invent current economics |
| Old source lacks downstream custody | Reconcile only within the authorized persisted-source scope |
| Lifecycle is terminal and a quote arrives late | Preserve terminal state and the quote's proper identity |

## What was observed

Retained October 23 activation records establish a ready Anchor, native activation, and exact frozen membership verification on the reviewed release. Separate native research records establish persisted contract/reference context and tracking initialization. These are observations of specific paths, not exhaustive production acceptance.

The later October 23 forensic review found complete downstream custody for 265 persisted Stock sources, including ten audit-only recoveries. It also retained nine post-persistence admission failures and missing terminal-quote acquisition in the research lifecycle. A healthy provider status did not prove that a final quote had been attempted. Sampled MFE/MAE therefore cannot establish terminal economics or realized P&L.

Expanded intraday candidate discovery is a roadmap item. This workflow does not establish a public MCP service or a cloud deployment. See [safety and limitations](SAFETY_AND_LIMITATIONS.md).
