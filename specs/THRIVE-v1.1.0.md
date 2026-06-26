# THRIVE v1.1.0
## Self and Wellness Context Layer
### Normative Specification for Personal Stewardship, Capacity, and Wellbeing

**Version:** 1.1.0
**Status:** Final Draft — Ready for Submission
**Author:** Caitlin Stokes
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)
**DOI:** [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569)
**Published:** 2026-05-28
**Amended:** 2026-06-22 (v1.1.0 — see `CHANGELOG.md`)
**Dependent Specs:** QSM v1.1.0, TSS v1.2.0, QSM-FAI v1.1.0

---

## Abstract

THRIVE defines the Self and wellness context layer within the stewardship stack. It provides a
normative structure for representing personal capacity, needs, constraints, habits,
obligations, recovery, and support in a way that is compatible with QSM and governed by
TSS. THRIVE is intended to make the self legible as a stewardship domain without reducing
wellbeing to a simplistic productivity metric.

The standard is designed for personal, caregiver, and hybrid human-agent use. It can be
implemented as a standalone Self context or as the foundation for broader household and
organizational stewardship systems.

---

## Status of This Document

This document is a living technical specification within The Stewardship Standard
stack. It is an openly accessible reference for implementers and practitioners and
may evolve over time through public feedback and practical experience. Changes are
recorded in the public change history (`CHANGELOG.md`) and tracked through public
issues in the canonical repository; the latest editor's draft there is authoritative.

**v1.1.0 amendment note:** this revision cross-references QSM §4.2.1's needs-framework
mechanism from THRIVE's Capacity and Load Model (§7.1), so the two specs do not silently
diverge on which needs-tiering vocabulary a SELF context actually uses. The change is
additive and informative; no v1.0.1 requirement was removed or tightened. See `CHANGELOG.md`
[1.1.0] for the full amendment record and implementation evidence.

## Use of AI-Assisted Tools in the Development of This Specification

This specification was conceived, directed, and is maintained by its named human
author, who defined the problem space, the core constructs, the domain ontology, and
the design intent, and who retains full responsibility and accountability for all
content — both normative and non-normative.

AI-assisted tools (large language models) were used substantially, and under direct
human supervision, throughout development: to draft and structure specification text
(including normative requirements and reference schemas), to explore alternative
framings, to refine terminology, and to check internal consistency. The author
reviewed, corrected, validated, or rejected all AI-generated material. AI tools were
not treated as authors and do not bear responsibility for the work; they were not
relied upon as sources of empirical or factual claims; and any citations were
verified by the author rather than accepted as generated.

The conceptual framework, its claims of novelty, and its design decisions are the
author's own and can be articulated and defended independently of the tools used to
express them.

## Openness and Governance

This specification is published as an open standard: it is publicly accessible, may be
implemented by anyone without discrimination or royalty, and is intended to support
interoperability across tools and contexts.

- **License.** Specification text is licensed under the Creative Commons Attribution
  4.0 International License (CC BY 4.0); reference schemas are licensed under the
  Apache License 2.0. Attribution is required; both commercial and non-commercial
  reuse are permitted. See `LICENSE-SPEC` and `LICENSE-SCHEMAS`.
- **Governance.** The standard is maintained by Cinderlit, with
  Excentropy as official implementation partner. Proposed changes are raised and
  reviewed publicly via the issue tracker at
  `github.com/cinderlit/stewardship-standard`, documented in the change history, and
  ratified by maintainer review on a quarterly cycle. Substantive amendments are
  accompanied by example data and at least one use case. See `GOVERNANCE.md` and
  `CONTRIBUTING.md` for the full process.

---

## 1. Purpose

THRIVE exists to answer a simple question: **What does this person need in order to function,
recover, and flourish within their current context?**

It organizes the Self as a stewardship domain with explicit capacities, limits, supports, and
responsibilities. The goal is clarity, not surveillance.

---

## 2. Scope

THRIVE applies to contexts where a steward is also the primary subject of stewardship. This
includes:

- Personal executive function.
- Health and wellness planning.
- Habit and routine support.
- Recovery from overload or disruption.
- Care coordination for oneself while also supporting others.

THRIVE does not define medical diagnosis, clinical treatment, or therapeutic practice. It may
reference those domains, but it does not replace them.

