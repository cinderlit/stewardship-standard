> **Superseded.** This is an archived version. The current specification is
> [QSM v1.1.0](./QSM-v1.1.0.md). See `CHANGELOG.md` [1.1.0] for what changed and why.

# QSM v1.0.1
## Quantified Stewardship Model
### Domain-Agnostic Ontology and Methodology for Legible Stewardship

**Version:** 1.0.1  
**Status:** Final Draft — Ready for Submission  
**Author:** Caitlin Stokes  
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)  
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)  
**DOI:** [10.5281/zenodo.20436570](https://doi.org/10.5281/zenodo.20436570)  
**Published:** 2026-05-28  
**Related Specs:** TSS v1.1.1, THRIVE v1.0.1, QSM-FAI v1.0.1

---

## Abstract

The Quantified Stewardship Model (QSM) is a domain-agnostic, human-centered ontology and
methodology for representing people, places, systems, responsibilities, needs, values, and
relationships in a way that makes stewardship legible, measurable, and improvable. QSM is
intended to support both human and agentic decision-making by providing a structured model
for context, role, dependency, risk, and action.

QSM is designed to be adaptable across self, household, estate, organizational, and public
contexts. It does not prescribe a single use case; instead, it provides a common semantic
substrate on top of which context-specific hardened implementations may be built. HEARTH is
the first hardened context within this family, and QSM-FAI defines the fiduciary agent
interface for acting within a QSM context.

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

QSM exists to answer three questions:

1. What exists in the stewardship domain?
2. What does it need, value, and depend on?
3. What responsibilities, risks, and actions follow from that understanding?

The model is meant to make invisible labor, dependency chains, and care obligations visible
without collapsing them into simplistic task lists.

---

## 2. Scope

QSM applies to any bounded stewardship domain where a steward, or a set of stewards, must
maintain awareness of entities, needs, constraints, and responsibilities over time. This
includes, but is not limited to:

- Self and personal executive function.
- Household and caregiving coordination.
- Property, home, and estate stewardship.
- Organizational and team governance.
- Public or civic coordination contexts.

QSM does not define implementation technology. It is compatible with graph databases,
spreadsheets, JSON schemas, knowledge graphs, agent systems, or manual workflows.

---

## 3. Core Principles

### 3.1 Human-centered stewardship

The model is built around care, responsibility, and clarity rather than extraction, opacity,
or short-term optimization.

### 3.2 Context first

A model is only meaningful when bounded. QSM requires explicit context declaration before any
meaningful interpretation or action.

### 3.3 Visibility of dependency

The model should surface hidden dependencies, failure points, and maintenance obligations.

### 3.4 Measurability without reduction

QSM permits scoring, dashboards, and metrics, but these must preserve the underlying meaning
of the domain and not erase qualitative judgment.

### 3.5 Stewardship over ownership

QSM treats responsibility as active, relational, and ongoing rather than purely possessive.

---

## 4. Structural Layers

QSM is composed of three core layers.

### 4.1 Ontology layer

The ontology layer defines the entities, roles, relationships, and context boundaries in a
stewardship domain.

Typical ontology elements include:
- People and agents.
- Places and assets.
- Systems and subsystems.
- Roles and responsibilities.
- Relationships and dependencies.
- Constraints and permissions.

### 4.2 Needs and values layer

The needs and values layer defines what matters to the people and systems in the context.
This includes:
- Needs.
- Values.
- Risks.
- Priorities.
- Service levels.
- Urgency and tolerance thresholds.

### 4.3 Relationship and action layer

The relationship layer describes how entities depend on one another and what actions arise
from those dependencies. It supports:
- Delegation.
- Coordination.
- Maintenance.
- Escalation.
- Handoffs.
- Accountability.

---

## 5. Core Concepts

| Concept | Definition |
|---|---|
| **Context** | A bounded stewardship domain with explicit scope and participants |
| **Entity** | Any person, place, system, asset, obligation, or meaningful object in scope |
| **Role** | A function or responsibility held by an entity or person |
| **Need** | A condition required for stability, flourishing, or safe operation |
| **Value** | A preference or principle used to prioritize actions |
| **Risk** | A condition that may degrade outcomes or create harm |
| **Dependency** | A relationship in which one entity relies on another |
| **Action** | A proposed or executed change in state, schedule, or relationship |
| **Steward** | The person or entity responsible for overseeing the context |

---

## 6. Context Declaration

A QSM implementation MUST declare its context before it may be considered valid.
A context declaration SHOULD include:

- A unique context identifier.
- A human-readable context name.
- The steward or stewards responsible.
- The scope boundary.
- The date of declaration.
- Any relevant subcontexts or exclusions.

A declaration that lacks boundary definition is incomplete and SHOULD be treated as draft.

### 6.1 Example Context Types

- **SELF** — personal well-being, executive function, habits, and life maintenance.
- **HEARTH** — home and household stewardship.
- **ESTATE** — stewardship of a property or asset (single-property through portfolio scale), held by identified stewards, containing no other contexts. Extends HEARTH.
- **CHARTER** — organizational governance or leadership context with defined leadership.
- **CREST** — a governance context with authority distributed across a board/collective/community; the distributed-authority variant of CHARTER (e.g. an HOA).

---

## 7. Data Model

The QSM data model SHOULD be representable in machine-readable form.
At minimum, a conformant implementation SHOULD support these object classes:

- Context.
- Entity.
- Need.
- Value.
- Role.
- Relationship.
- Risk.
- Action.
- StewardshipRecord.
- ScenarioPattern.

### 7.1 Minimal JSON Shape

```json
{
  "context": {
    "id": "ctx-001",
    "name": "HEARTH",
    "type": "HEARTH",
    "stewards": ["person-001"],
    "scope": "Primary residence and associated household systems"
  },
  "entities": [],
  "needs": [],
  "values": [],
  "roles": [],
  "relationships": [],
  "risks": [],
  "actions": [],
  "records": []
}
```

This shape is intentionally minimal and MAY be extended.

---

## 8. Scenario Patterns

QSM supports recurring scenario templates so the same context can be interpreted consistently.

### 8.1 Example patterns

- **Wildfire response** — evacuation, defensible space, air quality, insurance, communications.
- **Storm/outage** — power loss, heating, backup systems, food, water, contingencies.
- **Caregiving week** — time allocation, support coverage, medication, appointments, respite.
- **Executive-function fairness** — equitable load distribution, reminders, friction reduction.

### 8.2 Pattern rules

Scenario patterns SHOULD:
- Reuse core entities where possible.
- Identify common risks and dependencies.
- Encode default priorities.
- Make deviations from the pattern explicit.

---

## 9. Views and Outputs

QSM implementations MAY produce multiple views of the same graph.
Common views include:

- **Role and needs graph** — shows who depends on what.
- **Scenario timeline** — shows actions, risks, and deadlines over time.
- **Fairness dashboard** — shows distribution of load, unmet needs, and support gaps.
- **Health or readiness view** — shows system condition and risk posture.

Views are derivative artifacts. The graph or source model remains the authoritative record.

---

## 10. Conformance

A QSM implementation MAY claim conformance if it satisfies the following:

- **QSM-01:** It declares a bounded context.
- **QSM-02:** It represents entities, roles, needs, and relationships explicitly.
- **QSM-03:** It includes at least one mechanism for recording risk and action.
- **QSM-04:** It preserves stewardship context across outputs.
- **QSM-05:** It avoids redefining context-specific meanings without explicit declaration.

### 10.1 Conformance levels

| Level | Label | Description |
|---|---|---|
| **C0** | Informational | Describes context informally |
| **C1** | Structured | Uses a defined data model |
| **C2** | Operational | Supports actions, records, and scenario views |
| **C3** | Hardened | Fully supports repeated use in a declared context with auditability |

---

## 11. Relationship to Related Documents

| Document | Role |
|---|---|
| **QSM v1.0.1** | Core ontology and methodology |
| **TSS v1.1.1** | The broader stewardship standard and normative implementation layer |
| **THRIVE v1.0.1** | Self and wellness subcontext |
| **QSM-FAI v1.0.1** | Fiduciary AI interface for acting within QSM contexts |

---

## Appendix A: Recommended Implementation Sequence

1. Declare the context.
2. List the entities.
3. Define needs, values, and risks.
4. Map roles and dependencies.
5. Add scenario patterns.
6. Produce views.
7. Record actions and outcomes over time.

---

## Appendix B: Minimal Example Use

A household context may begin with a single graph containing occupants, appliances, maintenance obligations, and recurring scenarios such as travel, storm outages, or caregiving weeks. The model then expands by adding priorities, thresholds, and recorded actions over time.

*QSM v1.0.1 — Quantified Stewardship Model*  
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*  
*First published: 2026-05-28*


## Appendix C: Formal Schema Appendix

This appendix defines the recommended canonical schema set for QSM implementations.
A conformant implementation SHOULD expose these objects in a machine-readable format.

### C.1 Canonical object set

| Object | Purpose | Required Fields |
|---|---|---|
| Context | Bounded stewardship scope | id, name, type, stewards, scope |
| Entity | Any represented person, place, system, or obligation | id, type, label, status |
| Need | Required condition for stability or flourishing | id, label, priority, target |
| Value | Priority or principle used in decision-making | id, label, weight |
| Role | Function or responsibility in context | id, label, holder, scope |
| Relationship | Explicit link between objects | id, from, to, type |
| Risk | Potential harm or failure mode | id, label, severity, likelihood |
| Action | Proposed or executed change | id, type, actor, target, timestamp |
| StewardshipRecord | Append-only event log entry | id, event_type, timestamp, source |
| ScenarioPattern | Reusable contextual pattern | id, label, triggers, defaults |

### C.2 Minimal canonical JSON shape

```json
{
  "context": {
    "id": "ctx-001",
    "name": "HEARTH",
    "type": "HEARTH",
    "scope": "Primary residence and household systems",
    "stewards": ["person-001"]
  },
  "entities": [],
  "needs": [],
  "values": [],
  "roles": [],
  "relationships": [],
  "risks": [],
  "actions": [],
  "records": [],
  "patterns": []
}
```

### C.3 Schema rules

- C-SCHEMA-01: A conformant implementation SHOULD validate object presence and identifier uniqueness.
- C-SCHEMA-02: A conformant implementation SHOULD preserve provenance for all derived views.
- C-SCHEMA-03: A conformant implementation SHOULD represent relationships explicitly rather than inferring them from free text.
- C-SCHEMA-04: A conformant implementation SHOULD expose exportable JSON as the canonical interchange format.

## Appendix D: Normative Crosswalk

This appendix clarifies how QSM relates to the broader standard stack.

| Layer | Role in the stack | Normative dependency |
|---|---|---|
| QSM v1.0.1 | Ontology and methodology | Base layer |
| THRIVE v1.0.1 | Self and wellness context | Supplies the human-centered context for self stewardship |
| TSS v1.1.1 | Stewardship standard | Governs conformance, records, and interoperable structure |
| QSM-FAI v1.0.1 | Fiduciary AI interface | Constrains agent behavior within QSM contexts |

QSM implementations MAY reference THRIVE-specific need sets when the declared context is SELF.
QSM implementations MUST defer to TSS for conformance language and audit requirements.
QSM-FAI implementations MUST treat QSM as the source of context semantics.

## Appendix E: Normative Language Clarification

Within this specification, the following terms are normative:

- MUST: an absolute requirement for conformance.
- SHOULD: a recommended practice that may be deviated from only with explicit justification.
- MAY: an optional capability.
- MUST NOT: an absolute prohibition.

Where this document uses these terms, the intended force is normative, not advisory.

## Appendix F: Conformance Statement Template

> This implementation conforms to QSM v1.0.1 at level C2 for the HEARTH context. It represents contexts, entities, needs, values, roles, relationships, risks, actions, and records using an explicit machine-readable schema. It preserves context boundaries and produces auditable outputs.
