# Architecture Decision Records

Numbered, durable records of significant operating/tooling decisions in Stewardship Standard. ADRs capture the *why* and the forces at play so a decision isn't relitigated six months later. Lightweight one-line decisions still go in `cos-os/DECISIONS.md`; ADRs are for decisions with real trade-offs worth preserving.

**Relationship to other decision surfaces:**
- `.governance/DECISIONS.md` — chronological decision log scoped to this repo.
- QSM-ARCH spec and `CHANGELOG.md` — normative layer definitions this ADR interprets.

| ADR | Title | Status | Date |
|-----|-------|--------|------|
| [0001](ADR-0001-layer-naming-l4-l5-l8.md) | Layer Naming — Memory / Practice / Adaptation (L4, L5, L8) | Accepted | 2026-06-30 |

**Naming:** `ADR-NNNN-kebab-title.md`, zero-padded, monotonic. Supersede rather than delete — mark the old one `Superseded by ADR-NNNN` and keep it.

## Standard (enforced)

Every ADR must have:

- **Frontmatter fields** (as `**Field:**` lines, in this order): `Status`, `Date`, `Deciders`, `Related` (optional but expected). `Amendments` is optional, used when a signed-off ADR gets a later addition — link/summarize it there, never append it to Status.
- **Status** is exactly one of `Proposed | Accepted | Superseded | Deprecated` — no parentheticals, no free text. If it's Superseded, the body must contain the literal string `Superseded by ADR-NNNN`.
- **Required sections**, in order: `Context`, `Decision`, `Options Considered`, `Trade-off Analysis`, `Consequences`, `Action Items`. A section header may carry a parenthetical qualifier for a not-yet-accepted ADR (e.g. `## Decision (proposed — not yet accepted)`) — the canonical name must still be the prefix. Extra sections (e.g. `Open Questions` on a Proposed ADR) are fine in addition to, not instead of, the required six.
- **This README's table stays in sync** with every file's actual Status and Date — that's the #1 source of "which one is current" confusion when it drifts.

Run `node .governance/check-adrs.mjs --dir .governance/adr` before marking any ADR Accepted or committing a change to this table — it checks all of the above (numbering, required fields, status enum, required sections, README-vs-file sync) and exits non-zero on any violation. See `governance-preamble.md` DO rule 7.

**Optional decision-science sections (added 2026-07-02, not lint-enforced):** `template.md` also carries `Knowns and Unknowns`, `Pre-mortem` (with kill criteria), `Post-Decision Monitoring`, and `Decision Review / Calibration` sections, plus optional `Confidence`/`Review Date` header fields — adapted from Annie Duke's decision-quality framing (separate process quality from outcome quality; make uncertainty, kill criteria, and calibration checkpoints explicit). Use them for high-stakes or genuinely uncertain decisions; skip them for routine ones. `check-adrs.mjs` does not require these — only the original six sections are enforced, so existing ADRs written before this addition are still fully compliant.
