# Point-in-Time Rehearsal Sample

Timestamp: `As of 11:15 ET`  
Session date: `2099-01-15` synthetic  
Mode: no-lookahead public-safe rehearsal

## Evidence Available at That Moment

At `11:15 ET`, the system had only the evidence emitted up to that time:

* Opening range had formed.
* First break had occurred but did not show clean continuation.
* Price had rotated back toward the range.
* Invalidation context was visible.
* Chop guard remained active.

No later reversal, later trend extension, or end-of-day information was available to the rehearsal.

## Candidate Classification

Candidate classification: `suppressed_reversal_watch`

The candidate was not treated as execution-ready because continuation quality was incomplete and the chop guard remained active.

## Why Candidate Was Eligible or Suppressed

Suppressed because:

* evidence was mixed
* continuation was not validated
* first-break follow-through had weakened
* alert cooldown was active from a prior transition

Eligible for review because:

* structure had changed enough to record a candidate
* invalidation context was explicit
* the state was useful for later replay

## No-Lookahead Guard

This rehearsal uses only evidence available as of `11:15 ET`. Later price movement is excluded from candidate classification.

The no-lookahead guard prevents the report from rewriting a past decision with future information.

## Later Review

Later review showed that additional evidence arrived after `11:15 ET`, including a clearer reclaim sequence and improved structure quality.

That later evidence may explain why a future candidate became stronger, but it cannot be used to upgrade the `11:15 ET` candidate.

## What Changed After the Timestamp

* Reclaim evidence improved.
* Stale early-break assumptions were reduced.
* Alert outbox cooldown expired.
* Evidence tier improved from medium to high in the synthetic replay.

## What This Proves

* The system can rehearse decisions point-in-time.
* Candidate states can be suppressed without disappearing from review.
* Replay can separate what was known then from what became clear later.

## What This Does Not Prove

* It does not prove trading performance.
* It does not prove that the system predicted a move.
* It does not represent a broker order or execution.
* It is not financial advice.
