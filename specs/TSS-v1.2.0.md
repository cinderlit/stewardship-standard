# TSS v1.2.0
## The Stewardship Standard
### Normative Framework for Context, Care, Accountability, and Action

**Version:** 1.2.0
**Status:** Final Draft — Ready for Submission
**Author:** Caitlin Stokes
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)
**DOI:** [10.5281/zenodo.20436570](https://doi.org/10.5281/zenodo.20436570)
**Published:** 2026-05-28
**Amended:** 2026-06-22 (v1.2.0 — see `CHANGELOG.md`)
**Dependent Specs:** QSM v1.1.0, THRIVE v1.1.0, QSM-FAI v1.1.0

---

## Abstract

The Stewardship Standard (TSS) defines a normative framework for representing, managing,
and auditing stewardship across bounded contexts. It specifies the required concepts,
structures, conformance rules, and machine-readable schemas needed to make responsibility,
care, dependency, and action explicit in a system that may be implemented by humans,
software, or hybrid agentic workflows.

TSS is designed as a standards layer: QSM defines the ontology and modeling foundation,
THRIVE defines the human Self and wellness context, and QSM-FAI defines the fiduciary AI
interface for acting within a stewardship context. TSS provides the normative structure that
makes these components interoperable and auditable.

---

## Status of This Document

This document is a living technical specification within The Stewardship Standard
stack. It is an openly accessible reference for implementers and practitioners and
may evolve over time through public feedback and practical experience. Changes are
recorded in the public change history (`CHANGELOG.md`) and tracked through public
issues in the canonical repository; the latest editor's draft there is authoritative.

**v1.2.0 amendment note:** this revision adds the **Assignment** object and named delegation
models (§5.12), formalizes the **LOCUS → ATLAS → TENURE** stewardship-phase lifecycle as a
normative Context property (§6.2), and clarifies that an audit trail MAY be composed of
multiple linked Record subtypes (§9.1). All changes are additive; no v1.1.1 requirement was
removed or tightened, and v1.1.1 conformance claims remain valid under v1.2.0. See
`CHANGELOG.md` [1.1.0] for the full amendment record and implementation evidence.

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

TSS exists to establish a common, implementation-neutral standard for stewardship systems.
It enables:

- Explicit context declaration.
- Explicit representation of entities, roles, needs, and risks.
- Explicit delegation and accountability.
- Explicit logging of stewardship actions and outcomes.
- Interoperable schemas across contexts and implementations.

The standard is intentionally general so that it can support self-management, household
coordination, estate stewardship, team governance, and similar domains.

---

## 2. Scope

TSS applies to any system that:

- Declares a bounded stewardship context.
- Tracks relationships between entities and responsibilities.
- Produces decisions, recommendations, or actions grounded in that context.
- Requires auditable records of stewardship over time.

TSS does not prescribe a specific software architecture, interface style, or storage engine.

---

## 3. Core Principles

### 3.1 Context specificity

Every stewardship claim MUST be evaluated within a declared context.

### 3.2 Accountability

Every recommendation or action SHOULD be attributable to a steward, delegate, or approved
agent.

### 3.3 Auditability

Actions and state changes MUST be traceable through records.

### 3.4 Interoperability

Core concepts SHOULD be representable in a portable, machine-readable format.

### 3.5 Non-reductionism

The standard MUST preserve meaning, not merely count events or tasks.

---

## 4. Normative Terms

| Term | Definition |
|---|---|
| **Context** | A bounded stewardship domain with explicit scope |
| **Entity** | Any person, place, system, obligation, or asset represented in the context |
| **Steward** | A responsible human or organizational actor |
| **Delegate** | A human or agent acting under authorized scope |
| **Need** | A condition required for stability, wellbeing, or proper function |
| **Risk** | A condition that may harm the context or degrade outcomes |
| **Action** | A change to state, schedule, responsibility, or communication |
| **Record** | An auditable entry describing a stewardship event |
| **Assignment** | A binding between a Role or Responsibility and the Steward(s) or Delegate(s) who hold it, under a named delegation model |
| **Conformance** | Demonstrated adherence to the rules of this standard |

### 4.1 Normative language

Within this specification:

- **MUST**: an absolute requirement for conformance.
- **MUST NOT**: an absolute prohibition.
- **SHOULD**: a recommended practice that may be deviated from only with explicit justification.
- **MAY**: an optional capability.

Where this document uses these terms, the intended force is normative.

---

## 5. Required Objects and Normative Rules

A conformant implementation MUST support, at minimum, the following object types:

1. Context
2. Entity
3. Role
4. Need
5. Value
6. Risk
7. Relationship
8. Action
9. Record
10. ScenarioPattern
11. ConformanceClaim
12. Assignment *(conditionally required — see §5.12; required wherever the implementation
    supports Role-based delegation)*

Each object MUST satisfy the rules in this section.

### 5.1 Context

- **TSS-CTX-01:** Each Context MUST have a unique identifier.
- **TSS-CTX-02:** Each Context MUST have a name, type, and scope.
- **TSS-CTX-03:** Each Context MUST declare at least one Steward.
- **TSS-CTX-04:** Each Context MUST have an effective date and version.
- **TSS-CTX-05:** Each Context MUST NOT be conflated with another context without explicit mapping.

### 5.2 Entity

- **TSS-ENT-01:** Each Entity MUST have a unique identifier and type.
- **TSS-ENT-02:** Each Entity MUST have a human-readable label.
- **TSS-ENT-03:** Each Entity MUST have a status (e.g., active, deprecated).
- **TSS-ENT-04:** Each Entity MUST be assignable to at least one Context.

### 5.3 Role

- **TSS-ROLE-01:** Each Role MUST have a unique identifier and label.
- **TSS-ROLE-02:** Each Role MUST define a scope or set of responsibilities.
- **TSS-ROLE-03:** Each Role MUST be held by at least one Steward or Delegate.
- **TSS-ROLE-04:** Each Role MUST be assignable to a Context.

### 5.4 Need

- **TSS-NEED-01:** Each Need MUST have a unique identifier and label.
- **TSS-NEED-02:** Each Need MUST reference at least one Entity or Role.
- **TSS-NEED-03:** Each Need MUST have a priority or urgency indicator.
- **TSS-NEED-04:** Each Need MUST be representable in a machine-readable format.

### 5.5 Value

- **TSS-VAL-01:** Each Value MUST have a unique identifier and label.
- **TSS-VAL-02:** Each Value MAY have a weight or ranking.
- **TSS-VAL-03:** Each Value MUST be usable in decision-making or prioritization.

### 5.6 Risk

- **TSS-RISK-01:** Each Risk MUST have a unique identifier and label.
- **TSS-RISK-02:** Each Risk MUST have severity and likelihood indicators.
- **TSS-RISK-03:** Each Risk MUST reference at least one Entity, Role, or Context.
- **TSS-RISK-04:** Each Risk MUST be representable in a machine-readable format.

### 5.7 Relationship

- **TSS-REL-01:** Each Relationship MUST have a unique identifier.
- **TSS-REL-02:** Each Relationship MUST have a from and to reference.
- **TSS-REL-03:** Each Relationship MUST have a type (e.g., depends_on, supports, owns).
- **TSS-REL-04:** Each Relationship MUST be assignable to a Context.

### 5.8 Action

- **TSS-ACT-01:** Each Action MUST have a unique identifier and type.
- **TSS-ACT-02:** Each Action MUST have an actor (Steward, Delegate, or Agent).
- **TSS-ACT-03:** Each Action MUST have a target Entity or Context.
- **TSS-ACT-04:** Each Action MUST have a timestamp and status.
- **TSS-ACT-05:** Each Action MUST be attributable and auditable.

### 5.9 Record

- **TSS-REC-01:** Each Record MUST have a unique identifier.
- **TSS-REC-02:** Each Record MUST have an event_type and timestamp.
- **TSS-REC-03:** Each Record MUST be append-only.
- **TSS-REC-04:** Each Record MUST be exportable in a structured format.
- **TSS-REC-05:** Each Record MUST NOT be silently overwritten or deleted.

### 5.10 ScenarioPattern

- **TSS-SCEN-01:** Each ScenarioPattern MUST have a unique identifier and label.
- **TSS-SCEN-02:** Each ScenarioPattern MUST define triggers or applicable conditions.
- **TSS-SCEN-03:** Each ScenarioPattern MUST define default priorities or risks.
- **TSS-SCEN-04:** Each ScenarioPattern MUST be assignable to a Context.

### 5.11 ConformanceClaim

- **TSS-CONF-01:** Each ConformanceClaim MUST have a unique identifier.
- **TSS-CONF-02:** Each ConformanceClaim MUST specify the TSS version claimed.
- **TSS-CONF-03:** Each ConformanceClaim MUST specify the context type(s) supported.
- **TSS-CONF-04:** Each ConformanceClaim MUST specify the conformance level claimed.
- **TSS-CONF-05:** Each ConformanceClaim MUST declare any deviations.

### 5.12 Assignment *(added v1.2.0)*

An Assignment binds a Role or Responsibility to the Steward(s) or Delegate(s) who hold it,
under a named delegation model. Assignment formalizes a pattern implementations consistently
need as soon as more than one person or agent can be responsible for the same Role: not just
*who* holds a Role, but *how* responsibility is distributed across multiple holders.

- **TSS-ASN-01:** Each Assignment MUST have a unique identifier.
- **TSS-ASN-02:** Each Assignment MUST reference exactly one Role (or Responsibility, where the
  implementation distinguishes the two) and at least one holder (Steward or Delegate).
- **TSS-ASN-03:** Each Assignment MUST declare a `model` field (see §5.12.1).
- **TSS-ASN-04:** Each Assignment MUST be assignable to a Context.

#### 5.12.1 Delegation Models

`model` is an open, extensible enumeration. The following values are recognized by this
standard:

- **RACI** — Responsible, Accountable, Consulted, Informed. Each holder on the Assignment MAY
  carry one of these four sub-roles.
- **DACI** — Driver, Approver, Contributor, Informed.
- **MOCHA** — Manager, Owner, Consulted, Helper, Approver.
- **unstructured** — a single holder with no further sub-role distinction; the default for the
  common case of one Role, one holder.

Implementations MAY define additional `model` values beyond this list, but per TSS-CONF-05 a
ConformanceClaim using a non-listed model SHOULD declare it as a deviation so the claim remains
explicit about what a reader can assume.

---

## 6. Context Declaration

A context declaration MUST include:

- Context identifier.
- Context name.
- Context type.
- Steward or steward set.
- Effective date.
- Scope boundary.
- Exclusions, if any.
- Version.

A context without an explicit boundary is not conformant.

Context lifecycle — creation, state transitions (draft / active / suspended / retired), and object disposition on retirement — is defined in QSM-ARCH §6.6.

### 6.1 Context types

The standard recognizes, at minimum:
- SELF
- HEARTH
- ESTATE
- CHARTER
- CREST
- QSM_META *(added v1.2.0 — see QSM §6.1; a singleton, non-steward-owned governance context, not
  a stewarded entity. Excluded from §6.2 phase rules below: QSM_META has no stewardship phase.)*

**Note:** HEARTH is the first hardened context for the stewardship stack. QSM and QSM-FAI reference HEARTH as the priority hardened context and reference implementation.
Additional context types MAY be added in future versions if they preserve compatibility.

### 6.2 Stewardship Phase *(added v1.2.0)*

A Context's relationship to its own data matures over time. Implementation experience across
multiple concurrent contexts (see `CHANGELOG.md` [1.1.0]) converged independently on the same
three-phase lifecycle that QSM-FAI's "Hardened Context" definition already implies but never
names on its own. TSS now defines it directly, as an optional but RECOMMENDED Context property.

- **LOCUS** — establishing ground truth. The Context has a declared Steward and a structured,
  even if incomplete, inventory of what exists. No scoring or automated prioritization is
  expected to be meaningful yet.
- **ATLAS** — mapping the option space. The Context has at least one mapped Domain,
  Responsibility, System, or equivalent structural Entity, and a declared approach to
  prioritization (e.g., a needs framework per QSM §4.2.1).
- **TENURE** — ongoing maintenance. The Context is in a recurring review/scoring/oversight loop:
  cadence-driven reviews, health scoring, and escalation are active.

A conformant implementation MAY represent this as a `stewardship_phase` field on Context, with
enum value `locus | atlas | tenure`.

- **TSS-PHASE-01:** If a `stewardship_phase` field is present, a Context MUST NOT transition
  from `locus` to `atlas` unless TSS-CTX-03 (a declared Steward) is already satisfied.
- **TSS-PHASE-02:** A Context MUST NOT transition from `atlas` to `tenure` unless at least one
  structural Entity (Domain, Responsibility, System, or equivalent) is mapped to it.
- **TSS-PHASE-03:** An implementation MAY allow a Context to skip or reverse a phase, but any
  such transition MUST produce a Record (per §9) carrying an explicit justification. Skipping or
  reversing a phase MUST NOT happen silently.
- **TSS-PHASE-04:** QSM_META contexts (§6.1) are exempt from this section; they have no
  `stewardship_phase`.

This section is RECOMMENDED, not required for any conformance level below T3, since `locus`/
`atlas`/`tenure` gating is meaningful primarily for implementations that actively block premature
transitions rather than merely describing maturity informally.

---

## 7. Required Relationships

A conformant implementation MUST be able to represent:

- Steward to context.
- Entity to entity dependency.
- Role to responsibility.
- Need to entity or role.
- Risk to entity, role, or context.
- Action to steward or delegate.
- Record to the event it describes.

Relationships SHOULD be explicit rather than inferred.

---

## 8. Scenario Modeling

TSS requires support for recurring or high-value scenario patterns.

### 8.1 Pattern examples

- Wildfire.
- Storm or outage.
- Caregiving week.
- Executive-function fairness.
- Travel or absence.
- Transition or handoff.

### 8.2 Pattern rules

A scenario pattern SHOULD:
- Declare the conditions under which it applies.
- Name the entities and roles most likely to be involved.
- Identify the default risks and priorities.
- Record departures from the pattern when they occur.

---

## 9. Records and Audit Trail

A conformant system MUST maintain an append-only record of stewardship-relevant events.

### 9.1 Record types

> Implementations MAY use domain-specific names (e.g., StewardshipRecord, WellnessRecord, TENURE Record) as long as they satisfy TSS Record rules. An implementation's audit trail MAY also be
> composed of several linked Record subtypes (for example, a run log, a review log, and an
> escalation outbox) rather than a single flat log, provided each subtype independently
> satisfies TSS-REC-01 through TSS-REC-05 and the relationships between subtypes are explicit
> (§7).
- Context declaration.
- Entity creation or update.
- Role assignment.
- Need or risk update.
- Recommendation.
- Action.
- Escalation.
- Human acknowledgment.
- Conformance claim.

### 9.2 Record rules

- Records MUST be timestamped.
- Records MUST be attributable.
- Records MUST be exportable in a structured format.
- Records MUST NOT be silently overwritten.

---

## 10. Governance Bridge: How TSS Governs QSM and QSM-FAI

TSS is the normative umbrella that governs both QSM and QSM-FAI in practice.

### 10.1 TSS and QSM

QSM defines the ontology and modeling foundation. TSS governs QSM by:

- Requiring explicit context declaration before any QSM model is considered valid.
- Standardizing the required object types (Context, Entity, Need, Role, etc.).
- Imposing record and audit requirements on any QSM implementation claiming conformance.
- Defining conformance levels (T0–T3) that QSM implementations MUST map to.

A QSM implementation MAY claim TSS conformance only if it satisfies TSS-01 through TSS-05.

### 10.2 TSS and QSM-FAI

QSM-FAI defines the fiduciary AI interface for acting within a QSM context. TSS governs QSM-FAI by:

- Requiring that any agent action be attributable to a Steward, Delegate, or approved Agent.
- Standardizing the record and audit requirements for all agent actions.
- Defining how delegation, scope, and conformance claims are represented.
- Preserving QSM context semantics while imposing TSS audit and accountability rules.

A QSM-FAI implementation MUST treat TSS Record and ConformanceClaim rules as binding.

### 10.3 TSS and THRIVE

THRIVE defines the Self and wellness context layer. TSS governs THRIVE by:

- Requiring that THRIVE SelfContext declarations conform to TSS Context rules.
- Standardizing capacity, need, routine, and record objects within the TSS object framework.
- Imposing audit and export requirements on THRIVE implementations.
- Ensuring that THRIVE-derived data is treated as protected context in QSM-FAI interfaces.

A THRIVE implementation MAY claim conformance only if it satisfies TSS record and conformance rules.

---

## 11. Machine-Readable Schemas

TSS MAY be implemented with JSON, YAML, graph schemas, or other structured formats.
A conformant implementation SHOULD provide schemas for at least the following:

1. Context schema.
2. Entity schema.
3. Relationship schema.
4. Record schema.
5. ConformanceClaim schema.
6. Assignment schema *(added v1.2.0; required wherever §5.12 applies)*.

### 11.1 Formal schema appendix

The following schemas are normative reference schemata for TSS v1.2.0.

#### 11.1.1 context.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS Context Schema",
  "type": "object",
  "required": ["id", "name", "type", "stewards", "effective_date", "scope", "version"],
  "properties": {
    "id": { "type": "string" },
    "name": { "type": "string" },
    "type": { "type": "string", "enum": ["SELF", "HEARTH", "ESTATE", "CHARTER", "CREST", "QSM_META"] },
    "stewards": {
      "oneOf": [
        { "type": "array", "items": { "type": "string" }, "minItems": 1 },
        { "type": "string" }
      ],
      "description": "MAY be a single steward reference or an array of stewards. A QSM_META context (type: QSM_META) is exempt from this requirement per QSM-META-01."
    },
    "effective_date": { "type": "string", "format": "date-time" },
    "scope": { "type": "string" },
    "exclusions": { "type": "array", "items": { "type": "string" } },
    "version": { "type": "string" },
    "is_template": { "type": "boolean", "default": false, "description": "Added v1.2.0. See QSM §6.2." },
    "template_id": { "type": ["string", "null"], "description": "Added v1.2.0. References the template Context this instance was duplicated from, if any. See QSM §6.2." },
    "needs_framework": { "type": ["string", "null"], "description": "Added v1.2.0. e.g. 'maslow', 'well', 'erg', 'pink'. See QSM §4.2.1." },
    "stewardship_phase": { "type": "string", "enum": ["locus", "atlas", "tenure"], "description": "Added v1.2.0. See §6.2." }
  }
}
```

#### 11.1.2 entity.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS Entity Schema",
  "type": "object",
  "required": ["id", "type", "label", "status"],
  "properties": {
    "id": { "type": "string" },
    "type": { "type": "string" },
    "label": { "type": "string" },
    "status": { "type": "string", "enum": ["active", "inactive", "deprecated"] },
    "context_id": { "type": "string" }
  }
}
```