---

## 3. Core Principles

### 3.1 Dignity

The Self MUST be represented as a person, not a metric.

### 3.2 Capacity awareness

A conformant implementation SHOULD track effort, bandwidth, and recovery needs explicitly.

### 3.3 Non-punitive design

The model MUST not shame, moralize, or penalize the user for unmet needs or degraded capacity.

### 3.4 Context sensitivity

What counts as support depends on the current life context, not just abstract goals.

### 3.5 Reciprocity with the stack

THRIVE SHOULD interoperate with QSM, TSS, and QSM-FAI without losing the human center.

---

## 4. Normative Terms

| Term | Definition |
|---|---|
| **Self** | The person whose capacity, wellbeing, and responsibilities are being represented |
| **Capacity** | The amount of effective effort, attention, or resilience available at a given time |
| **Need** | A condition required to sustain wellbeing, functioning, or recovery |
| **Constraint** | A limit on time, energy, access, money, health, or attention |
| **Support** | A person, tool, routine, or resource that reduces friction or increases capacity |
| **Load** | The total burden of obligations, tasks, and emotional or cognitive demand |
| **Recovery** | The process of restoring capacity after depletion |
| **Routine** | A recurring structure that stabilizes functioning |
| **Override** | A deliberate departure from the default routine due to changing conditions |

---

## 5. Required Objects

A conformant THRIVE implementation MUST support, at minimum, the following objects:

- SelfContext
- CapacityProfile
- Need
- Constraint
- Support
- Routine
- Load
- RecoveryPlan
- WellnessRecord
- ScenarioPattern

### 5.1 Minimal object requirements

Each object SHOULD include:
- A unique identifier.
- A label.
- A status or state.
- A timestamp or effective date where relevant.
- A provenance reference where relevant.

---

## 6. SelfContext Declaration

A THRIVE implementation MUST begin with an explicit SelfContext declaration.

### 6.1 Required fields

- Context identifier.
- Person identifier or alias.
- Effective date.
- Declared scope.
- Capacity baseline.
- Known constraints.
- Support network, if any.
- Review cadence.

### 6.2 Example context types

- SELF
- RECOVERY
- TRANSITION
- CAREGIVING
- OVERLOAD

These types MAY be used individually or in combination.

### 6.3 World Domain Scope

A THRIVE implementation SHOULD declare which world domains the SelfContext is actively stewarding.

**World domains:**
- **Physical** — body, space, material environment, sensory experience, movement, health, sleep, nutrition.
- **Digital** — online presence, data assets, digital tools, attention management, notification load, digital identity, information diet, privacy, digital obligations, and digital relationships.
- **Metaphysical** — meaning, values, spiritual practice, psychological interior, purpose, and the relationship to uncertainty and growth.

A person exists simultaneously in all three domains. A conformant implementation SHOULD at minimum declare which domains are actively being stewarded and at what intensity. Domains that are not actively stewarded SHOULD be noted as out of scope rather than omitted silently.

**WorldDomainScope required fields:**
- Domain identifier (physical / digital / metaphysical).
- Active stewardship status (active / passive / out-of-scope).
- Known constraints or risks in this domain, if any.

The digital domain is frequently omitted in personal stewardship models. This is a structural gap. A conformant THRIVE implementation SHOULD treat digital stewardship as a first-class domain with its own capacity costs (attention is the primary resource), hygiene requirements (data, security, information diet), and management categories.

### 6.4 Identity and Intent Profile

A THRIVE implementation SHOULD include an explicit IdentityIntentProfile that orients all other stewardship decisions.

**Purpose:** Without an articulated orientation, stewardship becomes task execution against unstated purposes. The IdentityIntentProfile is not a goals list — it is the answer to "who is this person trying to become and what values orient their choices."

**Required fields:**
- Declared orientation or purpose statement (free text, updated on review).
- Core values list (≥2, ≤7 named values).
- Horizon scope (the timeframe the orientation addresses: seasonal / annual / multi-year).
- Last reviewed date.

**Rules:**
- The IdentityIntentProfile MUST NOT be a productivity target or output metric.
- It SHOULD be expressed in terms of being and becoming, not doing and achieving.
- It MUST be treated as a living document, reviewed at the cadence declared in the SelfContext.
- All major stewardship decisions SHOULD be legible against the IdentityIntentProfile.

