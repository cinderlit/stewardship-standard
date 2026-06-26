# QSM-ARCH v1.1
## Layer and Engine Operating Model
### Normative Specification for QSM Implementation Architecture

**Version:** 1.1.0  
**Status:** Final Draft — Ready for Submission  
**Maintainer:** Caitlin · Excentropy  
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)  
**DOI:** [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569)  
**Published:** 2026-06-25  
**Changelog (1.1.0):** Added context lifecycle (§6.6) and conformance-scale reconciliation with QSM/TSS (§8.3).  
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

Memory is the authoritative record for **persistent, intentional knowledge** — models, decisions, documentation, and curated understanding. It is NOT the authoritative home for ephemeral operational state, transient telemetry, or derived caches. Ephemeral state lives in Observation; derived views live in Signal. An object is promoted to Memory by a deliberate act — logging, documentation, or decision recording — not automatically.

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

Each layer is defined by a per-layer contract: definition, primary input, primary output, engines, what it owns, what it must never own, what it delegates to, required artifacts, allowed and prohibited dependencies, and anti-patterns. The "must never own" and "prohibited dependencies" fields are the boundary tests that keep layers from collapsing into one another. See also [QSM-LAYER-MATRIX.md](QSM-LAYER-MATRIX.md) for the question mapping, cross-cutting planes, and key structural rules.

### 5.1 Intent

**Definition:** Declares who/what this context is and what it is oriented toward.

**Primary input:** Stated values, goals, commitments, context boundaries.

**Primary output:** Mission framing, role definitions, priority ordering, horizon declaration.

**Engines:** Mission framing, role definition, boundary-setting, priority selection, horizon-setting.

**Owns:** Purpose and orientation, declared values, role definitions, priority ordering, horizon declaration, the context's boundary.

**Must never own:** Policies and constraints (Governance), execution of work (Practice), records of what happened (Memory and Observation).

**Delegates to:** Governance, which turns orientation into policy and constraint.

**Required artifacts:** Orientation/purpose statement, named values, role definitions, priority ordering, declared horizon.

**Allowed dependencies:** Originating layer — requires no upstream input; MAY receive improvement dispatches from Adaptation.

**Prohibited dependencies:** MUST NOT take operational direction from Practice, Signal, or Intake.

**Anti-patterns:** Becoming a goals list or task backlog rather than an orientation statement.

**Why it matters:** Without this layer, stewardship executes against unstated purposes. For SELF, this is the "who am I trying to become" layer.

### 5.2 Governance

**Definition:** Defines authority, policy, constraints, review cadence, and escalation paths.

**Primary input:** Values and priorities from Intent; exceptions and anomalies from Observation.

**Primary output:** Policies, approval decisions, constraint declarations, audit records.

**Engines:** Policy engine, exception engine, approval engine, rights/permissions engine, audit engine.

**Owns:** Policy, approvals, constraints, rights/permissions, review cadence, audit authority, and authorization of context state transitions.

**Must never own:** The purpose it serves (Intent), the work itself (Practice), the authoritative knowledge record (Memory).

**Delegates to:** Intake and Practice, which operate within its policies.

**Required artifacts:** Policy set, approval/decision records, constraint declarations, escalation paths, audit records.

**Allowed dependencies:** Intent (values and priorities); Observation (exceptions and anomalies); Adaptation (policy updates).

**Prohibited dependencies:** MUST NOT derive policy from Signal summaries alone.

**Anti-patterns:** Writing policy without consulting Intent (governance without declared purpose).

### 5.3 Intake

**Definition:** Captures signals and objects from the world and routes them into the system in normalized, classified form.

**Primary input:** Raw world events (requests, alerts, arrivals, triggers).

**Primary output:** Classified, normalized, deduplicated objects ready for Memory or Practice.

**Engines:** Ingestion, triage, classification, normalization, deduplication, routing.

**Owns:** Ingestion, triage, classification, normalization, deduplication, and routing of arriving objects.

**Must never own:** Long-term storage of objects (Memory), execution of the work (Practice), policy decisions (Governance).

**Delegates to:** Memory for persistence and Practice for action, per routing.

**Required artifacts:** Classification scheme, normalization rules, routing map, deduplication log.

**Allowed dependencies:** Governance (routing policy); Intent (triage priority).

