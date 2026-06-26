> **Superseded.** This is an archived version. The current specification is
> [QSM-ARCH v1.1.0](./QSM-ARCH-v1.1.0.md). See `CHANGELOG.md` [1.2.0] for what changed and why.

# QSM-ARCH v1.0
## Layer and Engine Operating Model
### Normative Specification for QSM Implementation Architecture

**Version:** 1.0.0  
**Status:** Final Draft — Ready for Submission  
**Maintainer:** Caitlin · Excentropy  
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)  
**DOI:** [10.5281/zenodo.20436570](https://doi.org/10.5281/zenodo.20436570)  
**Published:** 2026-06-25  
**Dependent Specs:** QSM v1.0, TSS v1.1.0

---

## Abstract

QSM-ARCH defines the operational architecture of QSM implementations. It specifies eight structural layers, the engines that operate within each layer, and five cross-cutting planes that apply across all layers. QSM-ARCH is the bridge between QSM as doctrine and QSM as a running system.

The standard is designed for personal, household, property, organizational, and community stewardship contexts. It may be implemented by humans, software, or hybrid agentic workflows governed by QSM-FAI.

---

## 1. Purpose

QSM-ARCH exists to answer: **How does a QSM implementation organize responsibility for sensing, deciding, acting, remembering, and adapting over time?**

QSM defines what to steward. THRIVE defines the Self context. TSS governs conformance and records. QSM-ARCH defines the stable operating structure — layers and engines — that any conformant implementation MUST map its capabilities onto.

---

## 2. Scope

QSM-ARCH applies to any system that:

- Claims conformance to QSM as a running stewardship system.
- Produces decisions, actions, or records within a declared context.
- Requires explicit separation between sensing, practice, memory, and adaptation.

QSM-ARCH does not prescribe a specific software stack, database, or UI. It defines normative structural responsibilities.

---

## 3. Core Principles

### 3.1 Layer separation

Each layer has a distinct job. Layers MUST NOT be collapsed when conformance is claimed at A2 or above.

### 3.2 Memory authority

The Memory layer is the authoritative record. Signal and Observation are derivative views.

### 3.3 Intent before practice

SELF context implementations MUST NOT omit the Intent layer.

### 3.4 Observation distinct from learning

Sensing what happened is distinct from updating operating assumptions based on what was learned.

### 3.5 Cross-cutting consistency

Lifecycle, ownership, provenance, metrics, and privacy properties SHOULD apply uniformly across objects.

---

## 4. Normative Terms

| Term | Definition |
|---|---|
| **Layer** | A stable domain of responsibility within a QSM implementation |
| **Engine** | A functional capability operating within a layer |
| **Plane** | A cross-cutting property dimension applied to objects across layers |
| **Derivative view** | A presentation or signal surface computed from authoritative records |
| **Authoritative record** | The canonical stored state in the Memory layer |
| **Adaptation loop** | The process by which operating assumptions are updated from observation and review |

---

## 5. The Eight Layers

Each layer is defined by purpose, primary input, primary output, and engines. See also [QSM-LAYER-MATRIX.md](QSM-LAYER-MATRIX.md) for the question mapping, cross-cutting planes, and key structural rules.

### 5.1 Intent

**Purpose:** Declares who/what this context is and what it is oriented toward.

**Primary input:** Stated values, goals, commitments, context boundaries.

**Primary output:** Mission framing, role definitions, priority ordering, horizon declaration.

**Engines:** Mission framing, role definition, boundary-setting, priority selection, horizon-setting.

**Why it matters:** Without this layer, stewardship executes against unstated purposes. For SELF, this is the "who am I trying to become" layer.

### 5.2 Governance

**Purpose:** Authority, policy, constraints, review, escalation.

**Primary input:** Values and priorities from Intent; exceptions and anomalies from Observation.

**Primary output:** Policies, approval decisions, constraint declarations, audit records.

**Engines:** Policy engine, exception engine, approval engine, rights/permissions engine, audit engine.

### 5.3 Intake

**Purpose:** Capture signals and objects from the world into the system.

**Primary input:** Raw world events (requests, alerts, arrivals, triggers).

**Primary output:** Classified, normalized, deduplicated objects ready for Memory or Practice.

**Engines:** Ingestion, triage, classification, normalization, deduplication, routing.

### 5.4 Memory

**Purpose:** Meaning, memory, models, and reference truth.

**Primary input:** Classified objects from Intake; observations from Observation; learning from Adaptation.

**Primary output:** Models, documentation, decisions, retrieved context, inferences.

**Engines:** Modeling, linking, synthesis, retrieval, decision memory, documentation stabilization.

**Note:** Documentation is a function inside Memory, not a standalone layer.

### 5.5 Practice

**Purpose:** Convert intent into outcomes.

**Primary input:** Priorities from Governance; context from Memory; tasks from Intake.

**Primary output:** Completed actions, updated states, dispatched work.

**Engines:** Planning, orchestration, workflow, automation, task dispatch, fulfillment.

### 5.6 Observation

**Purpose:** Sense what happened and what is happening.

**Primary input:** World state; Practice outputs; system telemetry.

**Primary output:** Verified states, audit trails, anomaly flags, completion records.

**Engines:** Monitoring, sensing, validation, audit trail, anomaly detection, verification.

**Important:** Observation is distinct from Adaptation. Observation is sensing; Adaptation is adapting.

### 5.7 Signal

**Purpose:** Present state and trigger appropriate attention.

**Primary input:** Observation outputs; Memory state.

**Primary output:** Summaries, alerts, status views, drill-down data, attention routing.

**Engines:** Summarization, alerting, status surfacing, drill-down, attention routing.

**Note:** Signal is derivative — the Memory layer is always the authoritative record.

### 5.8 Adaptation

**Purpose:** Adapt the system over time based on what it learned.

**Primary input:** Observation outputs; Signal patterns; retrospection inputs.

**Primary output:** Updated operating assumptions, calibrated thresholds, improvement dispatches to other layers.

**Engines:** Review, retrospection, calibration, metric analysis, pattern recognition, improvement dispatch.

**Note:** This layer closes the loop. Without it, QSM monitors but does not adapt.

---

## 6. Cross-Cutting Planes

These planes apply across all layers and all major QSM objects.

| Plane | Applies to | Required properties |
|---|---|---|
| **Lifecycle State** | All objects | `lifecycle_state` (draft / active / suspended / retired) |
| **Ownership** | All objects | `steward_ref` — identifier of responsible party |
| **Versioning / Provenance** | All records and schemas | `schema_version`, `provenance_source`, `created_at`, `modified_at` |
| **Metrics / Thresholds** | All engines and layers | `health_metric`, `alert_threshold`, `last_assessed` |
| **Security / Privacy** | All objects with personal data | `sensitivity_level`, `access_policy_ref` |

### 6.1 Lifecycle State

Every major object SHOULD declare a lifecycle state. States are: draft, active, suspended, retired.

### 6.2 Ownership

Every major object SHOULD identify a steward or responsible role via `steward_ref`.

### 6.3 Versioning / Provenance

Records and schemas SHOULD carry semantic version strings and provenance references sufficient for audit.

### 6.4 Metrics / Thresholds

Engines and layers SHOULD declare health metrics and alert thresholds where operational monitoring is expected.

### 6.5 Security / Privacy

Objects containing personal or sensitive data MUST declare a sensitivity level and access policy reference.

---

## 7. Layer Interaction Model

```text
Intent → Governance → Intake → Memory ↔ Practice
                              ↓           ↑
                         Observation → Signal
                              ↓
                      Adaptation → (all layers)
```

Adaptation dispatches improvements to Governance, Memory, Practice, and Intent as appropriate. Signal MUST NOT be treated as the system of record.

---

## 8. Conformance

A system MAY claim QSM-ARCH conformance if it satisfies the rules below.

### 8.1 Conformance levels

| Level | Label | Requirements |
|---|---|---|
| **A0** | Minimal | Implements Governance, Practice, and Observation layers |
| **A1** | Operational | Adds Intake, Memory, and Signal |
| **A2** | Complete | All 8 layers implemented |
| **A3** | Governed | All 8 layers plus all 5 cross-cutting planes formally supported |

### 8.2 Minimum conformance rules

- **ARCH-01:** A conformant implementation MUST implement at minimum the Governance, Practice, and Observation layers.
- **ARCH-02:** A conformant implementation MUST NOT collapse the Observation and Adaptation layers into one — sensing what happened is distinct from updating operating assumptions based on it.
- **ARCH-03:** A conformant implementation MUST NOT omit the Intent layer in SELF context implementations.
- **ARCH-04:** All objects in a conformant implementation SHOULD carry a `lifecycle_state` property.
- **ARCH-05:** All objects in a conformant implementation that contains personal or sensitive data MUST declare a `sensitivity_level`.
- **ARCH-06:** The Memory layer MUST be treated as the authoritative record; Signal and Observation are derivative.

---

## 9. Relationship to Other Specs

| Document | Role |
|---|---|
| **QSM v1.0** | Core ontology and stewardship model |
| **TSS v1.1.0** | Normative umbrella and audit framework |
| **THRIVE v1.1.0** | Self and wellness context layer |
| **QSM-FAI v1.0** | Fiduciary AI interface for acting within the stack |
| **QSM-ARCH v1.0** | Layer and engine operating model |

QSM-ARCH extends but does not replace references to the six-layer process stack in existing QSM documentation. The six-layer model (Governance, Dashboard, Intake, Execution, Observation, Documentation) remains valid; QSM-ARCH formalizes an eight-layer operating model that adds Intent, separates Memory from Documentation, and adds Adaptation.

---

## 10. Governance and Change Control

QSM-ARCH follows semantic versioning.

- MAJOR changes alter required layers, planes, or conformance rules.
- MINOR changes add engines, clarify layer boundaries, or extend plane properties.
- PATCH changes clarify language or fix errors.

---

## Appendix A: Layer Reference (Complete)

### Layer 1 — Intent

Job: Declares who/what this context is, what it is oriented toward, and what success looks like at the horizon.  
Inputs: Stated values, goals, commitments, context boundaries.  
Outputs: Mission framing, role definitions, priority ordering, horizon declaration.  
Engines: Mission framing engine, role definition engine, boundary-setting engine, priority selection engine, horizon-setting engine.

### Layer 2 — Governance

Job: Authority, policy, constraints, review cadence, escalation paths.  
Inputs: Values and priorities from Intent; exceptions and anomalies from Observation.  
Outputs: Policies, approval decisions, constraint declarations, audit records.  
Engines: Policy engine, exception engine, approval engine, rights/permissions engine, audit engine.

### Layer 3 — Intake

Job: Capture signals, requests, and objects from the world and route them into the system.  
Inputs: Raw world events (requests, alerts, arrivals, triggers).  
Outputs: Classified, normalized, deduplicated objects ready for Memory or Practice.  
Engines: Ingestion engine, triage engine, classification engine, normalization engine, deduplication engine, routing engine.

### Layer 4 — Memory

Job: Meaning, memory, models, and reference truth.  
Inputs: Classified objects from Intake; observations from Observation; learning from Adaptation.  
Outputs: Models, documentation, decisions, retrieved context, inferences.  
Engines: Modeling engine, linking engine, synthesis engine, retrieval engine, decision memory engine, documentation stabilization engine.

### Layer 5 — Practice

Job: Convert intent into outcomes.  
Inputs: Priorities from Governance; context from Memory; tasks from Intake.  
Outputs: Completed actions, updated states, dispatched work.  
Engines: Planning engine, orchestration engine, workflow engine, automation engine, task dispatch engine, fulfillment engine.

### Layer 6 — Observation

Job: Sense what happened and what is currently happening.  
Inputs: World state; Practice outputs; system telemetry.  
Outputs: Verified states, audit trails, anomaly flags, completion records.  
Engines: Monitoring engine, sensing engine, validation engine, audit trail engine, anomaly detection engine, verification engine.

### Layer 7 — Signal

Job: Present state and trigger appropriate attention.  
Inputs: Observation outputs; Memory state.  
Outputs: Summaries, alerts, status views, drill-down data, attention routing.  
Engines: Summarization engine, alerting engine, status surfacing engine, drill-down engine, attention routing engine.

### Layer 8 — Adaptation

Job: Adapt the system over time based on what it learned.  
Inputs: Observation outputs; Signal patterns; retrospection inputs.  
Outputs: Updated operating assumptions, calibrated thresholds, improvement dispatches to other layers.  
Engines: Review engine, retrospection engine, calibration engine, metric analysis engine, pattern recognition engine, improvement dispatch engine.

---

## Appendix B: Ontology Crosswalk

QSM ontology v3.0 maps architectural layers to `qsm:ArchitecturalLayer` individuals (`qsm:arch_layer_*`). Cross-cutting plane properties include `qsm:lifecycle_state`, `qsm:steward_ref`, `qsm:schema_version`, and `qsm:provenance_source`. See `Ontology/qsm-ontology-v3.ttl`.

---

## Appendix C: Conformance Statement Template

> This implementation conforms to QSM-ARCH v1.0 at level A2 for the SELF context. It implements all eight layers, treats Memory as authoritative, separates Observation from Adaptation, and includes Intent for personal stewardship.

*QSM-ARCH v1.0 — Layer and Engine Operating Model*  
*© 2026 Excentropy — CC BY 4.0*  
*First published: 2026-06-25*
