# Replay Report Sample

Session date: `2099-01-15` synthetic  
Instrument: XSP/SPY evidence simulation  
Report type: Public-safe replay example

## Session Summary

This synthetic replay demonstrates how a session review can describe evidence progression, candidate timing, noise, and missing context without exposing raw logs or claiming performance.

## First Major Reversal Timestamp

First major reversal candidate observed: `11:42 ET`

At that point, the replay showed a shift from weak continuation to inside-range rotation with a reclaim attempt. The report marks this as a review candidate, not a prediction.

## Evidence Tier Progression

| Time | Evidence tier | Notes |
| --- | --- | --- |
| 09:45 ET | Low | Opening range still forming; no durable structure. |
| 10:15 ET | Medium | First break observed, but follow-through incomplete. |
| 11:15 ET | Medium | Candidate structure present; chop guard still active. |
| 11:42 ET | High | Reversal evidence improved after reclaim sequence. |
| 13:10 ET | Low | Evidence became stale; alerts suppressed. |

## Max Favorable Move After Candidate Signal

The synthetic report records that the reviewed candidate had a favorable follow-through window after `11:42 ET`.

This field is included to demonstrate replay analysis mechanics only. It is not a profit/loss claim and does not prove predictive accuracy.

## Noise Flags

* Early failed break.
* Inside-range rotation.
* Stale evidence window after midday.
* Conflicting continuation signals before the reversal candidate.

## Opportunity Flags

* Reclaim sequence became clearer after the first failed continuation attempt.
* Invalidation context was explicit.
* Alert outbox prevented repeated notifications during cooldown.

## Missing Evidence Gaps

* No public screenshot is included in this sample.
* Option-chain details are omitted.
* Broker/account artifacts are intentionally excluded.
* Contract-level outcome attribution is not included.

## Lessons Learned

* Replay value comes from reviewing what the system knew at the time.
* Suppression is useful when evidence is ambiguous or stale.
* A candidate can be review-worthy without being an instruction to trade.

## What This Proves

* Session artifacts can be replayed.
* Evidence quality can be tracked over time.
* Candidate timing can be reviewed without lookahead.
* Suppression and stale-evidence states can be audited.

## What This Does Not Prove

* It does not prove profitability.
* It does not prove market prediction.
* It does not represent a real trade.
* It does not show broker execution.
* It does not provide financial advice.