**Prohibited dependencies:** MUST NOT depend on Signal or Adaptation for routing decisions.

**Anti-patterns:** Retaining objects permanently (Intake becoming storage instead of routing).

### 5.4 Memory

**Definition:** Holds meaning, models, decisions, and reference truth — the authoritative record for persistent, intentional knowledge.

**Primary input:** Classified objects from Intake; observations from Observation; learning from Adaptation.

**Primary output:** Models, documentation, decisions, retrieved context, inferences.

**Engines:** Modeling, linking, synthesis, retrieval, decision memory, documentation stabilization.

**Owns:** Models, decisions, documentation, curated understanding, and the authoritative record of persistent, intentional knowledge.

**Must never own:** Ephemeral operational state and transient telemetry (which live in Observation until deliberately promoted), and derived views or caches (which live in Signal).

**Delegates to:** Practice and Signal, which consume Memory; supplies retrieved context on request.

**Required artifacts:** Models, decision records, documentation, provenance and versioning metadata.

**Allowed dependencies:** Intake (classified objects); Observation (promoted findings); Adaptation (updated knowledge).

**Prohibited dependencies:** MUST NOT treat Signal output as a source of authoritative truth.

**Anti-patterns:** Claiming ephemeral operational state and transient telemetry as authoritative records — Memory is the authoritative record for *persistent, intentional* knowledge only; ephemeral state lives in Observation until deliberately promoted.

**Note:** Documentation is a function inside Memory, not a standalone layer. Memory is the authoritative home for persistent, intentional knowledge — models, decisions, documentation, and curated understanding. It is NOT the authoritative home for ephemeral operational state, transient telemetry, or derived caches. Ephemeral state lives in Observation; derived views live in Signal. An object is promoted to Memory by a deliberate act — logging, documentation, or decision recording — not automatically.

### 5.5 Practice

**Definition:** Converts intent into outcomes — the sustained work of stewardship.

**Primary input:** Priorities from Governance; context from Memory; tasks from Intake.

**Primary output:** Completed actions, updated states, dispatched work.

**Engines:** Planning, orchestration, workflow, automation, task dispatch, fulfillment.

**Owns:** Planning, orchestration, workflow, automation, task dispatch, fulfillment, and completed actions.

**Must never own:** Its own governing priorities (Governance/Intent), the authoritative record (Memory), policy (Governance).

**Delegates to:** Observation, which senses the results of its work.

**Required artifacts:** Plans, dispatched-work records, completion outputs, updated states.

**Allowed dependencies:** Governance (priorities); Memory (context); Intake (tasks).

**Prohibited dependencies:** MUST NOT generate its own governing priorities independent of Governance or Intent.

**Anti-patterns:** Generating its own priorities without grounding them in Governance or Intent (runaway execution).

### 5.6 Observation

**Definition:** Senses what happened and what is happening — current state, completion, anomalies, verified conditions.

**Primary input:** World state; Practice outputs; system telemetry.

**Primary output:** Verified states, audit trails, anomaly flags, completion records.

**Engines:** Monitoring, sensing, validation, audit trail, anomaly detection, verification.

**Owns:** Monitoring, sensing, validation, audit trails, anomaly flags, and ephemeral operational state.

**Must never own:** Decisions or actions based on what it senses (Practice/Governance), and the authoritative knowledge record (Memory, until deliberate promotion).

**Delegates to:** Signal for surfacing and Governance for exceptions; promotes deliberate findings to Memory.

**Required artifacts:** Verified state records, audit trails, anomaly flags, completion records.

**Allowed dependencies:** World state; Practice outputs; system telemetry.

**Prohibited dependencies:** MUST NOT take direction from Signal.

**Anti-patterns:** Making decisions based on what it senses (Observation becoming decision-making).

**Important:** Observation is distinct from Adaptation. Observation is sensing; Adaptation is adapting.

### 5.7 Signal

**Definition:** Presents current state and routes attention to what matters.

**Primary input:** Observation outputs; Memory state.

**Primary output:** Summaries, alerts, status views, drill-down data, attention routing.

**Engines:** Summarization, alerting, status surfacing, drill-down, attention routing.

**Owns:** Summarization, alerting, status surfacing, drill-down, attention routing, and derived views.

**Must never own:** The authoritative record (always Memory and Observation), and decisions or policy.

**Delegates to:** Human or agent stewards (attention), and back into Governance and Practice as triggers.