### 6.5 Developmental Context

A THRIVE implementation MAY declare a developmental context that modifies how needs and satisfiers are interpreted.

**Purpose:** Stage models (psychosocial stages, life stages, role stages) act as modifiers on needs assessment. The fundamental needs do not change by developmental stage, but what counts as an appropriate satisfier, what the competence thresholds look like, and what is salient in the current period all shift.

**DevelopmentalContext fields:**
- Declared life stage (free text or using a named stage framework).
- Stage framework used (optional — e.g., Erikson psychosocial stages, Kegan constructive development, or a custom model).
- Current developmental focus or tension (free text).
- Effective date of last stage review.

**Rules:**
- Implementations MUST NOT use developmental stage to rank needs as more or less important — stage modifies satisfiers, not needs.
- Implementations SHOULD review developmental context at major life transitions.
- QSM-FAI MUST treat DevelopmentalContext declarations as protected context inputs.

### 6.6 Temporal Cycle Profile

A THRIVE implementation SHOULD declare known temporal cycles that affect capacity baseline.

**Purpose:** Biological and time-based cycles (circadian rhythm, hormonal cycles, seasonal affect, recovery cycles from illness or overload) affect **capacity**, not needs. They belong in the CapacityProfile and Routine modeling, providing the rhythmic substrate that governs when capacity peaks, when it troughs, and what triggers recovery.

**TemporalCycleProfile fields:**
- Cycle identifier and label.
- Cycle type (circadian / hormonal / seasonal / illness-recovery / life-stage / other).
- Approximate period (hours / days / weeks / months / years).
- Capacity effect (modifier on baseline capacity during this phase).
- Known high-capacity phases and low-capacity phases.

**Rules:**
- Temporal cycles MUST inform CapacityProfile baselines and Routine trigger conditions.
- Low-capacity phases MUST trigger reduced-friction defaults, not increased demands.
- Cycle data MUST NOT be used punitively or to assign blame for reduced output.

---

## 7. Capacity and Load Model

THRIVE is centered on the relationship between capacity and load.

### 7.1 Capacity dimensions

A conformant implementation SHOULD be able to represent:
- Cognitive capacity.
- Emotional capacity.
- Physical capacity.
- Social capacity.
- Administrative capacity.
- Recovery capacity.

#### 7.1.1 Relationship to QSM needs frameworks *(added v1.1.0)*

THRIVE deliberately does not prescribe a needs-tiering theory of its own — see QSM §4.2.1,
which names the needs frameworks (Max-Neef, ERG, Pink, WELL) that QSM-conformant implementations
commonly select per context type, and notes that SELF contexts most often use Max-Neef's
fundamental human needs. Where a THRIVE SelfContext is also a QSM Context (per §13), the capacity dimensions
above SHOULD be interpretable against that Context's declared `needs_framework` rather than
introducing a second, parallel tiering scheme. For example, under Max-Neef, Physical capacity
maps most directly to Subsistence and Protection needs, Social capacity to Affection and Participation, and Recovery
capacity supports whichever need is currently under strain. This is guidance for consistency
across the stack, not a new conformance requirement: THRIVE-02 (below) is satisfied by
representing capacity and load at all, regardless of whether a framework mapping is declared.

### 7.2 Load dimensions

A conformant implementation SHOULD be able to represent:
- Required tasks.
- Interruptions.
- Care obligations.
- Decision burden.
- Hidden maintenance work.
- Context switching.

### 7.3 Load rule

If load persistently exceeds capacity, the system SHOULD surface an overload condition and
recommend structural reduction, support addition, or scope renegotiation.

---

## 8. Routine Modeling

THRIVE supports recurring routines as a first-class structure.

### 8.1 Routine types

- Morning.
- Evening.
- Recovery.
- Workday transition.
- Medication or health support.
- Caregiving support.
- Weekly reset.

### 8.2 Routine rules

A routine SHOULD specify:
- Trigger conditions.
- Steps or phases.
- Expected duration.
- Known failure modes.
- Recovery or fallback options.

Routines MAY be overridden when the context changes, but overrides SHOULD be recorded.

---

## 9. Scenario Patterns