#### 11.1.3 relationship.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS Relationship Schema",
  "type": "object",
  "required": ["id", "from", "to", "type"],
  "properties": {
    "id": { "type": "string" },
    "from": { "type": "string" },
    "to": { "type": "string" },
    "type": { "type": "string" },
    "context_id": { "type": "string" }
  }
}
```

#### 11.1.4 record.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS Record Schema",
  "type": "object",
  "required": ["id", "event_type", "timestamp"],
  "properties": {
    "id": { "type": "string" },
    "event_type": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "actor_id": { "type": "string" },
    "context_id": { "type": "string" },
    "summary": { "type": "string" },
    "details": { "type": "object" }
  }
}
```

#### 11.1.5 conformance-claim.schema.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS ConformanceClaim Schema",
  "type": "object",
  "required": ["id", "tss_version", "context_types", "conformance_level"],
  "properties": {
    "id": { "type": "string" },
    "tss_version": { "type": "string" },
    "context_types": {
      "type": "array",
      "items": { "type": "string" }
    },
    "conformance_level": { "type": "string", "enum": ["T0", "T1", "T2", "T3"] },
    "deviations": { "type": "array", "items": { "type": "string" } },
    "claimant": { "type": "string" },
    "claimed_at": { "type": "string", "format": "date-time" }
  }
}
```

#### 11.1.6 assignment.schema.json *(added v1.2.0)*

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "TSS Assignment Schema",
  "type": "object",
  "required": ["id", "role_id", "holders", "model"],
  "properties": {
    "id": { "type": "string" },
    "role_id": { "type": "string", "description": "References a Role or Responsibility." },
    "holders": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "required": ["holder_id"],
        "properties": {
          "holder_id": { "type": "string" },
          "sub_role": { "type": "string", "description": "e.g. 'responsible', 'accountable', 'driver', 'owner' — meaningful only relative to `model`." }
        }
      }
    },
    "model": { "type": "string", "enum": ["RACI", "DACI", "MOCHA", "unstructured"] },
    "context_id": { "type": "string" }
  }
}
```

