# QSM-FAI v1.3.0
## Quantified Stewardship Model — Fiduciary AI Interface
### Normative Specification

**Version:** 1.3.0
**Status:** Final Draft — Ready for Submission
**Author:** Caitlin Stokes
**Affiliation:** Cinderlit (cinderlit.com) · The Stewardship Standard (stewardshipstandard.org)
**License:** CC BY 4.0 (specification) · Apache 2.0 (reference schemas)
**DOI:** [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569)
**Published:** 2026-05-28
**Amended:** 2026-07-06 (v1.3.0 — see `CHANGELOG.md`)
**First Hardened Context:** HEARTH (Quantified Home)
**Dependent Specs:** QSM v1.1.0, TSS v1.2.0, THRIVE v1.1.0, QSM-ARCH v1.2.0

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

**v1.1.0 amendment note:** this revision formalizes the single `requires_escalation` flag
(§4.1) into a named Escalation Taxonomy (§4.2) and a standing Escalation Outbox pattern (§4.3),
adds an optional Delegate Track Record to `delegation_chain` entries (§3.3), notes that
`entry_type` on TENURE entries is extensible (§6.1), and adds a prohibited behavior excluding
QSM_META governance contexts from agent action (§9, PROHIB-06). All changes are additive or
optional **with one exception, corrected in the v1.4.1 bundle: `ESC-01` (§4.2) requires every
escalation to be classified, which v1.0.1 §4.1 permitted to be left unclassified — so a v1.0.1
implementation emitting a bare `requires_escalation: true` is not conformant at v1.1.0 or
later.** All other v1.0.1 conformance claims remain valid under v1.1.0. See `CHANGELOG.md`
[1.4.1] § *Correction to the [1.1.0] change record* for the correction and the migration note,
and [1.1.0] for the full amendment record and implementation evidence.

`PROHIB-06` reads like a second such exception and is **not** one: `QSM_META` was introduced in
the same release (QSM v1.1.0 §6.1), so no v1.0.1 context could carry that type and nothing
previously conformant could retroactively violate it.

**v1.2.0 amendment note:** this revision adds an optional Continuity block to the
FiduciaryContext (§3.4) covering steward availability, backup designation, and
agent-as-backup-steward; adds `steward_unavailable` to the Escalation Taxonomy
(§4.2); names `continuity_event` as an optional TENURE `entry_type` (§6.1); and
adds PROHIB-07 (§9). All changes are additive or optional; no v1.1.0 requirement
was removed or tightened, and v1.0.1 and v1.1.0 conformance claims remain valid
under v1.2.0. See `CHANGELOG.md` [1.3.0] for the amendment record.

**v1.3.0 amendment note:** this revision adds optional `action_tier` on TENURE entries
(§6.1) for audit queries by Action Tier without a join. Declined amendments from the
governance-closure review (Escalation Outbox SHOULD→MUST; numeric confidence on
escalation taxonomy) are recorded in `CHANGELOG.md` [1.4.0] with revisit triggers.
All changes are additive or optional; no v1.2.0 requirement was removed or tightened.

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
            └── HEARTH / CREST / CHARTER / SELF / ESTATE (hardened contexts)
