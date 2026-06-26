# QSM Glossary
## Stewardship Stack Vocabulary Reference

**Version:** 1.0.0  
**Status:** Final Draft — Ready for Submission  
**Maintainer:** Caitlin · Excentropy  
**License:** CC BY 4.0  
**Published:** 2026-06-25  
**Dependent Specs:** QSM v1.0, THRIVE v1.1, TSS v1.1, QSM-ARCH v1.0, QSM-FAI v1.0

---

## Abstract

This document is the single source of truth for defined terms used across the stewardship stack. It is **not** a normative specification — it contains no conformance rules. When a term is defined here, all specs SHOULD be considered to inherit that definition rather than redefining it locally.

For normative requirements, see the relevant spec document cited in each entry.

---

## Terms (alphabetical)

**Adaptation** — The layer responsible for changing how a system operates based on accumulated experience. Distinct from Observation, which only senses. (QSM-ARCH)

**Context** — A bounded domain of stewardship — one of five types: SELF, HEARTH, ESTATE, CHARTER, CREST. A context has declared scope, stewards, and a needs framework. (QSM)

**Context type** — One of the five categories of stewardship domain recognized by QSM: SELF, HEARTH, ESTATE, CHARTER, CREST. (QSM)

**Decision** — A recorded choice made within a context, with provenance, rationale, and lifecycle state. Decisions live in the Memory layer. (QSM-ARCH)

**Engine** — A named functional capability within a layer. Engines are what layers do — a layer is defined by the set of engines it contains. (QSM-ARCH)

**Entity** — Any person, place, object, or system that a context has a stewardship relationship with. (QSM)

**Event** — A discrete occurrence captured by the Intake or Observation layers. Events are time-stamped, typed, and classified before being routed. (QSM-ARCH)

**Fundamental human need** — In Max-Neef's taxonomy: one of nine universal, non-hierarchical, simultaneously active needs. The nine needs are: Subsistence, Protection, Affection, Understanding, Participation, Leisure, Creation, Identity, Freedom. Needs are constant; satisfiers vary. (THRIVE)

**Governance** — The layer that defines authority, policy, constraints, review cadence, and escalation paths. Governance SHOULD be grounded in Intent. (QSM-ARCH)

**Intent** — The layer that declares what a context is for, what it values, and what orients its decisions. The first layer in the QSM operating model. (QSM-ARCH)

**Intake** — The layer that captures signals and objects arriving from the world and routes them into the system in a normalized, classified form. (QSM-ARCH)

**Layer** — One of eight structural domains of responsibility in a QSM implementation. Layers partition the operating model into bounded concerns with defined inputs, outputs, and boundaries. (QSM-ARCH)

**Lifecycle state** — The current status of any QSM object: draft, active, suspended, or retired. A cross-cutting plane property required on all objects. (QSM-ARCH)

**Load** — A demand placed on an entity's capacity — a resource draw that reduces available capacity for other demands. (THRIVE)

**Memory** — The layer that holds what the system knows: models, decisions, documentation, and reference truth. The authoritative record for persistent, intentional knowledge. Ephemeral operational state and derived caches do not belong here. (QSM-ARCH)

**Model** — A structured representation of knowledge in the Memory layer — a pattern, schema, or framework used to interpret current state. (QSM-ARCH)

**Need** — <!-- REVIEW: inconsistent usage across QSM and THRIVE --> In QSM: a declared deficit or requirement within a context (TSS §5.4). In Max-Neef's framework as used in THRIVE: one of nine universal fundamental needs that are simultaneous and non-hierarchical. Needs are distinct from satisfiers. (QSM, THRIVE)

**NeedsDimension** — The abstract superclass in the QSM ontology for all needs framework vocabularies. Subclasses include MaxNeefNeed and MaslowTier. (qsm-ontology-v3)

**Observation** — The layer that senses what is happening and what happened. Produces verified states, audit trails, and anomaly flags. Distinct from Adaptation. (QSM-ARCH)

**Practice** — The layer that carries out the sustained work of stewardship — routines, tasks, and interventions that keep the context functioning. Formerly called Execution. (QSM-ARCH)

**Record** — A persisted, time-stamped entry in the Memory layer. Records are the output of documentation and decision-capture processes. (QSM-ARCH)

**Role** — A named function or responsibility assigned to an entity within a context. Roles are declared in the Intent layer. (QSM)

**Satisfier** — A practice, resource, relationship, or structure that addresses a fundamental need. Satisfiers vary across persons and contexts; needs do not. In QSM: management categories are satisfiers. (THRIVE)

**Signal** — The layer that surfaces current state and routes attention to what matters. Signal is always derivative of Memory and Observation — it is never the authoritative record. (QSM-ARCH)

**State** — The current condition of an object, context, or system as observed or recorded at a point in time. State lives in Observation; if deliberately recorded, it is promoted to Memory. (QSM-ARCH)

**Steward** — The person or role responsible for a context or object. Declared via `steward_ref`. (QSM)

**Stewardship** — The active, responsible care for something of value — a person, place, system, relationship, or community — over time. The organizing concept of QSM. (QSM)

**World domain** — One of three arenas of self-stewardship in the SELF context: Physical, Digital, Metaphysical. (THRIVE)

---

*QSM Glossary — maintained by Caitlin · Excentropy*