### 11.2 Schema rules

- **TSS-SCH-01:** A conformant implementation MUST validate that required fields are present.
- **TSS-SCH-02:** A conformant implementation MUST validate that identifiers are unique within context.
- **TSS-SCH-03:** A conformant implementation SHOULD export data in JSON.

---

## 12. Conformance

A system MAY claim conformance only if it satisfies the requirements in this section.

### 12.1 Conformance levels

| Level | Label | Description |
|---|---|---|
| **T0** | Descriptive | Describes stewardship concepts informally |
| **T1** | Structured | Uses explicit objects and relationships |
| **T2** | Auditable | Maintains append-only records and exports them |
| **T3** | Normative | Fully implements required object types, context rules, and scenario support |

### 12.2 Conformance claim requirements

A conformance claim MUST specify:
- The version of TSS claimed.
- The context type(s) supported.
- The conformance level claimed.
- Any deviations or partial implementations.

### 12.3 Minimum conformance rules

- **TSS-01:** A conformant system MUST declare context.
- **TSS-02:** A conformant system MUST represent entities and relationships.
- **TSS-03:** A conformant system MUST maintain records.
- **TSS-04:** A conformance claim MUST be explicit and versioned.
- **TSS-05:** A system MUST NOT claim compliance with a context it cannot represent.

