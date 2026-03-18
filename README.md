## XSP Trading Copilot

**A real-time AI market state engine that interprets price action using vision, memory, and deterministic logic.**

---

### What This Is

XSP Trading Copilot is a **governance-first AI system** designed to:

* interpret intraday market structure
* maintain session level state
* classify market regimes deterministically
* deliver structured, real-time decision context


This system acts as a **decision support layer** for discretionary execution.

---

### Core Architecture

The system is built around a strict separation of concerns:

#### Perception Layer (AI Vision)

* Ingests TradingView SPY chart screenshots
* Extracts structured market state using OpenAI vision models
* **LLM is perception only, never decision authority**

---

#### State & Memory Layer

* Tracks intraday structure:

  * OH / OL interactions
  * break attempts
  * failed moves
  * returns to range
* Maintains **session-only memory**
* No cross day bias

---

#### Decision Engine (Deterministic)

* Classifies market regimes using ordered rule logic
* Independent of the LLM
* Produces:

  * regime classification
  * directional bias
  * invalidation levels

---

#### Evaluation Layer

* Confidence scoring (directional conviction)
* Setup clarity scoring (visual cleanliness)
* Structure aware interpretation

---

#### Output Layer

* Telegram alerts (real-time)
* Streamlit dashboard (interactive analysis)
* SQLite snapshots (session history)

---

### End-to-End Flow

```
Chart Screenshot
→ Vision Extraction (AI)
→ Schema Validation
→ Market State Normalization
→ Regime Classification (Deterministic)
→ Structure + Memory Update
→ Confidence + Clarity Scoring
→ Snapshot Persistence
→ Telegram Alert + UI Display
```

---

### Key Design Principles

* **Deterministic > probabilistic decisions**
* **LLM = perception, not reasoning authority**
* **Stateful intraday memory**
* **No cross session bias**
* **Operator remains in control**

---

### Why This Exists

This system was built to keep me from trading in non optimal environments.
---

### Notes

* Proprietary logic (prompt design, scoring logic, rule weighting) is intentionally not included
* This repository is a **system showcase**, not a production trading engine

---

### Repo Status

* Actively evolving
* Core pipeline operational
* Dashboard + alerting integrated
* Further enhancements in progress

---


You’re in a very strong position right now.
