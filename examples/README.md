# Synthetic example index

All values in this directory are invented. These files are public teaching illustrations, not production payloads, strategy rules, live quotes, test results, or records of execution. They are not a supported API/schema. No trading application consumes these files; the offline validator checks them as documentation.

| Files | Classification and use |
| --- | --- |
| [sample_automatic_contract_recommendation.json](sample_automatic_contract_recommendation.json) | Updated synthetic recommendation: suppressed issuance, recommendation only, execution disabled, no approval |
| [sample_operator_agent_response.json](sample_operator_agent_response.json) | Historical synthetic read-only tool response; does not establish a deployed public agent or MCP service |
| [sample_market_state.json](sample_market_state.json), [sample_pipeline_result.json](sample_pipeline_result.json), [sample_tradeability.json](sample_tradeability.json) | Historical simplified state/analysis shapes; scores and reasons are invented and are not current qualification rules |
| [alert_outbox_sample.json](alert_outbox_sample.json) | Historical dry-run suppression illustration; its timing values and shape are not production controls |
| [public_app_state_sample.json](public_app_state_sample.json) | Historical operator-posture illustration, not the current UI or production schema |
| [point_in_time_rehearsal_sample.md](point_in_time_rehearsal_sample.md), [replay_report_sample.md](replay_report_sample.md) | Historical synthetic review narratives, not natural acceptance or evidence of a shipped renderer |

The recommendation's former execution-shaped approval object was replaced intentionally: `decision_support` says execution is disabled and approval is not applicable. Retained suppression and quote fields remain illustrative. No production migration is implied; external readers of older examples must treat this as a revised illustration, not a compatible API response.

For executable engineering evidence, use the [independent durable-outbox reference](../reference/README.md). For production capabilities, use the [dated register](../docs/PUBLIC_PROOF_RELEASE.md).