---

## 13. Relationship to Dependent Specs

| Document | Role |
|---|---|
| **QSM v1.1.0** | Ontology and modeling foundation |
| **TSS v1.2.0** | Normative umbrella standard |
| **THRIVE v1.1.0** | Self and wellness context layer |
| **QSM-FAI v1.1.0** | Fiduciary AI interface for context-bound action |

---

## 14. Governance and Change Control

TSS and the stewardship stack follow semantic versioning across three distinct version tracks:

| Track | Example | Scope |
|---|---|---|
| **Spec version** | QSM-ARCH 1.1.0 | The architecture or normative standard itself |
| **Profile version** | QSM-HOUSEHOLD 1.0.0 | Domain-specific adaptations and context profiles |
| **Implementation version** | tooling, schemas, templates | Machine-readable artifacts and reference implementations |

### 14.1 Change classes

- **MAJOR** — layer added or removed, layer semantics changed, invariants changed, or breaking changes to required objects or conformance.
- **MINOR** — new examples, new non-breaking guidance, new optional artifacts, new context types, object types, or optional capabilities.
- **PATCH** — wording fixes, clarifications, typographical corrections without altering conformance.

### 14.2 Deprecation policy

Deprecated terms and constructs MUST remain in the spec with a `deprecated since:` notice for at least one major version before removal. A migration appendix MUST list each deprecated term, its successor, and the version in which it was removed.

