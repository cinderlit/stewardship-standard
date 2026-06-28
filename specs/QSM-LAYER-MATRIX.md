# QSM — Layer Matrix
**Part of:** QSM-ARCH v1.0  
**Updated:** 2026-06-25

Layer names: Intent · Governance · Intake · Memory · Practice · Observation · Signal · Adaptation  
Questions: Q1 = purpose · Q2 = awareness · Q3 = action and improvement

---

## The eight layers

| # | Layer | Q | Purpose | Inputs | Outputs | Engines |
|---|---|---|---|---|---|---|
| 1 | **Intent** | Q1 | Declares what the context is for, what it values, and what orients its decisions and priorities. | Values, commitments, scope, horizon | Purpose statement, priority ordering, role definitions | Mission framing · Role definition · Boundary-setting · Priority selection · Horizon-setting |
| 2 | **Governance** | Q1 | Authority, policy, constraints, review cadence, and escalation paths. Who can decide what and under what conditions. | Intent declarations; exceptions from Observation | Policies, approvals, constraints, audit records | Policy · Exception handling · Approval · Rights/permissions · Audit |
| 3 | **Intake** | Q2 | Captures signals and objects arriving from the world and routes them into the system in a usable form. | Raw events, requests, alerts, arrivals | Classified, normalized objects ready for Memory or Practice | Ingestion · Triage · Classification · Normalization · Deduplication · Routing |
| 4 | **Memory** | Q3 | Holds what the system knows — meaning, models, decisions, and documentation. The authoritative record. Everything else is derivative of Memory. | Objects from Intake; findings from Observation; updates from Adaptation | Models, documentation, decisions, retrieved context | Modeling · Linking · Synthesis · Retrieval · Decision memory · Documentation |
| 5 | **Practice** | Q3 | The sustained work of stewardship — routines, tasks, decisions, and interventions that keep the context functioning. | Priorities from Governance; context from Memory; tasks from Intake | Completed actions, updated states, dispatched work | Planning · Orchestration · Workflow · Automation · Task dispatch · Fulfillment |
| 6 | **Observation** | Q2 | Senses what is happening and what happened — current state, completion, anomalies, and verified conditions. | World state, Practice outputs, system telemetry | Verified states, audit trails, anomaly flags, completion records | Monitoring · Sensing · Validation · Audit trail · Anomaly detection · Verification |
| 7 | **Signal** | Q2 | Surfaces current state and routes attention to what matters. Derivative of Memory and Observation — never the authoritative record. | Observation outputs; Memory state | Summaries, alerts, status views, attention routing | Summarization · Alerting · Status surfacing · Drill-down · Attention routing |
| 8 | **Adaptation** | Q3 | Changes how the system operates based on what it experienced. Closes the loop between Observation and improved Practice. A system without Adaptation monitors but never improves. | Observation outputs; Signal patterns; retrospection inputs | Updated operating assumptions, calibrated thresholds, improvement dispatches to other layers | Review · Retrospection · Calibration · Metric analysis · Pattern recognition · Improvement dispatch |

---

## Question mapping

| Question | Layers |
|---|---|
| **Q1 — What is this for and what does it care about?** | Intent · Governance |
| **Q2 — What is happening and what needs attention?** | Intake · Observation · Signal |
| **Q3 — What are we doing about it and are we getting better?** | Memory · Practice · Adaptation |

---

## Cross-cutting planes

These five properties apply to every object across all layers, regardless of context type.

| Plane | Required properties |
|---|---|
| **Lifecycle State** | `lifecycle_state` — draft / active / suspended / retired |
| **Ownership** | `steward_ref` — identifier of the responsible party |
| **Versioning / Provenance** | `schema_version` · `provenance_source` · `created_at` · `modified_at` |
| **Metrics / Thresholds** | `health_metric` · `alert_threshold` · `last_assessed` |
| **Security / Privacy** | `sensitivity_level` · `access_policy_ref` |

---

## Key rules

- **Memory is the authoritative record.** Signal and Observation are derivative — they surface and sense what Memory holds, but they do not replace it. Memory is the authoritative record for **persistent, intentional knowledge** — models, decisions, documentation, and curated understanding. It is NOT the authoritative home for ephemeral operational state, transient telemetry, or derived caches. Ephemeral state lives in Observation; derived views live in Signal. An object is promoted to Memory by a deliberate act — logging, documentation, or decision recording — not automatically.
- **Observation and Adaptation are distinct.** Observation senses what happened. Adaptation changes how the system operates because of it. Collapsing them produces a system that monitors but does not improve.
- **Documentation lives inside Memory.** It is a stabilization function — the way things get persisted so Memory can hold them — not a peer layer.
- **Intent should precede Governance.** Conformant implementations SHOULD establish Intent before formalizing Governance. Governance without declared purpose tends to produce constraint without direction — rules that restrict without orienting. In practice, Intent and Governance may co-evolve; what this rule prohibits is a governance layer that has no declared Intent to ground itself in.
- **Adaptation dispatches improvements to other layers.** Its outputs are not just records — they are instructions that update policies (Governance), operating models (Practice), thresholds (Observation), and knowledge (Memory).

---

*QSM Layer Matrix — © 2026 Caitlin Stokes / Cinderlit · CC BY 4.0*
