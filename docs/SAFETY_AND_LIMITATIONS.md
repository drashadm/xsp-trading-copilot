# Safety and Limitations

The system is designed as deterministic decision support, not automated execution. This document describes the public safety boundaries and known limitations.

## Safety Boundaries

The system is not an auto-trader. It does not place broker orders, execute trades, or manage positions.

The operator controls all action outside the system. Every execution step is manual and discretionary.

The system is not financial advice. Outputs are research and decision support artifacts, not instructions to buy or sell securities.

## LLM Authority Boundary

LLMs are non-authoritative. They are used for:

- screenshot perception
- optional verification
- bounded read-only operator-agent classification

They are not used as the regime authority, confidence authority, tradeability authority, contract selection authority, or broker execution authority.

## Verifier Boundary

The verifier is additive only. It may provide agreement, disagreement, setup quality, confidence context, or an operator note. It cannot override deterministic decisions.

If verifier output is missing, malformed, or unavailable, the pipeline continues without treating the verifier as authoritative.

## Read-Only Tool Calls

Market data and operator agent tool calls are read only. The full local tool harness is allowlisted and designed to fail closed on unknown tools, malformed arguments, unsupported requests, and provider failures.

No tool in the documented operator-agent boundary has broker execution authority.

## Contract Recommendation Boundary

Contract recommendation is recommendation only. The automatic contract recommendation path packages an artifact after upstream deterministic eligibility has already been established.

It does not:

- place orders
- call broker execution APIs
- create new trade eligibility doctrine
- mutate approval state
- override regime, confidence, or tradeability

## Known Limitations

- **OpenAI latency**: Vision extraction can be slow during live use because screenshot interpretation depends on a remote model call.
- **Vision extraction variability**: Chart layout, image quality, and visual ambiguity can affect extracted fields.
- **Prompt/JSON formatting risk**: Model output may include malformed JSON, markdown fences, missing fields, or unexpected values. Schema validation and output cleaning reduce this risk but do not eliminate it.
- **Possible over-suppression**: Fail-closed and suppression rules may block or downgrade states that a human would still consider useful.
- **Recommendation-only contract path**: Contract recommendations are display artifacts for operator review, not execution instructions.
- **Contract-level outcome tracking is still in progress**: Engine-level outcome review exists in the private system, but complete attribution for agent-called contract recommendations is not claimed.

## Public Repository Scope

This repository intentionally excludes secrets, credentials, raw screenshots, raw trading logs, broker/account data, database files, local production paths, `.env` values, and proprietary live configuration.