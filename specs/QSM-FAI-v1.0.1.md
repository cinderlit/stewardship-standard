> **Superseded.** This is an archived version. The current specification is
> [QSM-FAI v1.1.0](./QSM-FAI-v1.1.0.md). See `CHANGELOG.md` [1.1.0] for what changed and why.

# QSM-FAI v1.0.1
## Quantified Stewardship Model — Fiduciary AI Interface
### Normative Specification

**Version:** 1.0.1  
**Status:** Final Draft — Ready for Submission  
**Author:** Caitlin Stokes  
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)  
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)  
**DOI:** [10.5281/zenodo.20436570](https://doi.org/10.5281/zenodo.20436570)  
**Published:** 2026-05-28  
**First Hardened Context:** HEARTH (Quantified Home)

---

## Abstract

The Quantified Stewardship Model — Fiduciary AI Interface (QSM-FAI) defines a normative
interface layer through which AI agents may act as fiduciaries within stewardship contexts.
It specifies the data structures, behavioral constraints, delegation rules, and accountability
mechanisms required for an AI system to operate within a QSM-conformant environment without
violating stewardship obligations to the entities it serves.

QSM-FAI is domain-agnostic but requires a hardened context — a formally declared stewardship
scope — before any agent may act. HEARTH (the Quantified Home context) is the first such
hardened context and serves as the normative reference implementation throughout this document.

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

## 1. Purpose and Scope

### 1.1 Purpose

QSM-FAI answers a single question: **Under what conditions, and subject to what constraints,
may an AI agent act on behalf of a steward?**

It does not define how AI agents are built. It defines the interface they must conform to —
the declared context, the permission model, the accountability trail, and the exit conditions
that make AI-assisted stewardship trustworthy.

### 1.2 Scope

This specification applies to:
- Any AI agent (LLM-based, rule-based, or hybrid) operating within a QSM-declared context
- Any system that ingests QSM entity graphs and produces actions, recommendations, or reports
- Any platform claiming QSM-FAI conformance

This specification does NOT govern:
- The internal architecture of AI agents
- Training data or model weights
- Non-stewardship AI use cases (e.g., pure content generation)

### 1.3 Relationship to QSM

QSM defines the ontology, needs/values layer, and relationship graph.  
QSM-FAI defines how agents read from, act within, and write back to that graph — subject to
fiduciary constraints.

```
QSM (world model)
    └── QSM-FAI (agent interface + fiduciary rules)
            └── HEARTH / CREST / CHARTER / SELF (hardened contexts)
```

---

## 2. Normative Terms

| Term | Definition |
|------|-----------|
| **Steward** | A person or entity with declared responsibility for an Entity Set |
| **Entity Set** | The bounded collection of people, places, systems, and relationships within a context |
| **Fiduciary Context (FC)** | A formally declared stewardship scope; required before any agent may act |
| **Agent** | Any AI system operating under QSM-FAI; must hold a valid FiduciaryContext object |
| **Delegation Chain** | The ordered list of stewards who have authorized an agent to act |
| **Action** | Any agent output that modifies entity state, schedules work, or triggers a notification |
| **Recommendation** | An agent output that proposes but does not execute an action |
| **Rationale** | A machine-readable justification linking an action to one or more QSM model elements |
| **TENURE Record** | A timestamped audit log entry attached to an entity or action |
| **Hardened Context** | A context with a fully populated LOCUS, a validated ATLAS, and at least one TENURE cycle |

---

## 3. The FiduciaryContext Object

Every QSM-FAI-conformant agent MUST hold a valid `FiduciaryContext` object before taking
any action. This object is the agent's "license to act."

### 3.1 Schema

```json
{
  "$schema": "https://stewardshipstandard.org/schemas/fiduciary-context/v1.0.json",
  "id": "fc-[uuid]",
  "version": "1.0",
  "context_type": "HEARTH | CREST | CHARTER | SELF",
  "label": "string — human-readable name for this context",
  "declared_by": {
    "steward_id": "string",
    "steward_name": "string",
    "declared_at": "ISO8601 timestamp"
  },
  "delegation_chain": [
    {
      "steward_id": "string",
      "role": "primary | delegate | observer",
      "authorized_at": "ISO8601 timestamp",
      "scope": ["read", "recommend", "act", "delegate"]
    }
  ],
  "entity_set_ref": "string — reference to LOCUS document ID",
  "atlas_ref": "string — reference to ATLAS document ID",
  "tenure_log_ref": "string — reference to active TENURE log",
  "constraints": {
    "max_action_tier": 1,
    "require_human_approval_above_tier": 1,
    "spending_limit_usd": null,
    "notification_required_for": ["tier-2-actions", "entity-state-changes"],
    "prohibited_domains": []
  },
  "status": "active | suspended | revoked | expired",
  "expires_at": "ISO8601 timestamp | null"
}
```

### 3.2 Conformance Rules

- **FC-01:** An agent MUST NOT act without a `FiduciaryContext` in `active` status.
- **FC-02:** An agent MUST NOT act outside the scope defined in its delegation chain entry.
- **FC-03:** Any action exceeding `max_action_tier` MUST be downgraded to a Recommendation and
  flagged for human approval.
- **FC-04:** `delegation_chain` MUST include at least one `primary` steward.
- **FC-05:** An agent MUST attach the `fc.id` to every Action and TENURE Record it generates.

---

## 4. Action Tiers

QSM-FAI defines a four-tier action model. Tier determines whether an agent may act autonomously,
must recommend, or must escalate.

| Tier | Label | Examples | Default Agent Permission |
|------|-------|----------|------------------------|
| 0 | **Read** | Query entity state, generate reports, surface gaps | Always permitted |
| 1 | **Recommend** | Propose tasks, draft schedules, flag risks | Always permitted; must attach Rationale |
| 2 | **Notify** | Send alerts, create calendar items, message stewards | Permitted if in delegation scope |
| 3 | **Act** | Modify entity state, schedule vendors, trigger automations | Requires explicit `act` scope in delegation chain |
| 4 | **Delegate** | Grant or modify another agent's FiduciaryContext | Requires `delegate` scope; primary steward only |

### 4.1 Tier Escalation Rule

If an agent determines that a Tier 3 or Tier 4 action is necessary but lacks scope, it MUST:
1. Generate a Recommendation (Tier 1) describing the action
2. Attach a `requires_escalation: true` flag
3. Notify the nearest `primary` steward in the delegation chain
4. Log the escalation attempt in the TENURE Record

---

## 5. Rationale Requirements

Every Recommendation and Action MUST include a machine-readable `rationale` block.

### 5.1 Rationale Schema

```json
{
  "rationale": {
    "addresses_needs": ["need_id_1", "need_id_2"],
    "addresses_risks": ["risk_id_1"],
    "references_requirements": ["REQ-ID-001"],
    "domain": "string — e.g., 'systems', 'safety', 'financial'",
    "urgency": "routine | elevated | critical",
    "human_readable": "string — plain-language explanation for steward"
  }
}
```

### 5.2 Rationale Conformance Rules

- **RAT-01:** A Rationale MUST reference at least one QSM model element (need, risk, or requirement).
- **RAT-02:** `human_readable` MUST be present and non-empty.
- **RAT-03:** `urgency: critical` MUST trigger an immediate notification per FC constraint rules.

---

## 6. TENURE Record (Audit Log)

Every agent action, recommendation, and escalation MUST produce a TENURE Record entry.

### 6.1 TENURE Entry Schema

```json
{
  "tenure_entry": {
    "id": "te-[uuid]",
    "fc_id": "string — FiduciaryContext.id",
    "agent_id": "string",
    "timestamp": "ISO8601",
    "entry_type": "action | recommendation | escalation | notification | read",
    "entity_refs": ["entity_id_1"],
    "summary": "string",
    "rationale_ref": "rationale object or id",
    "outcome": "pending | accepted | rejected | superseded | completed",
    "steward_acknowledgment": {
      "acknowledged_by": "steward_id | null",
      "acknowledged_at": "ISO8601 | null"
    }
  }
}
```

### 6.2 TENURE Conformance Rules

- **TEN-01:** Every agent output MUST produce at least one TENURE entry.
- **TEN-02:** TENURE Records are append-only; prior entries MUST NOT be modified or deleted.
- **TEN-03:** `outcome` MUST be updated when a steward accepts or rejects a recommendation.
- **TEN-04:** TENURE logs MUST be exportable in JSON and human-readable formats.
- **TEN-05:** TENURE Records MUST conform to TSS Record schema and rules (TSS-REC-01 through
  TSS-REC-05). QSM-FAI L-levels map to TSS T-levels as shown in Appendix Z of TSS v1.1.1;
  L2 typically aligns with T2.


---

## 7. HEARTH — First Hardened Context

HEARTH is the QSM context for the Quantified Home. It is the first formally hardened context
under QSM-FAI and serves as the reference implementation.

### 7.1 HEARTH Entity Set (Canonical Domains)

| Domain | Examples |
|--------|---------|
| **Structural** | Foundation, roof, walls, windows, doors |
| **Systems** | HVAC, plumbing, electrical, irrigation |
| **Safety** | Smoke/CO detectors, egress, fire suppression |
| **Financial** | Insurance, warranties, maintenance budget |
| **Lifecycle** | Appliances, fixtures (age, condition, replacement timeline) |
| **Occupants** | Household members, roles, needs, schedules |
| **Relationships** | Vendors, contractors, service providers |
| **Environmental** | Wildfire risk, flood zone, seismic zone, climate exposure |

### 7.2 HEARTH FiduciaryContext — Reference Instance

```json
{
  "id": "fc-hearth-001",
  "version": "1.0",
  "context_type": "HEARTH",
  "label": "Primary Residence — Stewardship Context",
  "declared_by": {
    "steward_id": "steward-001",
    "steward_name": "Primary Homeowner",
    "declared_at": "2026-05-28T00:00:00Z"
  },
  "delegation_chain": [
    {
      "steward_id": "steward-001",
      "role": "primary",
      "authorized_at": "2026-05-28T00:00:00Z",
      "scope": ["read", "recommend", "act", "delegate"]
    },
    {
      "steward_id": "agent-hearth-assistant",
      "role": "delegate",
      "authorized_at": "2026-05-28T00:00:00Z",
      "scope": ["read", "recommend", "notify"]
    }
  ],
  "constraints": {
    "max_action_tier": 1,
    "require_human_approval_above_tier": 1,
    "spending_limit_usd": null,
    "notification_required_for": ["tier-2-actions", "safety-domain-changes", "critical-urgency"],
    "prohibited_domains": []
  },
  "status": "active",
  "expires_at": null
}
```

### 7.3 HEARTH Agent Behavioral Rules

- **HEARTH-01:** An agent operating in HEARTH context MUST surface safety domain gaps before
  any other domain in prioritized output.
- **HEARTH-02:** Environmental risk flags (wildfire, flood, seismic) MUST be re-evaluated at
  minimum annually or upon a declared emergency event.
- **HEARTH-03:** Lifecycle tracking for all systems MUST include estimated replacement date and
  cost; gaps in this data MUST be flagged as Tier 1 recommendations.
- **HEARTH-04:** Occupant needs (health, mobility, care dependencies) MUST be represented in
  the entity graph and considered in all scheduling recommendations.

---

## 8. Conformance Levels

| Level | Label | Requirements |
|-------|-------|-------------|
| **L0** | Observer | Read-only; generates no TENURE entries; no FiduciaryContext required |
| **L1** | Advisor | Holds FiduciaryContext; generates Tier 0–1 outputs with Rationale and TENURE |
| **L2** | Operator | L1 + authorized for Tier 2–3 actions within declared scope |
| **L3** | Steward AI | L2 + full delegation chain management; TENURE export and human handoff protocols |

A conformant implementation MUST declare its conformance level in its system manifest.

---

## 9. Prohibited Behaviors

Regardless of delegation scope, a QSM-FAI-conformant agent MUST NOT:

- **PROHIB-01:** Take any action that removes a human steward from the delegation chain entirely
- **PROHIB-02:** Modify or delete TENURE records
- **PROHIB-03:** Act on behalf of a steward whose FiduciaryContext has `status: revoked`
- **PROHIB-04:** Execute financial transactions without explicit `act` scope AND a spending limit
  defined in the FiduciaryContext constraints
- **PROHIB-05:** Override a steward's explicit rejection of a prior recommendation on the same
  entity without a new rationale citing changed conditions

---

## 10. Versioning and Governance

- This document follows semantic versioning: `MAJOR.MINOR.PATCH`
- Breaking changes to schema or conformance rules increment MAJOR
- Additive changes (new context types, new optional fields) increment MINOR
- Clarifications and errata increment PATCH
- Community feedback and proposed amendments: [github.com/cinderlit/stewardship-standard/issues]
- Maintainer review cycle: quarterly

---

## Appendix A: Quick Reference — Conformance Checklist

- [ ] Agent holds a valid, active FiduciaryContext before any action
- [ ] All outputs include a Rationale with at least one QSM model element reference
- [ ] All outputs produce a TENURE Record entry
- [ ] Tier 3+ actions require `act` scope in delegation chain
- [ ] Critical urgency triggers immediate steward notification
- [ ] TENURE log is append-only and exportable
- [ ] Conformance level declared in system manifest

---

## Appendix B: Relationship to Other QSM Documents

| Document | Role |
|----------|------|
| **QSM v1.0.1** | Core ontology and modeling framework; QSM-FAI is a dependent spec |
| **TSS v1.1.1** | The Stewardship Standard; normative open standard QSM-FAI implements |
| **THRIVE v1.0.1** | Human wellness and Self context layer; informs occupant need modeling in HEARTH |
| **QSM-FAI v1.0.1** | This document |

---

*QSM-FAI v1.0.1 — Quantified Stewardship Model: Fiduciary AI Interface*  
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*  
*First published: 2026-05-28*
