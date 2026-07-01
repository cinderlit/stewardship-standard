# ADR-001 — Layer Naming: Memory / Practice / Adaptation (L4, L5, L8)

**Date:** 2026-06-30
**Status:** Accepted

## Context

QSM-ARCH v1.0 (2026-06-25) named the eight layers using vocabulary inherited from an earlier
six-layer process-stack draft, including **Knowledge** (L4), **Execution** (L5), and
**Feedback** (L8). QSM-ARCH v1.1.0, released the same week as part of the v1.2.0 standard
bundle, renamed these three to **Memory**, **Practice**, and **Adaptation** respectively
(`CHANGELOG.md` [1.2.0]; `QSM-GLOSSARY.md` records "Practice ... Formerly called Execution").
No rationale was recorded at the time — the changelog states the rename as fact, not as a
reasoned decision.

The absence of a recorded rationale let the rename go half-propagated. A 2026-06-30 compliance
audit of the `qsm-self` Obsidian vault found L4/L5/L8 headers still reading "Knowledge,"
"Execution," and "Feedback" while the same files' own subtitles already used "Memory,"
"Practice," and "Adapt." The same pattern was then found live on quantifiedly.com: the model
page's card titles (`quantifiedly/src/data/layers.js`, `name: 'Knowledge'` / `'Execution'` /
`'Feedback / Learning'`) still carry the old names, while the body copy on those same cards
("Memory is the system for storing...", "Practice is the sustained work...", "Adaptation is the
layer where the system examines itself...") and the page's layer-dependency and
framework-comparison tables already use only the new names. Two independent surfaces drifted
the same way, which is a sign of a missing decision record, not isolated carelessness.

Separately: Mind Over Meta's glossary (`mind-over-meta-parent/planning/glossary.md`) was checked
as a possible source of an intentional "simplified" vocabulary that Knowledge/Execution/Feedback
might belong to. It isn't — MoM uses its own, unrelated framing (a Plan → Measure → Review →
Adjust cycle; three high-level layers of ontology/needs/roles; "Life Domains") that doesn't
reference the L1–L8 names at all yet. There is no existing dual-vocabulary convention to
preserve.

## Decision

**Memory, Practice, and Adaptation are the sole canonical names for layers 4, 5, and 8**, across
the spec, all reference implementations, and all public-facing copy (Quantifiedly, Mind Over
Meta once it adopts layer language, qsm-self, cinderlit-work-system).

"Knowledge," "Execution," and "Feedback / Learning" are deprecated. They may persist only as
legacy filenames/slugs where renaming isn't immediately feasible (e.g. `qsm-self/L4-Knowledge.md`,
kept for Obsidian link stability pending a manual rename) — never as a displayed layer name, card
title, or heading.

## Rationale

Per-layer, the new names were checked against the old ones on their own merits, not just on
spec precedent:

- **L4 — Memory, not Knowledge.** "Knowledge" collides semantically with L8's domain ("the system
  learns" / Adaptation). A reader scanning eight layer names sees two that both sound like
  "knowing things," with no cue that one is the static record and the other is the
  change-mechanism. "Memory" claims the narrower, more accurate territory — *the persisted
  record* — and frees "knowledge/learning" language to live unambiguously at L8. This matches
  the layer's own contract ("the authoritative record of persistent, intentional knowledge");
  "Memory" names the *mechanism*, "Knowledge" names the *content*, and the layer is more
  precisely the former.
- **L5 — Practice, not Execution.** "Execution" is corporate/project vocabulary — it reads as
  "ship the thing once," which fits CHARTER contexts but sits oddly against what this layer
  actually holds for SELF and HEARTH: recurring routines, daily/weekly rhythms, household
  upkeep. "Practice" (as in "a daily practice," "best practices," "medical practice") natively
  carries the idea of sustained, repeated, disciplined activity — which is the actual definition
  ("the sustained work of stewardship"). It's also the more context-portable word: "Execution"
  sounds wrong applied to a morning routine; "Practice" doesn't sound wrong applied to a
  quarterly business review.
- **L8 — Adaptation, not Feedback (or Feedback/Learning).** "Feedback" names an *input* (a
  signal arriving), not what this layer *does* with it — already a source of ambiguity with
  Signal (L7) and Observation (L6), which also handle incoming information. "Learning" is
  overloaded by ML/AI usage and reads as passive/individual ("a person learning"), not as the
  deliberate, dispatched, system-level change this layer is defined to produce. "Adaptation"
  names the actual mechanism — the system changing how it operates — and pairs cleanly as the
  *output* of feedback rather than competing with it as a synonym for the same noun.

Net effect: the rename isn't cosmetic. It resolves a real ambiguity (Knowledge vs. the
Adaptation layer's "learning"), and for L5 in particular it's a better fit for a model that has
to describe both a CHARTER's quarterly OKR cycle and a SELF's morning routine with the same word.

## Consequences

**Easier:** Layer names no longer compete for the same semantic territory; "Memory is
authoritative, Signal and Observation are derivative" reads unambiguously once "Knowledge"
isn't also implying a learning/understanding sense that overlaps L8. Cross-context copy (a
single word that has to describe SELF, HEARTH, and CHARTER alike) fits better under
Practice than Execution.

**Harder:** Every existing implementation, doc, and public page that predates the v1.1.0 rename
needs an audit pass — this ADR exists in part because the first rename wasn't enough to prevent
drift; enforcement has to be active, not assumed.

**Open follow-ups (tracked outside this ADR):**
- `quantifiedly/src/data/layers.js` — card titles for ids 4, 5, 8 still read the old names.
- `cinderlit-work-system/work-system/qsm-mapping.md` — cross-context mapping doc still headed
  "L4 · Knowledge," "L5 · Execution," "L8 · Feedback / Learning" throughout.
- Mind Over Meta — no action needed yet (doesn't use layer names), but should adopt Memory /
  Practice / Adaptation if/when it does.

*Stewardship Standard — © 2026 Caitlin Stokes / Cinderlit · CC BY 4.0*
