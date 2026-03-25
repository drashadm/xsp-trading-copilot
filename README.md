# XSP Trading Copilot

**A real time AI decision support system that interprets price action using vision, deterministic logic, and multimodal validation.**

---

## What This Is

XSP Trading Copilot is a **governance first AI system** designed to:

* interpret intraday market structure
* maintain session level state
* classify market regimes deterministically
* deliver structured, real time decision context

This system does **not execute trades**.

It acts as a **decision support layer for discretionary execution**, prioritizing clarity, discipline, and capital preservation.

---

## Core Architecture

The system is built around strict separation of concerns:

---

### Perception Layer (AI Vision)

* Ingests charts
* Extracts structured market state using OpenAI vision models
* Outputs strict JSON schema

> **LLM is perception only — never decision authority**

---

### State & Memory Layer

* Tracks intraday structure:

  * Opening interactions
  * break attempts
  * failed moves
  * returns to range
* Maintains **session only memory**
* Enforces **no cross day bias**

---

### Decision Engine (Deterministic)

* Classifies market regimes using ordered rule logic
* Fully independent of the LLM
* Produces:

  * regime classification
  * directional bias
  * invalidation levels

> **This is the authoritative layer of the system**

---

### Evaluation Layer

* Confidence scoring (directional conviction)
* Setup clarity scoring (visual cleanliness)
* Tradeability + environment quality
* Structure aware interpretation

---

### Verification Layer (Multimodal AI)

* Performs a second-pass validation using:

  * chart inputs
  * deterministic engine output
* Evaluates:

  * agreement / disagreement
  * setup quality
  * confidence
  * operator facing context

> This layer is **additive only** and never overrides deterministic decisions.

---

### Output Layer

* Telegram alerts (real time, decision first formatting)
* Streamlit dashboard (interactive operator interface)
* SQLite snapshots (session history + journaling)

---

## End-to-End Flow

```
Chart Ingestion
→ Vision Extraction (AI)
→ Schema Validation
→ Market State Normalization
→ Regime Classification (Deterministic)
→ Structure + Memory Update
→ Confidence + Clarity + Tradeability
→ Verification Layer (AI)
→ Chart Persistence
→ Telegram Alert + UI Display
```

---

## Design Evolution

### Multi Agent Exploration

An earlier version of the system implemented a **multi agent advisory layer**, including:

* Structure agent
* Momentum / continuation agent
* Regime validation agent
* Risk framing agent
* Orchestrated synthesis layer

This introduced:

* parallel reasoning paths
* structured disagreement
* reconciliation logic

---

### Observed Tradeoffs

In live testing, the multi agent system introduced:

* increased latency (multiple LLM calls)
* higher operational cost
* overlapping or redundant signals
* limited improvement over deterministic baseline

---

### Final Architecture

The system was refactored into a **dual layer AI architecture**:

```
Vision → Deterministic Engine → Verification Layer
```

Where:

* LLM #1 = perception
* deterministic engine = decision authority
* LLM #2 = validation layer

---

### Result

This architecture:

* reduces latency and cost
* improves clarity of signal
* preserves interpretability
* maintains strict governance boundaries

---

## Key Design Principles

* **Deterministic > probabilistic decisions**
* **LLM = perception, not reasoning authority**
* **Validation is additive, not authoritative**
* **Stateful intraday memory**
* **No cross session bias**
* **Operator remains in control**

---

## Why This Exists

This system was built to:

> **avoid trading in low quality environments and improve execution discipline in real time**

---

## Repo Scope

* This repository is a **system showcase**
* Core architecture and pipeline are represented
* Proprietary logic is intentionally excluded:

  * prompt design
  * scoring weights
  * production thresholds

---

## Current Status

* Core pipeline operational
* Real time alerts integrated
* Streamlit dashboard active
* Verification layer deployed
* System actively used and refined

---

You’re in a *very* strong position right now.