THRIVE includes scenario patterns that recur in the Self context.

### 9.1 Example patterns

- Burnout recovery.
- Executive dysfunction day.
- High-demand work week.
- Family caregiving week.
- Illness or injury.
- Travel or disruption.

### 9.2 Pattern rules

Scenario patterns SHOULD:
- Identify capacity changes.
- Alter expectations or defaults.
- Suggest reduced-friction actions.
- Record recovery needs after the event.

---

## 10. Records and Reflection

A conformant THRIVE implementation MUST maintain records of meaningful changes to self-context.

### 10.1 Record types

- Capacity update.
- Need change.
- Constraint change.
- Routine change.
- Support change.
- Load spike.
- Recovery event.
- Reflection or review.

### 10.2 Record rules

- Records MUST be timestamped.
- Records SHOULD be understandable to the user.
- Records MUST support retrospective review.
- Records MUST NOT imply blame.

---

## 11. Machine-Readable Schemas

THRIVE MAY be implemented with JSON, YAML, or graph schemas.
A conformant implementation SHOULD provide schemas for the following objects:

1. SelfContext schema.
2. CapacityProfile schema.
3. Need schema.
4. Routine schema.
5. WellnessRecord schema.

### 11.1 Reference schema set

```text
schemas/
├── self-context.schema.json
├── capacity-profile.schema.json
├── need.schema.json
├── routine.schema.json
└── wellness-record.schema.json
```

---

## 12. Conformance

A system MAY claim conformance if it satisfies the following.

### 12.1 Conformance levels

| Level | Label | Description |
|---|---|---|
| **H0** | Descriptive | Informal self model or journal |
| **H1** | Structured | Uses explicit capacity, need, and routine objects |
| **H2** | Supportive | Maintains records and pattern support |
| **H3** | Normative | Fully supports SelfContext declarations, load/capacity modeling, and review loops |
| **H4** | Integrated | Fully supports all of H3 plus WorldDomainScope, IdentityIntentProfile, DevelopmentalContext, and TemporalCycleProfile |

### 12.2 Minimum conformance rules

- **THRIVE-01:** A conformant implementation MUST declare a SelfContext.
- **THRIVE-02:** A conformant implementation MUST represent capacity and load.
- **THRIVE-03:** A conformant implementation MUST support records and reflection.
- **THRIVE-04:** A conformant implementation MUST preserve dignity and avoid punitive framing.
- **THRIVE-05:** A conformant implementation SHOULD support routines and recovery planning.
- **THRIVE-06:** A conformant implementation SHOULD declare WorldDomainScope for at least the physical domain.
- **THRIVE-07:** A conformant implementation SHOULD include an IdentityIntentProfile.
- **THRIVE-08:** A conformant implementation using the SELF context SHOULD use Max-Neef's fundamental human needs as the needs framework.

---

## 13. Relationship to Other Specs

| Document | Role |
|---|---|
| **QSM v1.1.0** | Core ontology and stewardship model |
| **TSS v1.2.0** | Normative umbrella and audit framework |
| **THRIVE v1.1.0** | Self and wellness context layer |
| **QSM-FAI v1.1.0** | Fiduciary AI interface for acting within the stack |

THRIVE MAY serve as the SELF context type within QSM.
THRIVE MUST be governed by the conformance and record rules of TSS.
QSM-FAI MUST treat THRIVE-derived capacity and constraint data as protected context inputs.

---

## 14. Governance and Change Control

THRIVE follows semantic versioning.

- MAJOR changes alter required objects or conformance rules.
- MINOR changes add new context types, routines, or capacity dimensions.
- PATCH changes clarify language or fix errors.

---

## Appendix A: Suggested Implementation Package

A conformant implementation SHOULD include:

- A SelfContext schema.
- A capacity profile model.
- Routine templates.
- Recovery and overload patterns.
- A wellness record export format.
- A conformance statement.

---

## Appendix B: Example Conformance Statement

> This implementation conforms to THRIVE v1.1.0 at level H2 for SELF and RECOVERY contexts. It represents capacity, load, routines, and recovery events, maintains records, and avoids punitive framing.

*THRIVE v1.1.0 — Self and Wellness Context Layer*
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*
*First published: 2026-05-28 · Amended: 2026-06-22*