### 14.3 Release front matter

Every spec release MUST carry: version number, date, changelog, rationale, compatibility notes, and migration guidance.

Proposed amendments SHOULD be accompanied by example data and at least one use case.

### 14.4 Conflict resolution

When disputes arise about the standard, implementations SHOULD classify the conflict before attempting resolution:

| Conflict type | Description | First resolution step |
|---|---|---|
| **Interpretation conflict** | Two parties read the same rule differently | Structured review against the normative text |
| **Boundary conflict** | Disagreement about which layer or spec owns something | Layer definition + anti-pattern check |
| **Version conflict** | Competing edits or incompatible releases | Versioning rules in TSS (§14.1–14.3) |
| **Authority conflict** | Disagreement about who has decision rights | Spec steward determination |
| **Compliance conflict** | An implementation diverges from the standard | Conformance check against the relevant spec |

Core semantics can only be changed through a formal versioned release, not through informal resolution of individual conflicts.

---

## Appendix Z: Conformance Alignment Across the Stack

This appendix clarifies how conformance levels across QSM, THRIVE, and QSM-FAI relate to TSS levels.

### Z.1 Level mapping

Implementations SHOULD aim for aligned levels when possible. A typical operational conformance is:

| QSM | TSS | THRIVE | QSM-FAI | Label |
|-----|-----|--------|---------|-------|
| C0 | T0 | H0 | L0 | Observational / Informal |
| C1 | T1 | H1 | L1 | Structured |
| C2 | T2 | H2 | L2 | Operational / Auditable |
| C3 | T3 | H3 | L3 | Normative / Full |

