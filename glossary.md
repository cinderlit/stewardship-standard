# Glossary

A consolidated reference of normative terms used across The Stewardship
Standard stack. Where a term is defined by a specific spec, the source is
noted. In case of conflict, the cited spec governs.

| Term | Definition | Source |
|------|-----------|--------|
| **Action** | A change to state, schedule, responsibility, or communication; any agent output that modifies entity state, schedules work, or triggers a notification. | TSS, QSM-FAI |
| **Agent** | Any AI system operating under QSM-FAI; must hold a valid FiduciaryContext before acting. | QSM-FAI |
| **Assignment** | A binding between a Role or Responsibility and the Steward(s)/Delegate(s) who hold it, under a named delegation model (RACI, DACI, MOCHA, or unstructured). *Added v1.2.0.* | TSS |
| **Capacity** | The amount of effective effort, attention, or resilience available to a Self at a given time. | THRIVE |
| **Conformance** | Demonstrated adherence to the rules of the standard, declared explicitly and versioned. | TSS |
| **ConformanceClaim** | A versioned statement of the TSS version, context types, and conformance level an implementation claims. | TSS |
| **Constraint** | A limit on time, energy, access, money, health, or attention. | THRIVE |
| **Context** | A bounded stewardship domain with explicit scope and participants. | QSM, TSS |
| **Delegate** | A human or agent acting under authorized scope. | TSS |
| **Delegation Chain** | The ordered list of stewards/agents who have authorized an agent to act. Must include at least one primary steward. | QSM-FAI |
| **Dependency** | A relationship in which one entity relies on another. | QSM |
| **Entity** | Any person, place, system, asset, obligation, or meaningful object in scope. | QSM, TSS |
| **Entity Set** | The bounded collection of people, places, systems, and relationships within a context. | QSM-FAI |
| **Escalation Outbox** | A standing, queryable collection of unresolved escalations awaiting steward attention, classified under the Escalation Taxonomy. *Added v1.1.0.* | QSM-FAI |
| **Fiduciary Context (FC)** | A formally declared stewardship scope and an agent's "license to act"; required before any agent may act. | QSM-FAI |
| **Fiduciary Duty** | The legal and ethical obligations of care, loyalty, and disclosure owed by an agent to a principal. | QSM-FAI |
| **Hardened Context** | A context with a fully populated LOCUS, a validated ATLAS, and at least one TENURE cycle. HEARTH is the first. | QSM-FAI |
| **HEARTH** | The Quantified Home context; the first hardened context and the normative reference implementation for the stack. | QSM-FAI, TSS |
| **Load** | The total burden of obligations, tasks, and emotional or cognitive demand on a Self. | THRIVE |
| **Need** | A condition required for stability, flourishing, wellbeing, or safe operation. | QSM, TSS, THRIVE |
| **Principal / Steward** | The person or entity with declared responsibility for an Entity Set; the party on whose behalf an agent acts. | QSM, TSS, QSM-FAI |
| **Rationale** | A machine-readable justification linking an action or recommendation to one or more QSM model elements. | QSM-FAI |
| **Recommendation** | An agent output that proposes but does not execute an action. | QSM-FAI |
| **Record** | An append-only auditable entry describing a stewardship event. Domain variants: StewardshipRecord, WellnessRecord, TENURE Record. | TSS |
| **Recovery** | The process of restoring capacity after depletion. | THRIVE |
| **Relationship** | An explicit link between objects (e.g., depends_on, supports, owns). | QSM, TSS |
| **Risk** | A condition that may degrade outcomes or create harm. | QSM, TSS |
| **Role** | A function or responsibility held by an entity or person. | QSM, TSS |
| **Routine** | A recurring structure that stabilizes functioning. | THRIVE |
| **ScenarioPattern** | A reusable contextual template (e.g., wildfire, storm/outage, caregiving week). | QSM, TSS |
| **Self** | The person whose capacity, wellbeing, and responsibilities are being represented. | THRIVE |
| **Stewardship Phase** | A Context's position in the LOCUS → ATLAS → TENURE lifecycle (establishing ground truth → mapping the option space → ongoing maintenance). *Added v1.2.0.* | TSS |
| **Support** | A person, tool, routine, or resource that reduces friction or increases capacity. | THRIVE |
| **Template / Instance** | A template Context (`is_template: true`) holds a non-steward-owned default domain map for its type; an instance duplicates a template under a new steward-owned Context. *Added v1.1.0.* | QSM |
| **TENURE Record** | A timestamped, append-only audit log entry attached to an entity or action; conforms to TSS Record rules. | QSM-FAI |
| **Track Record** | An optional, rolling summary of a delegate's accepted/rejected/superseded outcome history. Non-normative for conformance. *Added v1.1.0.* | QSM-FAI |
| **Value** | A preference or principle used to prioritize actions. | QSM, TSS |

## Context types

| Type | Meaning | Source |
|------|---------|--------|
| **SELF** | Personal wellbeing, executive function, habits, life maintenance (see THRIVE). | QSM, TSS, THRIVE |
| **HEARTH** | Home and household stewardship; first hardened context. | QSM, TSS |
| **ESTATE** | Multi-property or portfolio-scale stewardship. | QSM, TSS |
| **CHARTER** | Organizational governance or leadership context. | QSM, TSS |
| **CREST** | Recurring, seasonal, or episodic responsibility context — distinguished from ESTATE by shape (cyclical/dormant-between-cycles), not scale. | QSM, TSS |
| **QSM_META** | Singleton, non-steward-owned governance context representing the standard/ontology layer itself, not a stewarded entity. Not a valid target for agent action. *Added v1.1.0.* | QSM, TSS, QSM-FAI |

## Conformance levels

TSS T-levels are the primary audit standard; the others are domain interpretations of the same tier (TSS Appendix Z).

| Tier | TSS | QSM | THRIVE | QSM-FAI |
|------|-----|-----|--------|---------|
| Observational / informal | T0 | C0 | H0 | L0 |
| Structured | T1 | C1 | H1 | L1 |
| Operational / auditable | T2 | C2 | H2 | L2 |
| Normative / full | T3 | C3 | H3 | L3 |

## Action tiers (QSM-FAI)

| Tier | Label | Default agent permission |
|------|-------|--------------------------|
| 0 | Read | Always permitted |
| 1 | Recommend | Always permitted; must attach Rationale |
| 2 | Notify | Permitted if in delegation scope |
| 3 | Act | Requires explicit `act` scope |
| 4 | Delegate | Requires `delegate` scope; primary steward only |

## Escalation taxonomy (QSM-FAI, added v1.1.0)

| Reason | Description |
|--------|--------------|
| `uncertain_decision` | Agent lacks sufficient information to choose an action with confidence |
| `scope_violation` | Needed action falls outside the agent's declared delegation scope |
| `rule_conflict` | Two or more applicable rules point in different directions |
| `timeout_exceeded` | A task/action was not completed within its expected window |
| `tool_failure` | An external tool the agent depends on returned an error or unexpected result |
| `concurrent_write_risk` | Agent is about to write to a record another agent/process may also be writing to |
