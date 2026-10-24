# Dated capability and evidence register

**As of October 24, 2026.** This register replaces the undated/August status labels previously used across the portfolio. It describes the October release reviewed in the architecture audit, not a fresh query of today's running process. Subsequent private candidates are not credited as deployed fixes.

## Evidence classes and provenance

- **Deployed:** source/release inspection and retained installation verification support presence, not exhaustive acceptance.
- **Natural observation:** a dated production path was observed. Its scope and unresolved failures remain attached.
- **Inspected tests:** retained regression tests were examined in the architecture review; production tests were not rerun for this portfolio.
- **Public reference tests:** independently authored educational code runs on synthetic fixtures; results apply only to that example.
- **Historical illustration:** older screenshots/examples explain a concept without establishing current capability.
- **Planned / not re-established:** no current deployment or natural-acceptance claim is made.

The October 24 architecture review corroborated the installed October release through its manifest, retained independent October 19 installation verification, October 23 runtime records, and a comparison of 21 relevant modules (19 exact matches; two line-ending-only differences). The exact private source revision was checked read-only during portfolio preparation. This identifies the reviewed baseline; it is not new runtime acceptance.

The October 23 end-of-day forensic review was supplied by the operator and inspected for this candidate, alongside retained activation/research summaries. Its aggregate conclusions below were **not independently reconstructed from production databases** during this work. Private raw evidence and release internals are retained outside the public repository.

## Capability-specific status

| Capability | Evidence date and class | Supported scope | Limits / release relationship |
| --- | --- | --- | --- |
| Structured ingress and XSP source authority | Oct 24 source/release review; Oct 23 natural review | Authenticated, validated structured evidence; AMEX:SPY confirmed five-minute authority | One Oct 23 SPY bar missing with unknown loss boundary; recent evidence is not proof of continuity |
| XSP qualification, contract monitoring, terminal ownership | Oct 24 deployed inspection; dated natural lifecycle records | Deterministic qualification and selected-contract economics constrain lifecycle state | Quote coverage is sampled; terminal closure does not imply a fill or realized result |
| Sequential XSP generations | Oct 22 observations in Oct 23 operator-supplied forensic review | Three sequential, nonoverlapping generations, consistent with authorized policy | Generation 2 ENTRY delivery remains ambiguous; this is not complete delivery acceptance or proof of every reversal route |
| Settled-reversal route | Oct 24 implementation review; Oct 23 natural review | Deployed policy path inspected | Not exercised on Oct 23; no universal natural-acceptance claim |
| Telegram notification ownership and ambiguity handling | Oct 24 deployed inspection and inspected fault tests; dated natural delivery records | Durable intent, conditional claims, sequencing, outcome classification | Provider acknowledgement is not device-display proof; Oct 22 ambiguity remains unresolved |
| Stock Scout frozen Anchor and native activation | Oct 23 retained activation summary; natural observation on reviewed release | Ready snapshot, accepted activation, exact membership verification | AI ranking participation is run-specific; no unrestricted autonomous ranking claim |
| Native selected-contract research | Oct 23 retained research summary and forensic review; natural observation | Contract/reference context persisted and native tracking initialized | Final terminal-quote acquisition omitted; terminal economics unknown; analogous Oct 21/22 omissions retained |
| Stock source/job reconciliation | Oct 16 independent cohort review; Oct 23 operator-supplied forensic review | Predecessor mechanism preserved in reviewed successor; 265 persisted sources mapped to 265 completed jobs, including ten audit-only recoveries on Oct 23 | Covers persisted sources only; historical recovery does not create trading actions or delivery |
| SQLite contention controls | Oct 24 deployed inspection; Oct 23 natural failures | Bounded work, indexing, transaction discipline, and downstream reconciliation | Nine post-persistence admission failures on Oct 23; recovered custody does not eliminate contention |
| Installation and release succession | Oct 19 retained independent verification; Oct 24 architecture review | Reviewed release identity and installed-source relationship corroborated | Separate from every natural runtime path; no later candidate automatically inherits deployed status |
| Failure-oriented production regression coverage | Oct 24 architecture review; inspected tests | Crash boundaries, identity conflicts, uncertain outcomes, recovery readiness | Tests inspected, not rerun here; fixtures do not establish natural acceptance |
| Public durable-outbox reference | Oct 24 authored educational example | Runnable synthetic admission, claiming, uncertainty, terminal tests | Independent schema; no private imports or production qualification |
| X opening/terminal public posting | August public baseline; historical claim | Earlier documentation recorded opening observations and a deployed terminal repair | Current-release posting acceptance not re-established; neither inherited success nor continued pending status is assumed |
| Replay evidence/readiness and video rendering | August public baseline; historical claim / planned consumer | Earlier documentation described OHLCV enrichment and readiness gates | Complete current-release replay acceptance not re-established; renderer not claimed shipped |
| Existing cockpit screenshots and sample reports | Historical public assets | Illustrate safety posture and synthetic review concepts | Not reviewed-release UI or natural production proof; no performance evidence |
| Expanded intraday discovery, public read-only MCP, cloud migration | Oct 24 roadmap | Future engineering directions | Not deployed capabilities in this portfolio |

## Measurement and acceptance rules

A reference ASK is not an executed fill. Sampled maximum favorable/adverse excursion (MFE/MAE) describes accepted quote samples relative to a reference; it does not establish continuous market extrema, an executable exit, terminal economics, or realized P&L. No outcome gallery, win rate, adoption, uptime, or universal latency claim is supported here.

Provider acknowledgement, outbox presence, custody completion, and human receipt are distinct. Audit-only recovery does not repair source loss before persistence or restore missed live actions. Source gaps, admission contention, delayed historical reset reporting, incomplete telemetry, and resource constraints remain relevant limitations.

See [XSP](DEMO_WALKTHROUGH.md), [Stock Scout](STOCK_SCOUT_WALKTHROUGH.md), [reliability](PRODUCTION_RELIABILITY.md), and [safety](SAFETY_AND_LIMITATIONS.md) for the meaning of each boundary.
