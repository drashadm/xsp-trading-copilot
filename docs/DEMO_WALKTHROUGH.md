# XSP decision-support walkthrough

This narrative follows the reviewed production architecture. The identities below are invented; the sequence illustrates responsibilities rather than replaying a production session or publishing private qualification rules. [Architecture](ARCHITECTURE.md) · [Dated evidence](PUBLIC_PROOF_RELEASE.md).

## From observation to selected contract

1. **Admit evidence.** Structured TradingView observations are authenticated and validated. XSP requires the approved AMEX:SPY confirmed-bar authority. Persistence and durable downstream custody are checked separately; receipt of an HTTP request alone proves neither.
2. **Qualify a setup.** Deterministic code assesses eligibility and source continuity. `WAIT` communicates insufficient evidence. A fresh observation does not erase a missing earlier source. AI summaries cannot override a block.
3. **Attach the selected contract.** A qualified `ENTRY` leads to persisted contract context and its reference quote. Synthetic identity `DEMO_CONTRACT_A` belongs only to `DEMO_SETUP_A`. Selection is read-only research, not an order. A reference ASK is not a fill.
4. **Monitor economics and lifecycle.** Later quotes and market evidence compose only with the matching setup and contract. Selected-contract economics can constrain optimistic market-state language. `PROTECT` and `TAKE PROFIT` express risk guidance; they do not demonstrate an operator sale or profit.
5. **Communicate through durable intents.** Eligible transitions create notification work. Conditional claims and sequencing checks constrain ownership. A provider acknowledgement is recorded as such. An uncertain send remains uncertain and cannot justify a blind retry.
6. **Close and reconcile.** Invalidation, economic protection, or session closure can terminalize the lifecycle. `INVALIDATED` describes a thesis that no longer qualifies; `RESET` is session closure. Delayed evidence cannot reopen that lifecycle. Terminal reconciliation releases setup ownership where policy permits.
7. **Qualify later work independently.** A later `DEMO_SETUP_B` needs its own evidence, contract context, and qualification. It cannot reuse setup A's authority simply because A ended. Sequential generations are separate lifecycles, not overlapping ownership or continuation of a closed thesis.

## Inspect the boundaries

| Synthetic event | Permitted result | Blocked inference |
| --- | --- | --- |
| A required source is missing | Withhold unsupported qualification; record the gap | A current quote proves complete market history |
| A quote arrives for setup A after A is terminal | Preserve terminal state; retain evidence under its proper identity | Reopen A or attach its quote to B |
| A notification times out after a possible send | Fence the outcome as uncertain pending disposition | Replay automatically because no acknowledgement was retained |
| Setup A closes and later evidence qualifies B | Admit B independently within session policy | Every terminal closure guarantees another eligible setup |
| A sampled BID rises above the reference ASK | Describe a sampled quote excursion | Report a filled trade or realized P&L |

## What the retained evidence establishes

The October 23 forensic review reports three sequential, nonoverlapping generations on October 22, consistent with the authorized policy. Generation 2's ENTRY delivery remains ambiguous. That observation supports a particular natural sequence; it does not establish universal delivery reliability or acceptance of every reversal path. The settled-reversal route was not exercised on October 23.

Existing cockpit [screenshots](../assets/screenshots/README.md) are historical illustrations. They are not current-release screenshots or proof of this sequence. The [synthetic recommendation](../examples/sample_automatic_contract_recommendation.json) deliberately has disabled execution semantics and is not a production payload contract.

The operator independently decides whether to trade. This path has no active approval-to-order route. See the [broker boundary](BROKER_SAFETY_BOUNDARY.md) and [measurement limits](SAFETY_AND_LIMITATIONS.md).
