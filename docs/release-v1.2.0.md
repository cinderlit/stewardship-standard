# Release v1.2.0 — GitHub and Zenodo

Draft release notes and deposit steps for **The Stewardship Standard v1.2.0** (2026-06-25).

## GitHub release

**Tag:** `v1.2.0`  
**Title:** The Stewardship Standard v1.2.0  
**Target:** `main` (after PR merge)

### Release notes (copy into GitHub)

Architecture release. Adds **QSM-ARCH v1.1.0**, the Layer and Engine Operating Model, formalizing the eight-layer architecture (Intent, Governance, Intake, Memory, Practice, Observation, Signal, Adaptation) that supersedes the earlier six-layer process-stack vocabulary. This release is additive to the doctrine and methodology specs — all prior v1.x conformance claims remain valid.

#### Specifications added

- **QSM-ARCH v1.1.0** — eight structural layers each defined by a full per-layer contract (definition, owns, must-never-own, delegates-to, required artifacts, allowed/prohibited dependencies, anti-patterns); five cross-cutting planes; **context lifecycle** (§6.6, with rules ARCH-07/08) and **conformance-scale reconciliation** with QSM/TSS (§8.3); the Memory layer clarified as authoritative only for persistent, intentional knowledge (ephemeral state lives in Observation, derived views in Signal). Supersedes the v1.0.0 draft.
- **QSM-GLOSSARY v1.0.0** — canonical vocabulary reference (28 terms, alphabetical).

#### Specifications updated

- **QSM-LAYER-MATRIX** — Memory authoritative-record rule clarified for persistent intentional knowledge; the Intent→Governance rule reworded from an absolute to a conditional SHOULD.
- **THRIVE v1.1.0** — WorldDomainScope, IdentityIntentProfile, DevelopmentalContext, TemporalCycleProfile (§6.3–6.6); conformance rules THRIVE-06 through THRIVE-08; level H4.
- **TSS v1.2.0** — context lifecycle cross-ref (§6); governance change classes, deprecation policy, release front matter, and conflict resolution taxonomy (§14.1–14.4); Appendix Z.3 (QSM-ARCH A-levels as separate axis).
- **QSM v1.1.0** — Max-Neef as default SELF needs framework; Appendix G (needs frameworks per context).

Full details: [`CHANGELOG.md`](CHANGELOG.md) [1.2.0].

**Concept DOI (always latest):** [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569)

---

## Tag and push (after merge to main)

```bash
git checkout main
git pull origin main
git tag -a v1.2.0 -m "The Stewardship Standard v1.2.0"
git push origin v1.2.0
```

Then publish the GitHub Release from the `v1.2.0` tag using the notes above.

---

## Zenodo deposit (new version)

1. Open the concept record: [zenodo.org/records/20436569](https://zenodo.org/records/20436569)
2. Click **New version** (or use the GitHub–Zenodo integration if enabled for this repo).
3. Confirm metadata from [`.zenodo.json`](../.zenodo.json) (`version: v1.2.0`, `related_identifiers` → `tree/v1.2.0`).
4. Publish the new version. Zenodo mints a **version-specific DOI** for v1.2.0.

### After the v1.2.0 version DOI is minted

1. Add the new version DOI to `CITATION.cff` as the top-level `doi` (keep `10.5281/zenodo.20436569` in `identifiers` as the concept DOI).
2. Optionally add the v1.2.0 version DOI to current-release spec front matter (`specs/*-v1.1.0.md`, `specs/TSS-v1.2.0.md`, `specs/QSM-ARCH-v1.1.0.md`).
3. Update this file with the minted version DOI for reference.

**Current DOI mapping**

| Role | DOI | Record |
|------|-----|--------|
| Concept (latest) | [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569) | [20436569](https://zenodo.org/records/20436569) |
| Version v1.0.0 | [10.5281/zenodo.20436570](https://doi.org/10.5281/zenodo.20436570) | [20436570](https://zenodo.org/records/20436570) |
| Version v1.2.0 | *(pending deposit)* | — |
