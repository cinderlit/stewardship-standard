# Changelog

All notable changes to The Stewardship Standard are documented here. This
project follows [Semantic Versioning](https://semver.org). Each constituent
spec is versioned independently; this changelog tracks the combined release
bundle.

## [1.3.0] — 2026-06-25

Methodology release. Extends the framework-declaration pattern (established in [1.1.0] for
needs frameworks) to learning and behavior design; adds decision-confidence fields to the record
schema; adds FiduciaryContext samples for SELF and CHARTER contexts; introduces the conformance
test suite.

### Specifications added
- **QSM v1.2.0** — adds SDT as a recommended needs framework for CHARTER contexts (§4.2.1);
  adds learning-framework mechanism §4.2.2 and Appendix H with rules QSM-LF-01 through
  QSM-LF-03. Supersedes QSM v1.1.0.

### Reference schemas updated
- **context.schema.json** (v1.3) — added `learning_framework` field (QSM-LF-01); updated
  `needs_framework` description to include 'sdt'.
- **record.schema.json** (v1.2) — added optional decision-confidence fields:
  `decision_confidence` (0–1 probability at decision time), `expected_outcome`,
  `actual_outcome`, `outcome_assessed_at`. Apply to decision-type records only; never required.
- **thrive/routine.schema.json** (v1.1) — added optional `behavior_design` object with `cue`,
  `cue_type`, `reward`, `implementation_intention`, `anchor_routine_id`.

### Samples added
- `samples/self-fiduciary-context.json` — FiduciaryContext for a SELF context; T2 scope.
- `samples/charter-fiduciary-context.json` — FiduciaryContext for a CHARTER context with
  spending limit.

### Conformance suite added
- `tests/` — schema validation harness (validates all samples against their schemas) and
  named-rule assertions for FC-01/04, TEN-01/02, QSM-NF-01, THRIVE-02. See `tests/README.md`.
- `.github/workflows/conformance.yml` — CI that runs the harness on every PR.

## [1.2.0] — 2026-06-25

Architecture release. Adds **QSM-ARCH v1.1.0**, the Layer and Engine Operating Model, formalizing
the eight-layer architecture (Intent, Governance, Intake, Memory, Practice, Observation, Signal,
Adaptation) that supersedes the earlier six-layer process-stack vocabulary. This release is
additive to the doctrine and methodology specs — all prior v1.x conformance claims remain valid.

### Specifications added
- **QSM-ARCH v1.1.0** — eight structural layers each defined by a full per-layer contract
  (definition, owns, must-never-own, delegates-to, required artifacts, allowed/prohibited
  dependencies, anti-patterns); five cross-cutting planes; **context lifecycle** (§6.6, with rules
  ARCH-07/08) and **conformance-scale reconciliation** with QSM/TSS (§8.3); the Memory layer
  clarified as authoritative only for persistent, intentional knowledge (ephemeral state lives in
  Observation, derived views in Signal). Supersedes the v1.0.0 draft.
- **QSM-GLOSSARY v1.0.0** — canonical vocabulary reference (28 terms, alphabetical).

### Specifications updated
- **QSM-LAYER-MATRIX** — Memory authoritative-record rule clarified for persistent intentional
  knowledge; the Intent→Governance rule reworded from an absolute to a conditional SHOULD.
- **THRIVE v1.1.0** — WorldDomainScope, IdentityIntentProfile, DevelopmentalContext,
  TemporalCycleProfile (§6.3–6.6); conformance rules THRIVE-06 through THRIVE-08; level H4.
- **TSS v1.2.0** — context lifecycle cross-ref (§6); governance change classes, deprecation
  policy, release front matter, and conflict resolution taxonomy (§14.1–14.4); Appendix Z.3
  (QSM-ARCH A-levels as separate axis).
- **QSM v1.1.0** — Max-Neef as default SELF needs framework; Appendix G (needs frameworks per
  context).

The superseded `QSM-ARCH-v1.0.md` remains in `specs/`, marked superseded with a pointer to its
replacement.

## [1.1.0] — 2026-06-22

Amendment release. Every change in this release is additive — no v1.0.x/v1.1.x requirement
was removed or tightened, so all v1.0.0 conformance claims remain valid under v1.1.0. Use case
and implementation evidence for this entire release: Org-estra, a multi-context stewardship
implementation (SELF, HEARTH, and CHARTER/Excentropy contexts running concurrently) built
directly against the v1.0.0 stack, proposed as a second reference implementation alongside
HEARTH for multi-context, template/instance, and governance-engine material.

### Specifications updated
- **QSM v1.1.0** (was 1.0.1) — added the `QSM_META` context type (§6.1); formalized the Context
  template/instance pattern (§6.2, `is_template`/`template_id`); named the needs-framework
  selection mechanism and reference scoring formula (§4.2.1: Maslow/ERG/Pink/WELL); clarified the
  CREST-vs-ESTATE boundary (§6.1).
- **TSS v1.2.0** (was 1.1.1) — added **Assignment** as a required object wherever Role-based
  delegation is supported, with named delegation models RACI/DACI/MOCHA/unstructured (§5.12);
  formalized the **LOCUS → ATLAS → TENURE** stewardship-phase lifecycle as a Context property
  with gating rules (§6.2); confirmed that an audit trail MAY be composed of multiple linked
  Record subtypes (§9.1); added `is_template`, `template_id`, `needs_framework`, and
  `stewardship_phase` to the Context schema and relaxed `stewards` to accept a single reference
  or an array (§11.1.1).
- **THRIVE v1.1.0** (was 1.0.1) — cross-referenced QSM §4.2.1's needs frameworks from the
  Capacity and Load Model (§7.1.1), aligning THRIVE's capacity dimensions with the framework
  (commonly Maslow) that a SELF context declares.
- **QSM-FAI v1.1.0** (was 1.0.1) — formalized the `requires_escalation` flag into a named
  Escalation Taxonomy (§4.2: `uncertain_decision`, `scope_violation`, `rule_conflict`,
  `timeout_exceeded`, `tool_failure`, `concurrent_write_risk`) and a standing Escalation Outbox
  pattern (§4.3); added an optional Delegate Track Record to `delegation_chain` entries (§3.3,
  explicitly non-normative); noted that TENURE `entry_type` is extensible (§6.1, TEN-06); added
  PROHIB-06 excluding QSM_META governance contexts from agent action.

Superseded versions remain in `specs/` for reference, each marked superseded with a pointer to
its replacement: `QSM-v1.0.1.md`, `TSS-v1.1.1.md`, `THRIVE-v1.0.1.md`, `QSM-FAI-v1.0.1.md`.

### Reference schemas
- Added: `assignment.schema.json` (TSS), `escalation-outbox-entry.schema.json` (QSM-FAI).
- Changed: `context.schema.json` — added `is_template`, `template_id`, `needs_framework`,
  `stewardship_phase`; relaxed `stewards` to `oneOf` array or string; added `QSM_META` to the
  `type` enum. `tenure-entry.schema.json` — annotated `entry_type` as extensible; added optional
  `escalation_reason`.

### Samples
- Added: `charter-template-and-instance.json` (demonstrates §6.2 of QSM v1.1.0), 
  `escalation-outbox-entry.json` (demonstrates §4.3 of QSM-FAI v1.1.0).

### Notes
- This release keeps every change additive (new optional fields, new enum values, new optional
  or conditionally-required objects) — a MINOR bump across all four specs, not a MAJOR one, per
  each spec's own versioning rules (`GOVERNANCE.md`).
- HEARTH remains the first hardened context and primary reference implementation; Org-estra is
  added as a second reference implementation specifically for multi-context,
  template/instance, and governance-engine material that HEARTH alone doesn't exercise.
- Two items raised during this amendment cycle were explicitly deferred rather than included:
  capacity-aware FiduciaryContext constraints and joy/friction as a routing signal both need a
  second independent implementation's evidence before being proposed normatively.

[1.1.0]: https://github.com/cinderlit/stewardship-standard/releases/tag/v1.1.0

## [1.0.0] — 2026-05-28

Initial public release of the four-document stewardship stack.

### Specifications included
- **QSM v1.0.1** — Quantified Stewardship Model: domain-agnostic ontology and methodology.
- **TSS v1.1.1** — The Stewardship Standard: normative umbrella, conformance levels (T0–T3), records, and audit rules.
- **THRIVE v1.0.1** — Self and Wellness Context Layer.
- **QSM-FAI v1.0.1** — Fiduciary AI Interface: FiduciaryContext, action tiers, rationale, and TENURE audit records.

### Reference schemas
- TSS core: `context`, `entity`, `relationship`, `record`, `conformance-claim`.
- QSM-FAI: `fiduciary-context`, `rationale`, `tenure-entry`.
- THRIVE: `self-context`, `capacity-profile`, `need`, `routine`, `wellness-record`.

### Samples
- `hearth-context.json`, `hearth-fiduciary-context.json`, `default-conformance-claim.json`.

### Notes
- HEARTH (the Quantified Home) is the first hardened context and the normative reference implementation.
- TSS T-level is established as the primary audit standard; QSM C-level, THRIVE H-level, and QSM-FAI L-level are domain interpretations of the same conformance tier (TSS Appendix Z).
- Specification text licensed under CC BY 4.0; reference schemas under Apache 2.0.
- Each specification carries front matter for Status of This Document, Use of AI-Assisted Tools, and Openness and Governance. A canonical AI-use disclosure is provided in `AI-USE.md`.

[1.0.0]: https://github.com/cinderlit/stewardship-standard/releases/tag/v1.0.0
