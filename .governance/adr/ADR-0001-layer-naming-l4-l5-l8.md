# ADR-0001: Layer Naming — Memory / Practice / Adaptation (L4, L5, L8)

**Status:** Accepted
**Date:** 2026-06-30
**Deciders:** Caitlin
**Related:** QSM-ARCH v1.1.0, `CHANGELOG.md` [1.2.0], superseded location `governance/decisions/ADR-001-layer-naming-L4-L5-L8.md`
**Confidence:** High — each rename is argued per-layer on semantic grounds, not just on spec precedent.
**Review Date:** No fixed date — reopen only if a future standard revision proposes a fourth naming scheme with its own documented trade-offs.

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

## Options Considered

### Option A: Retain Knowledge / Execution / Feedback (legacy v1.0 names)
**Pros:** No migration work; matches older docs and some live UI card titles. **Cons:** Semantic collision between "Knowledge" (L4) and L8's learning domain; "Execution" fits CHARTER poorly for SELF/HEARTH routines; "Feedback" overlaps L6/L7 signal vocabulary; drift already proven across qsm-self and quantifiedly.com.

### Option B: Memory / Practice / Adaptation (v1.1.0 names — chosen)
**Pros:** Resolves L4 vs L8 ambiguity; "Practice" fits recurring SELF/HEARTH rhythms and CHARTER OKR cycles; "Adaptation" names system-level change, not passive input. **Cons:** Requires audit pass on every surface that predates v1.1.0.

### Option C: Mind Over Meta simplified vocabulary as parallel standard
**Pros:** Could reduce jargon on MoM surfaces. **Cons:** MoM glossary does not use L1–L8 names today; inventing a dual vocabulary would add a second naming scheme without existing convention to preserve.

## Knowns and Unknowns

### What we know
- The rename to Memory/Practice/Adaptation already happened at spec level (v1.1.0); drift is empirically documented on two independent surfaces (qsm-self vault, quantifiedly.com).

### What we don't know
- Whether the audit pass (Action Items 1-2) actually gets completed before a third surface is built using the old names.

### What would change our mind
- A future standard revision proposing a fourth naming scheme with its own documented trade-offs — already named as the explicit Revisit condition below.

## Pre-mortem

### Failure modes
- FM-1: The audit pass never completes, and the same "changelog states the rename as fact, nobody executes it" pattern repeats — the exact root cause this ADR diagnosed. Likelihood: medium, since this ADR itself had to be written because a prior rename half-propagated · Impact: medium — confusing public copy, not a functional break · Mitigation: Action Items 1-2, explicit and trackable · Owner: Caitlin/Cursor
- FM-2: A new surface gets built using outdated names copied from an unaudited file before Action Items 1-2 land. Likelihood: medium while those items stay open · Impact: low-medium · Mitigation: none named beyond completing the audit promptly · Owner: whoever builds new layer-referencing content

### Kill criteria
- If old-name drift is found on a third independent surface after this ADR, that's a signal enforcement (a lint check on layer names) is needed, not just a one-time audit.

## Trade-off Analysis

Per-layer, the new names were checked against the old ones on their own merits, not just on
spec precedent:

- **L4 — Memory, not Knowledge.** "Knowledge" collides semantically with L8's domain ("the system
  learns" / Adaptation). A reader scanning eight layer names sees two that both sound like
  "knowing things," with no cue that one is the static record and the other is the
  change-mechanism. "Memory" claims the narrower, more accurate territory — *the persisted
  record* — and frees "knowledge/learning" language to live unambiguously at L8.
- **L5 — Practice, not Execution.** "Execution" is corporate/project vocabulary — it reads as
  "ship the thing once," which fits CHARTER contexts but sits oddly against what this layer
  actually holds for SELF and HEARTH: recurring routines, daily/weekly rhythms, household
  upkeep. "Practice" natively carries sustained, repeated, disciplined activity — the actual
  definition ("the sustained work of stewardship").
- **L8 — Adaptation, not Feedback (or Feedback/Learning).** "Feedback" names an *input* (a
  signal arriving), not what this layer *does* with it — already a source of ambiguity with
  Signal (L7) and Observation (L6). "Learning" is overloaded by ML/AI usage. "Adaptation"
  names the actual mechanism — the system changing how it operates.

Net effect: the rename isn't cosmetic. It resolves real ambiguity and fits cross-context copy
better than the v1.0 vocabulary.

## Consequences

**Easier:** Layer names no longer compete for the same semantic territory; "Memory is
authoritative, Signal and Observation are derivative" reads unambiguously once "Knowledge"
isn't also implying a learning/understanding sense that overlaps L8. Cross-context copy (a
single word that has to describe SELF, HEARTH, and CHARTER alike) fits better under
Practice than Execution.

**Harder:** Every existing implementation, doc, and public page that predates the v1.1.0 rename
needs an audit pass — this ADR exists in part because the first rename wasn't enough to prevent
drift; enforcement has to be active, not assumed.

**Revisit:** Re-open only if a future standard revision proposes a fourth naming scheme with documented trade-offs.

## Action Items

1. [ ] Update `quantifiedly/src/data/layers.js` — card titles for ids 4, 5, 8 still read the old names. Confirmed still open 2026-07-02 (live fetch of quantifiedly.com shows the model page's layer cards labeled Knowledge/Execution/Feedback & Learning while body copy already uses the correct names). This is application source code — Cursor job, not a doc fix.
2. [x] Update `cinderlit-work-system/work-system/qsm-mapping.md` — cross-context mapping doc still headed with legacy names. **Verified done 2026-07-02** — file already reads "L4 · Memory," "L5 · Practice," "L8 · Adaptation" throughout. Checkbox was stale; no further action needed.
3. [ ] Mind Over Meta — adopt Memory / Practice / Adaptation if/when it adopts L1–L8 layer language. Still N/A as of 2026-07-02 — mindovermeta.com's live site uses its own Plan/Measure/Review/Adjust framing, not L1–L8 names.

## Post-Decision Monitoring

### Success signals
- Action Items 1-2 completed; no further surfaces found using legacy names.

### Guardrail signals
- Any new instance of "Knowledge"/"Execution"/"Feedback" as a displayed layer name found after this ADR.

### Review cadence
- No fixed date — only if a fourth naming scheme is proposed.

## Decision Review / Calibration

Not yet reached — Action Items 1-2 are still open as of this writing.