```

Note: `QSM_META` (QSM §6.1) is a governance context, not a hardened context, and is not a valid
target for agent action — see PROHIB-06.

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
| **Escalation Outbox** *(added v1.1.0)* | A standing, queryable collection of unresolved escalations awaiting steward attention (see §4.3) |
| **Track Record** *(added v1.1.0)* | An optional, rolling summary of a delegate's accepted/rejected/superseded outcome history (see §3.3) |
| **Backup Steward** *(added v1.2.0)* | A human or agent designated to assume bounded operational authority for a steward's scope upon continuity activation (see §3.4) |
| **Continuity Activation** *(added v1.2.0)* | The recorded event by which a backup steward gains its pre-declared authority, triggered by an availability transition (QSM-ARCH §6.2.1) |
| **Steward Availability** *(added v1.2.0)* | A steward's declared or detected capacity state within a context: `available`, `limited`, or `unavailable` (QSM-ARCH §6.2.1) |

---

## 3. The FiduciaryContext Object

Every QSM-FAI-conformant agent MUST hold a valid `FiduciaryContext` object before taking
any action. This object is the agent's "license to act."

### 3.1 Schema

```json
{
  "$schema": "https://stewardshipstandard.org/schemas/fiduciary-context/v1.1.json",
  "id": "fc-[uuid]",
  "version": "1.0",
  "context_type": "HEARTH | CREST | CHARTER | SELF | ESTATE",
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
      "scope": ["read", "recommend", "act", "delegate"],
      "availability": "available | limited | unavailable",
      "track_record": {
        "accepted_count": 0,
        "rejected_count": 0,
        "superseded_count": 0,
        "last_updated_at": "ISO8601 timestamp | null"
      }
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
  "continuity": {
    "policy": "designated | none_accepted",
    "declared_by": "steward_id",
    "declared_at": "ISO8601 timestamp",
    "continuity_ref": "string — Memory record for the continuity plan | null",
    "backups": [
      {
        "kind": "human | agent",
        "steward_id": "string",
        "order": 1,
        "function_scope": ["string — implementation-defined function labels"],
        "activation": {
          "mode": "explicit | timeout",
          "timeout_window": "ISO8601 duration | null — REQUIRED when mode: timeout",
          "declared_by": "steward_id",
          "declared_at": "ISO8601 timestamp"
        },
        "scope_on_activation": ["read", "recommend", "notify", "act"],
        "agent_fc_ref": "string — REQUIRED when kind: agent; the standing FiduciaryContext bounding the agent during continuity operation",
        "failure_triggers": {
          "liveness": {
            "heartbeat_interval": "ISO8601 duration",
            "misses_to_unavailable": 2
          },
          "escalation_patterns": [
            { "reason": "tool_failure", "count": 3, "window": "P1D" }
          ]
        }
      }
    ]
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

### 3.3 Delegate Track Record *(added v1.1.0, optional)*

A `delegation_chain` entry MAY carry a `track_record` object summarizing that delegate's
history of accepted, rejected, and superseded outcomes, derived from the `outcome` field of its
own TENURE Records (§6.1).

- **TR-01 (optional):** If present, `track_record` counts MUST be derived only from this
  delegate's own TENURE Record outcomes within this FiduciaryContext.
- **TR-02 (optional):** `track_record` MUST NOT be used as the sole basis for changing
  `max_action_tier` or any other constraint without a corresponding Recommendation and Rationale
  — i.e., a track record MAY inform a steward's decision to widen or narrow a delegate's scope,
  but MUST NOT silently and automatically change `constraints` on its own.
- This subsection is explicitly non-normative for conformance at any level (L0–L3) in v1.1.0.
  It names a real, recurring implementation need — using a delegate's history to inform trust —
  without yet specifying how that history should affect autonomy. A future MAJOR or MINOR
  version may formalize `track_record` as an input to tier policy once more implementations have
  produced evidence on how to do so safely.

### 3.4 Continuity *(added v1.2.0)*

A FiduciaryContext MAY declare a `continuity` block designating what happens when a
steward in its delegation chain becomes `limited` or `unavailable` (QSM-ARCH §6.2.1).
Continuity transfers *operation*, never fiduciary responsibility: responsibility
remains with the human steward of record throughout.

- **CONT-01:** `continuity` is OPTIONAL. Its absence means continuity is
  *undeclared* — implementations SHOULD surface undeclared continuity on an active
  FiduciaryContext as a Tier 1 Recommendation. Absence MUST NOT be interpreted as
  `none_accepted`.
- **CONT-02:** `policy: none_accepted` is a valid, conformant state: an explicit,
  recorded decision to operate without a backup. It MUST carry `declared_by` and
  `declared_at`.
- **CONT-03:** Every entry in `backups` MUST declare `kind` (`human` or `agent`).
- **CONT-04:** Every continuity activation — either mode, either kind — MUST
  produce a TENURE entry (`entry_type: continuity_event`, §6.1) recording who or
  what activated, under which trigger, and with what scope.
- **CONT-05:** A backup's authority on activation is `scope_on_activation`
  intersected with the FiduciaryContext's `constraints`. Activation MUST NOT raise
  `max_action_tier` or widen any constraint beyond what was declared before the
  triggering availability change.
- **CONT-06:** Human-kind backups activate per QSM-ARCH §6.2.2: `explicit` by
  default; `timeout` only where pre-declared with an explicit window by the steward
  it applies to.
- **CONT-07:** An agent-kind backup MUST reference, via `agent_fc_ref`, a standing
  FiduciaryContext declared in advance by a human steward. That context's
  constraints — including `max_action_tier` — bound the agent during continuity
  operation, SHOULD default to the agent's normal operating tier, MAY exceed it
  only where the human steward pre-declared the wider grant, and MUST NOT be
  computed or raised at activation time.
- **CONT-08:** An agent-kind backup's availability uses the same states as any
  steward (QSM-ARCH §6.2.1), but transitions MAY additionally be *detected*: the
  agent MUST be treated as `unavailable` when it fails its declared liveness checks
  or matches a declared `escalation_patterns` trigger. On agent unavailability,
  activation passes to the next `order` in `backups`.
- **CONT-09:** In any FiduciaryContext that declares an agent-kind backup, at least
  one human steward MUST hold `role: primary` in `delegation_chain` (see PROHIB-07
  for the activation-conflict rule).

#### 3.4.1 Reference example A: human backup chain (CHARTER, Excentropy)

Non-normative. Encodes Part C answer 1 — primary steward with two function-split backups. Code labels only; engagement referenced as `818A`.

```json
{
  "id": "fc-charter-excentropy-001",
  "version": "1.1",
  "context_type": "CHARTER",
  "label": "Excentropy — Consulting Practice Stewardship Context",
  "declared_by": {
    "steward_id": "person_caitlin",
    "steward_name": "Primary Steward",
    "declared_at": "2026-07-06T00:00:00Z"
  },
  "delegation_chain": [
    {
      "steward_id": "person_caitlin",
      "role": "primary",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "act", "delegate"],
      "availability": "available"
    },
    {
      "steward_id": "person_james",
      "role": "delegate",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "notify", "act"],
      "availability": "available"
    }
  ],
  "constraints": {
    "max_action_tier": 3,
    "require_human_approval_above_tier": 2,
    "spending_limit_usd": null,
    "notification_required_for": ["tier-2-actions", "entity-state-changes"],
    "prohibited_domains": []
  },
  "continuity": {
    "policy": "designated",
    "declared_by": "person_caitlin",
    "declared_at": "2026-07-06T00:00:00Z",
    "continuity_ref": "mem-continuity-plan-excentropy",
    "backups": [
      {
        "kind": "human",
        "steward_id": "person_henry",
        "order": 1,
        "function_scope": ["on-site"],
        "activation": {
          "mode": "explicit",
          "timeout_window": null,
          "declared_by": "person_caitlin",
          "declared_at": "2026-07-06T00:00:00Z"
        },
        "scope_on_activation": ["read", "recommend", "notify", "act"]
      },
      {
        "kind": "human",
        "steward_id": "person_marie",
        "order": 1,
        "function_scope": ["admin"],
        "activation": {
          "mode": "explicit",
          "timeout_window": null,
          "declared_by": "person_caitlin",
          "declared_at": "2026-07-06T00:00:00Z"
        },
        "scope_on_activation": ["read", "recommend", "notify"]
      }
    ]
  },
  "status": "active",
  "expires_at": null
}
```

Both backups share `order: 1` because they activate together, split by function — the on-site/admin split from Part C, not a seniority ladder. Obligation-level continuity for the delegate function (James's on-site work → Caitlin order 1, Henry order 2) rides the ARCH Ownership plane (§2.5 above) and composes with this FC-level block.

#### 3.4.2 Reference example B: agentic-primary continuity (CHARTER, Cinderlit)

Non-normative. Encodes Part C answer 2 — agent as primary continuity mechanism, human fallback only if the agentic layer itself fails. Household co-steward stays role-labeled per naming convention.

```json
{
  "id": "fc-charter-cinderlit-001",
  "version": "1.1",
  "context_type": "CHARTER",
  "label": "Cinderlit — Umbrella Stewardship Context",
  "declared_by": {
    "steward_id": "person_caitlin",
    "steward_name": "Primary Steward",
    "declared_at": "2026-07-06T00:00:00Z"
  },
  "delegation_chain": [
    {
      "steward_id": "person_caitlin",
      "role": "primary",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "act", "delegate"],
      "availability": "available"
    },
    {
      "steward_id": "agent_cos_cinderlit",
      "role": "delegate",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "notify"],
      "availability": "available"
    }
  ],
  "constraints": {
    "max_action_tier": 1,
    "require_human_approval_above_tier": 1,
    "spending_limit_usd": null,
    "notification_required_for": ["tier-2-actions", "entity-state-changes"],
    "prohibited_domains": []
  },
  "continuity": {
    "policy": "designated",
    "declared_by": "person_caitlin",
    "declared_at": "2026-07-06T00:00:00Z",
    "continuity_ref": "mem-continuity-plan-cinderlit",
    "backups": [
      {
        "kind": "agent",
        "steward_id": "agent_cos_cinderlit",
        "order": 1,
        "function_scope": null,
        "activation": {
          "mode": "timeout",
          "timeout_window": "P7D",
          "declared_by": "person_caitlin",
          "declared_at": "2026-07-06T00:00:00Z"
        },
        "scope_on_activation": ["read", "recommend", "notify", "act"],
        "agent_fc_ref": "fc-cinderlit-continuity-001",
        "failure_triggers": {
          "liveness": {
            "heartbeat_interval": "P1D",
            "misses_to_unavailable": 2
          },
          "escalation_patterns": [
            { "reason": "tool_failure", "count": 3, "window": "P1D" },
            { "reason": "uncertain_decision", "count": 5, "window": "P1D" }
          ]
        }
      },
      {
        "kind": "human",
        "steward_id": "person_household_costeward",
        "order": 2,
        "function_scope": null,
        "activation": {
          "mode": "explicit",
          "timeout_window": null,
          "declared_by": "person_caitlin",
          "declared_at": "2026-07-06T00:00:00Z"
        },
        "scope_on_activation": ["read", "recommend", "notify", "act"]
      }
    ]
  },
  "status": "active",
  "expires_at": null
}
```

And the standing continuity FC the agent activates into (the CONT-07 bounded context — note the pre-declared tier is *wider* than the agent's day-to-day Tier 1, because Caitlin granted it in advance; it is still narrower than what a human backup receives):

```json
{
  "id": "fc-cinderlit-continuity-001",
  "version": "1.1",
  "context_type": "CHARTER",
  "label": "Cinderlit — Agent Continuity Context (standing, activates per CONT-07)",
  "declared_by": {
    "steward_id": "person_caitlin",
    "steward_name": "Primary Steward",
    "declared_at": "2026-07-06T00:00:00Z"
  },
  "delegation_chain": [
    {
      "steward_id": "person_caitlin",
      "role": "primary",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "act", "delegate"]
    },
    {
      "steward_id": "agent_cos_cinderlit",
      "role": "delegate",
      "authorized_at": "2026-07-06T00:00:00Z",
      "scope": ["read", "recommend", "notify", "act"]
    }
  ],
  "constraints": {
    "max_action_tier": 2,
    "require_human_approval_above_tier": 2,
    "spending_limit_usd": 5,
    "notification_required_for": ["tier-2-actions", "entity-state-changes", "critical-urgency"],
    "prohibited_domains": ["financial-commitments-new"]
  },
  "status": "suspended",
  "expires_at": null
}
```

The standing FC sits `suspended` until continuity activation flips it `active` (recorded per CONT-04); on human return it re-suspends. `spending_limit_usd` is set to **$5** (Caitlin, 2026-07-06) — a nominal ceiling, not an operating budget; per PROHIB-04 the agent can execute financial transactions only within that limit while operating under this FC, and any actual spending need surfaces as a Tier 2 escalation to the human fallback rather than being expected to clear on its own. The human fallback (order 2) fires through CONT-08: two missed daily heartbeats or a matched escalation pattern marks the agent `unavailable`, and the household co-steward is next in the chain.

---

## 4. Action Tiers

QSM-FAI defines a five-tier action model (Tiers 0–4). Tier determines whether an agent may act autonomously,
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

### 4.2 Escalation Taxonomy *(added v1.1.0)*

`requires_escalation: true` alone does not say *why* an agent could not resolve something on its
own, which matters both for the steward reviewing it and for any pattern-detection layer
watching for systemic issues. An agent MUST classify every escalation under one of the following
reasons:

| Reason | Description |
|---|---|
| `uncertain_decision` | The agent lacks sufficient information to choose an action or approach with confidence |
| `scope_violation` | The needed action falls outside the agent's declared delegation scope |
| `rule_conflict` | Two or more applicable decision rules or policies point in different directions |
| `timeout_exceeded` | A task or action was not completed within its expected window (implementations commonly use a multiplier of the expected duration, e.g. 2×, as the threshold) |
| `tool_failure` | An external tool or system the agent depends on returned an error or unexpected result |
| `concurrent_write_risk` | The agent is about to write to a record or file that another agent or process may also be writing to |
| `steward_unavailable` *(added v1.2.0)* | A steward in the delegation chain (or the steward of a referenced object) has become `limited` or `unavailable` and continuity handling requires attention |

- **ESC-01:** Every escalation MUST be classified under exactly one reason from the table above,
  or under an implementation-declared extension (see ESC-04).
- **ESC-02:** A `rule_conflict` escalation MUST record the conflicting rule identifiers or
  sources in the TENURE entry (see `escalation_reason` in §6.1).
- **ESC-03:** A `scope_violation` escalation MUST record the scope that was required and the
  scope the agent actually held.
- **ESC-04:** Implementations MAY define additional escalation reasons beyond this table, but
  per TSS-CONF-05 SHOULD declare them as deviations in their conformance claim.

### 4.3 Escalation Outbox *(added v1.1.0)*

A conformant implementation SHOULD maintain a standing, queryable collection of unresolved
escalations — an **Escalation Outbox** — rather than leaving each implementation to invent its
own ad hoc holding area for "things waiting on a human."

- **EO-01:** Each Escalation Outbox entry MUST reference the TENURE entry that generated it.
- **EO-02:** Each entry MUST carry a `status`: `awaiting_human_review`, `awaiting_approval`,
  `awaiting_authority`, or `resolved`.
- **EO-03:** A resolved entry MUST record its resolution and MUST NOT be deleted — resolution is
  a status change, not a removal (consistent with TSS-REC-05).
- **EO-04:** The Escalation Outbox MAY be implemented as a materialized view over TENURE Records
  filtered to `entry_type: escalation` rather than as a separate data store, provided it
  satisfies EO-01 through EO-03.

See `schemas/escalation-outbox-entry.schema.json` for a reference schema.

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
    "entry_type": "action | recommendation | escalation | notification | read | continuity_event",
    "action_tier": "0 | 1 | 2 | 3 | 4 | null",
    "escalation_reason": "uncertain_decision | scope_violation | rule_conflict | timeout_exceeded | tool_failure | concurrent_write_risk | steward_unavailable | string | null",
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

`continuity_event` *(added v1.2.0)* records a continuity activation or deactivation
per CONT-04; it MUST reference the availability transition or failure trigger that
caused it.

`escalation_reason` is present only when `entry_type: escalation`; it MUST be one of the
Escalation Taxonomy values in §4.2 or an implementation-declared extension string.

`action_tier` *(added v1.3.0)* is the Action Tier (§4) at which the logged action,
recommendation, or escalation was executed or proposed. It is OPTIONAL, but SHOULD
be populated when `entry_type` is `action`, `recommendation`, or `escalation`, so
that audit queries by tier ("all Tier 3 actions by agent X") require no join.
`urgency` deliberately remains on the Rationale object (§5.1) and MUST NOT be
duplicated onto TENURE entries: TEN-02 makes entries append-only, so a mis-copied
urgency could never be corrected. Implementations wanting urgency-filtered queries
SHOULD inline the rationale object (permitted by `rationale_ref`) and index it.

### 6.2 TENURE Conformance Rules

- **TEN-01:** Every agent output MUST produce at least one TENURE entry.
- **TEN-02:** TENURE Records are append-only; prior entries MUST NOT be modified or deleted.
- **TEN-03:** `outcome` MUST be updated when a steward accepts or rejects a recommendation.
- **TEN-04:** TENURE logs MUST be exportable in JSON and human-readable formats.
- **TEN-05:** TENURE Records MUST conform to TSS Record schema and rules (TSS-REC-01 through
  TSS-REC-05). QSM-FAI L-levels map to TSS T-levels as shown in Appendix Z of TSS v1.2.0;
  L2 typically aligns with T2.
- **TEN-06 *(added v1.1.0):*** `entry_type` MAY be extended with implementation-specific values
  beyond `action | recommendation | escalation | notification | read` (for example, values used
  internally for pattern-detection bookkeeping), provided the extension is declared in the
  implementation's conformance manifest and each extended value still satisfies TSS-REC-01
  through TSS-REC-05.

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
  "continuity": {
    "policy": "none_accepted",
    "declared_by": "steward-001",
    "declared_at": "2026-07-06T00:00:00Z",
    "continuity_ref": null,
    "backups": []
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
- **PROHIB-06 *(added v1.1.0):*** Hold or act under a FiduciaryContext whose `context_type` is
  `QSM_META` (QSM §6.1). QSM_META represents the governance/ontology layer itself, not a
  stewarded entity, and per QSM-META-01 MUST NOT be treated as an actionable Entity Set.
- **PROHIB-07 *(added v1.2.0):*** Declare, authorize, or effect the availability
  transition of a human steward where that transition activates the agent's own
  continuity authority — except under a `timeout` activation the affected human
  steward pre-declared with explicit parameters (window and scope). On any timeout
  activation the agent MUST, as its first act, issue a Tier 2 notification to every
  human steward in the delegation chain and create an Escalation Outbox entry
  (`status: awaiting_human_review`, reason `steward_unavailable`).

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
- [ ] Escalations are classified under the Escalation Taxonomy (§4.2) or a declared extension
- [ ] Agent does not act under a QSM_META FiduciaryContext (PROHIB-06)
- [ ] Continuity state on active FiduciaryContexts is declared (`designated` or `none_accepted`), or its absence is surfaced as a Tier 1 recommendation (CONT-01)
- [ ] Agent-kind backups reference a standing, human-pre-declared FiduciaryContext and never gain authority from their own availability determination (CONT-07, PROHIB-07)

---

## Appendix B: Relationship to Other QSM Documents

| Document | Role |
|----------|------|
| **QSM v1.1.0** | Core ontology and modeling framework; QSM-FAI is a dependent spec |
| **TSS v1.2.0** | The Stewardship Standard; normative open standard QSM-FAI implements |
| **THRIVE v1.1.0** | Human wellness and Self context layer; informs occupant need modeling in HEARTH |
| **QSM-ARCH v1.2.0** | Layer and engine operating model; steward availability and continuity designation |
| **QSM-FAI v1.2.0** | This document |

---

*QSM-FAI v1.2.0 — Quantified Stewardship Model: Fiduciary AI Interface*
*© 2026 Caitlin Stokes / Cinderlit — CC BY 4.0*
*First published: 2026-05-28 · Amended: 2026-07-06*