### Z.2 Primary audit standard

**TSS T-level is the primary audit standard.**
QSM C-level, THRIVE H-level, and QSM-FAI L-level are domain-specific interpretations of the same conformance tier.

An implementation claiming "TSS T2" MAY also claim "QSM C2", "THRIVE H2", and "QSM-FAI L2" if it satisfies the respective domain-level rules.

### Z.3 QSM-ARCH A-levels (separate axis)

QSM-ARCH conformance levels (A0–A3) measure **architectural completeness** — how many layers and cross-cutting planes an implementation supports. They are independent of the C/T/H/L ladder above. An implementation MAY claim any combination (e.g., T2 + A1). For the relationship between scales, see QSM-ARCH §8.3.

## Appendix A: Submission Bundle — Sample Package

A submission-ready TSS package SHOULD include:

- TSS v1.2.0 specification (this document).
- QSM v1.1.0 specification.
- THRIVE v1.1.0 specification.
- QSM-FAI v1.1.0 specification.
- A schemas/ directory with the reference JSON schemas (six core TSS schemas as of v1.2.0).
- One sample context bundle (e.g., HEARTH or SELF) in JSON.
- One sample conformance claim in JSON.
- A README.md describing the package.

### A.1 Sample bundle structure

```text
stewardship-stack/
├── README.md
├── specs/
│   ├── QSM-v1.1.0.md
│   ├── THRIVE-v1.1.0.md
│   ├── QSM-FAI-v1.1.0.md
│   └── TSS-v1.2.0.md
├── schemas/
│   ├── context.schema.json
│   ├── entity.schema.json
│   ├── relationship.schema.json
│   ├── record.schema.json
│   ├── conformance-claim.schema.json
│   └── assignment.schema.json
├── samples/
│   ├── hearth-context.json
│   └── default-conformance-claim.json
└── LICENSE
```

