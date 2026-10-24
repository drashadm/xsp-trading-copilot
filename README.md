# ASUMASNAM

**An operator-controlled market decision-support and research platform.**

ASUMASNAM turns structured market evidence into deterministic decision lifecycles, selected-contract monitoring, and auditable notifications. Built and operated under the constraints of a local Windows deployment, it demonstrates the engineering behind external integrations, bounded AI assistance, durable background work, and incident recovery.

**AI proposes; deterministic code enforces; the operator decides. Broker and options execution are disabled.**

This public portfolio explains the production architecture and provides an independent, runnable engineering example. The private application, trading rules, configuration, and operational data are excluded.

## Two workflows

**[XSP decision support](docs/DEMO_WALKTHROUGH.md)** follows validated AMEX:SPY evidence through setup qualification, exact contract selection, economic monitoring, risk guidance, and terminal closure. A later setup must qualify independently after the previous ownership is released. A reference quote records a decision basis; it is not an executed fill.

**[Stock Scout research](docs/STOCK_SCOUT_WALKTHROUGH.md)** starts with readiness checks and a frozen candidate snapshot called the Anchor. Advisory ranking stays within that snapshot; native validation admits the selected research universe. Authorized option research then persists contract context and monitors quotes. Later observations cannot silently rewrite the frozen basis.

## Architecture

![Structured evidence, deterministic workflows, durable delivery, and audit-only recovery](assets/diagrams/production-architecture.svg)

[Architecture and authority map](docs/ARCHITECTURE.md) · [Editable Mermaid source](assets/diagrams/production-architecture.mmd)

Production stack: Python, SQLite, structured webhook ingress, bounded background workers, a Streamlit operator interface, read-only market-data integrations, and Telegram communication.

## Engineering evidence

- **Durable work:** persisted evidence, downstream job custody, evaluation, and delivery are separate obligations. The [reliability case study](docs/PRODUCTION_RELIABILITY.md) explains how reconciliation repairs custody without replaying historical trading actions.
- **Explicit uncertainty:** conditional ownership, duplicate suppression, terminal boundaries, and uncertain-send handling prevent unsupported retries. Run the [educational SQLite outbox example](reference/README.md) locally with Python and no third-party dependencies.
- **Release discipline:** reviewed source identity, installation verification, fault-oriented tests, and natural production observations are tracked separately. AI-assisted engineering is assessed through reviewed changes and validation evidence, not model-generated confidence.

## Status and limits

The [evidence register, reviewed October 24, 2026](docs/PUBLIC_PROOF_RELEASE.md), separates deployed capabilities, observed production paths, inspected tests, historical illustrations, and planned work. October observations include sequential XSP generations and complete custody for a bounded persisted Stock cohort. They also retain an ambiguous delivery, source gaps, recurring SQLite admission contention, and missing research terminal quotes.

Provider acknowledgement does not prove device display. Sampled MFE/MAE describes quote excursions, not realized P&L. Reconciliation cannot recover requests that never reached storage. Existing [screenshots](assets/screenshots/README.md) are historical illustrations.

Intraday Stock Scout discovery, a public read-only MCP service, and cloud migration remain roadmap items. Current acceptance of older X-posting and replay claims has not been re-established.

[Observability](docs/OBSERVABILITY.md) · [Synthetic examples](examples/README.md) · [Safety and limitations](docs/SAFETY_AND_LIMITATIONS.md) · [Broker boundary](docs/BROKER_SAFETY_BOUNDARY.md) · [Disclaimer](DISCLAIMER.md)