**Required artifacts:** Summaries, alerts, status views, drill-down surfaces.

**Allowed dependencies:** Observation outputs; Memory state.

**Prohibited dependencies:** MUST NOT be consumed authoritatively by Memory.

**Anti-patterns:** Becoming the record of truth — Signal is always derivative of Memory and Observation.

**Note:** Signal is derivative — the Memory layer is always the authoritative record.

### 5.8 Adaptation

**Definition:** Adapts how the system operates over time based on what it learned.

**Primary input:** Observation outputs; Signal patterns; retrospection inputs.

**Primary output:** Updated operating assumptions, calibrated thresholds, improvement dispatches to other layers.

**Engines:** Review, retrospection, calibration, metric analysis, pattern recognition, improvement dispatch.

**Owns:** Review, retrospection, calibration, metric analysis, pattern recognition, and improvement dispatch.

**Must never own:** Direct, undocumented mutation of records or policy — changes must be governed and recorded.

**Delegates to:** Intent, Governance, Memory, Practice, and Observation, via improvement dispatches.

**Required artifacts:** Review records, calibrated thresholds, improvement dispatches with provenance.

**Allowed dependencies:** Observation outputs; Signal patterns; retrospection inputs.

**Prohibited dependencies:** MUST NOT bypass Governance to enact changes.

**Anti-patterns:** Making undocumented or ungoverned changes to the system (Adaptation becoming undocumented churn).

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

### 6.6 Context Lifecycle

Context-level lifecycle extends the object-level `lifecycle_state` plane to the bounded stewardship domain itself. A context uses the same four states: **draft**, **active**, **suspended**, and **retired**.

| State | Meaning |
|---|---|
| **draft** | Context is being defined; not yet operational. Objects may be created but Practice SHOULD NOT dispatch against them. |
| **active** | Context is operational. All layers function according to declared scope. |
| **suspended** | Context is temporarily paused. Memory objects are retained and frozen (read-only); Practice MUST NOT dispatch new work; Signal MAY surface status only. |
| **retired** | Context is closed. Memory objects are preserved as archival record; Practice and Signal cease; Observation stops. |

**Transition triggers and authorization:**

- Transitions from **draft → active** SHOULD be authorized by Governance, informed by Intent (declared scope and steward are complete).
- Transitions to **suspended** SHOULD be authorized by Governance (e.g., steward absence, capacity overload, seasonal pause).
- Transitions to **retired** MUST be authorized by Governance and SHOULD be informed by Intent (the context's purpose has ended or been superseded).
- Transitions from **suspended → active** SHOULD be authorized by Governance after review.

**Object disposition on context state change:**

- On **suspend:** Memory objects are retained unchanged but frozen. No new Practice dispatches. Existing Observation MAY continue for monitoring only.
- On **retire:** Memory objects MUST be preserved as archival record and MUST NOT be deleted. <!-- REVIEW: whether retired contexts allow read-only Signal access for historical review --> Practice and Signal cease. Observation stops except for archival integrity checks.

Retiring a SELF context means the person's stewardship model for that bounded domain is closed — records are preserved for audit and reflection, but the context no longer accepts new stewardship activity.

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
- **ARCH-07:** A context MUST NOT be retired without preserving its Memory records as archival record.
- **ARCH-08:** Context state transitions MUST be recorded in Memory with provenance (who authorized, when, and rationale).

### 8.3 Relationship to QSM and TSS conformance

QSM-ARCH A-levels (A0–A3) and QSM C-levels / TSS T-levels / THRIVE H-levels / QSM-FAI L-levels measure **different things** and are **independent scales**.

| Scale | What it measures |
|---|---|
| **A-level** (QSM-ARCH) | Architectural completeness — how many layers and cross-cutting planes are implemented |
| **C/T/H/L-level** (QSM, TSS, THRIVE, QSM-FAI) | Spec and object conformance — whether required concepts, structures, and rules are satisfied |

An implementation MAY claim any combination (e.g., C2 + A1 is coherent: strong object conformance with partial architectural coverage). Implementations SHOULD aim for aligned levels where practical — an A2 implementation with C0 would be unusual but not contradictory.

For the C/T/H/L alignment ladder, see TSS Appendix Z. A-levels are a separate architectural axis and are not part of the T-level audit standard.

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