### A.2 Sample HEARTH context (hearth-context.json)

```json
{
  "context": {
    "id": "ctx-hearth-001",
    "name": "Primary Residence Stewardship",
    "type": "HEARTH",
    "stewards": ["person-001"],
    "effective_date": "2026-05-28T00:00:00Z",
    "scope": "Single-family home and household systems",
    "version": "1.0"
  },
  "entities": [
    {
      "id": "entity-hvac-001",
      "type": "System",
      "label": "HVAC System",
      "status": "active"
    }
  ],
  "needs": [
    {
      "id": "need-safety-001",
      "label": "Air quality and heating safety",
      "priority": "high"
    }
  ],
  "risks": [
    {
      "id": "risk-hvac-001",
      "label": "HVAC failure in winter",
      "severity": "high",
      "likelihood": "medium"
    }
  ]
}
```

### A.3 Sample conformance claim (default-conformance-claim.json)

```json
{
  "id": "claim-001",
  "tss_version": "1.2.0",
  "context_types": ["HEARTH", "SELF"],
  "conformance_level": "T2",
  "deviations": [],
  "claimant": "Cinderlit",
  "claimed_at": "2026-05-28T00:00:00Z"
}
```

---

## Appendix B: Example Conformance Statement

> This implementation conforms to TSS v1.2.0 at level T2 for HEARTH and SELF contexts. It
> supports explicit context declaration, entity and relationship modeling, and append-only
> stewardship records. It does not yet support CHARTER or ESTATE contexts.

*The Stewardship Standard (TSS) v1.2.0*
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*
*First published: 2026-05-28 · Amended: 2026-06-22*
