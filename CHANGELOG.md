# Changelog

All notable changes to The Stewardship Standard are documented here. This
project follows [Semantic Versioning](https://semver.org). Each constituent
spec is versioned independently; this changelog tracks the combined release
bundle.

## [1.4.1] — 2026-07-25

**This bundle is the first published release to carry [1.3.0] and [1.4.0].** Both were authored
2026-07-06 but never tagged, never released, and never deposited — the last release cut was
**v1.2.0 (2026-06-25)**, which is still what the DOI resolves to. Anyone citing the standard today
receives a version predating QSM-FAI v1.3.0's `action_tier` field entirely. This release closes
that gap; nothing in 1.3.0 or 1.4.0 is changed, only finally shipped.

Cut as a patch rather than tagging 1.4.0 retroactively: dating a tag 2026-07-06 would assert a
publication that never happened. The content of 1.3.0 and 1.4.0 is unchanged and their entries below
keep their original authoring dates.

### Errata

**QSM-FAI §4 — "four-tier" corrected to "five-tier (Tiers 0–4)."** Editorial only; no normative
requirement changed and no conformance claim is affected.

The prose introducing §4 Action Tiers read *"QSM-FAI defines a four-tier action model"* while the
normative table immediately below it listed **five** tiers — `0 Read · 1 Recommend · 2 Notify ·
3 Act · 4 Delegate`. The table was always authoritative, and §4.1 treats Tier 0 as a real point on
the scale (it escalates *to* "Recommendation (Tier 1)" and gates "Tier 3 or Tier 4"), so this was an
off-by-one in the sentence, not an ambiguity about whether Tier 0 counts.

**Present in every published release** — v1.0.1, v1.1.0, v1.2.0, and v1.3.0. Corrected in v1.3.0
only; the earlier files are shipped historical artifacts and are deliberately left as published.
Implementers reading any version should treat the **table** as normative.

Found while reconciling `capacity-envelope-model.md`'s oversight coefficients against this spec
(cinderlit-work-system ADR-0029 AI-6). That reconciliation surfaced a second, larger gap that is
*not* fixed here: **Tier 4 (Delegate) has no oversight cost assigned anywhere** — see the
tier-mapping ADR in cinderlit-work-system.

The spec file itself is **not** version-bumped — the corrected sentence states what the normative
table already required, so QSM-FAI remains **v1.3.0**. Only the bundle takes the patch number.

### Correction to the [1.1.0] change record — QSM-FAI v1.1.0 was **not** purely additive

**The [1.1.0] entry below, and `QSM-FAI-v1.1.0.md`'s own version note, both assert that "no v1.0.1
requirement was removed or tightened, and v1.0.1 conformance claims remain valid under v1.1.0."
That assertion is incorrect.** This entry supersedes it.

**QSM-FAI v1.1.0 §4.2 ESC-01 is a tightening.** It requires every escalation to be classified under
exactly one reason from the escalation taxonomy (or a declared ESC-04 extension). Under v1.0.1 §4.1
an escalating agent was required only to *"attach a `requires_escalation: true` flag"* — there was no
reason taxonomy and no obligation to classify. ESC-01 therefore imposes a **new MUST on behaviour
that already existed and was already conformant**: a v1.0.1-conformant implementation emitting a bare
`requires_escalation: true` is **non-conformant under v1.1.0**. ESC-02 and ESC-03 add further
MUST-record obligations in the same shape.

**A v1.0.1 conformance claim does not automatically carry forward to v1.1.0.** Implementers holding
one should re-read §4.2 and verify their escalation path classifies, rather than relying on the
additivity sentence.

**Checked and cleared, so it is not re-litigated:** PROHIB-06 (v1.1.0 §9) prohibits agents holding a
`QSM_META` FiduciaryContext and reads like a new prohibition, but `QSM_META` was itself introduced in
QSM v1.1.0 §6.1 — no v1.0.1 context could carry that type, so nothing previously conformant could
retroactively violate it. PROHIB-06 **is** genuinely additive. ESC-01 is not, because escalations
existed at v1.0.1 and the spec already mandated them.

**Why the record is corrected here rather than in the v1.1.0 files.** `specs/QSM-FAI-v1.1.0.md` is a
shipped artifact and is deliberately left as published (same rule as the §4 erratum above), so its
inline version note still contains the incorrect sentence. **Where a spec file's own change note and
this CHANGELOG disagree about what changed between versions, this CHANGELOG is authoritative.**

No known implementation is affected: `org-estra-archive`'s v1.0.1 claim was never issued, and
Orgestra was built against v1.1.0 or later. This is a defect in the change record, not a live broken
claim — but the record is what an external implementer relies on to decide whether a re-read is
needed, and one relying on it here would ship a non-conformant escalation path.

*Found by the FAI/TSS tier reconciliation, 2026-07-25, which was instructed to verify the additivity
assertion rather than quote it. The §4 erratum above is why that instruction was given.*

### Release hygiene

- `CITATION.cff` and `.zenodo.json` were both still pinned at **1.2.0**; updated here to 1.4.1.
- The `identifiers` list in `CITATION.cff` carries a version DOI for **v1.0.0 only** — v1.2.0's was
  never added. The concept DOI (`10.5281/zenodo.20436569`) is unchanged and always resolves to the
  latest version. **The v1.4.1 version DOI can only be added after Zenodo deposits it**, so it is
  deliberately absent here rather than guessed.

## [1.4.0] — 2026-07-06

Governance closure spec rider. Adds optional `action_tier` on TENURE entries
(QSM-FAI v1.3.0 §6.1) for tier-filtered audit queries. Declined amendments
(Escalation Outbox SHOULD→MUST; numeric confidence on escalation taxonomy) recorded
with revisit triggers in the bundle notes. All changes additive; all prior
conformance claims remain valid.

### Specifications updated
- **QSM-FAI v1.3.0** (was 1.2.0) — optional `action_tier` on TENURE entries (§6.1).

### Notes
- QSM core (v1.1.0), TSS (v1.2.0), THRIVE (v1.1.0), and QSM-ARCH (v1.2.0) are unchanged in this bundle.
- Superseded: `QSM-FAI-v1.2.0.md` (marked with pointer).

[1.4.0]: https://github.com/cinderlit/stewardship-standard/releases/tag/v1.4.0

## [1.3.0] — 2026-07-06

Steward continuity release. Adds steward availability and continuity designation
(QSM-ARCH v1.2.0 §6.2.1–6.2.2, ARCH-09/10) and the FiduciaryContext Continuity block with
agent-as-backup-steward rules (QSM-FAI v1.2.0 §3.4, PROHIB-07). All changes
additive; all prior conformance claims remain valid.

### Specifications updated
- **QSM-ARCH v1.2.0** (was 1.1.0) — steward availability records (§6.2.1), continuity designation (§6.2.2), availability/lifecycle orthogonality (§6.6), ARCH-09/10.
- **QSM-FAI v1.2.0** (was 1.1.0) — Continuity block (§3.4, CONT-01..09), agent backup rules, `steward_unavailable` escalation, `continuity_event` TENURE type, PROHIB-07.

### Reference schemas
- Added: `fiduciary-context-v1.1.schema.json` — strict superset of v1.0; optional `continuity` block and `delegation_chain[].availability`.

### Notes
- QSM core (v1.1.0), TSS (v1.2.0), and THRIVE (v1.1.0) are unchanged in this bundle.
- Superseded: `QSM-ARCH-v1.1.0.md`, `QSM-FAI-v1.1.0.md` (marked with pointers).

[1.3.0]: https://github.com/cinderlit/stewardship-standard/releases/tag/v1.3.0

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

> **⚠ Corrected 2026-07-25 — see [1.4.1] § *Correction to the [1.1.0] change record*.** The
> additivity sentence immediately below is **incorrect**: QSM-FAI v1.1.0 §4.2 **ESC-01 is a
> tightening**, and a v1.0.1 conformance claim does not automatically carry forward. The [1.4.1]
> entry is authoritative.

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
