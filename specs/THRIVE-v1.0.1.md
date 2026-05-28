# THRIVE v1.0.1
## Self and Wellness Context Layer
### Normative Specification for Personal Stewardship, Capacity, and Wellbeing

**Version:** 1.0.1  
**Status:** Final Draft — Ready for Submission  
**Author:** Caitlin Stokes  
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)  
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)  
**DOI:** [pending — Zenodo]  
**Published:** 2026-05-28  
**Dependent Specs:** QSM v1.0.1, TSS v1.1.1, QSM-FAI v1.0.1

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

### 12.2 Minimum conformance rules

- **THRIVE-01:** A conformant implementation MUST declare a SelfContext.
- **THRIVE-02:** A conformant implementation MUST represent capacity and load.
- **THRIVE-03:** A conformant implementation MUST support records and reflection.
- **THRIVE-04:** A conformant implementation MUST preserve dignity and avoid punitive framing.
- **THRIVE-05:** A conformant implementation SHOULD support routines and recovery planning.

---

## 13. Relationship to Other Specs

| Document | Role |
|---|---|
| **QSM v1.0.1** | Core ontology and stewardship model |
| **TSS v1.1.1** | Normative umbrella and audit framework |
| **THRIVE v1.0.1** | Self and wellness context layer |
| **QSM-FAI v1.0.1** | Fiduciary AI interface for acting within the stack |

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

> This implementation conforms to THRIVE v1.0.1 at level H2 for SELF and RECOVERY contexts. It represents capacity, load, routines, and recovery events, maintains records, and avoids punitive framing.

*THRIVE v1.0.1 — Self and Wellness Context Layer*  
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*  
*First published: 2026-05-28*
