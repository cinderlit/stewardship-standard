# Releasing The Stewardship Standard

**Why this file exists:** bundles **1.3.0** and **1.4.0** were authored on 2026-07-06 and never
released. Not tagged, not published, not deposited. The gap went unnoticed for nineteen days, during
which every citation of this standard resolved to **v1.2.0** — a version predating QSM-FAI v1.3.0's
`action_tier` field. Nothing broke. Nothing failed. There was simply no check.

## The invariant

**A CHANGELOG entry is not a release.** The only things the outside world can see are the **git
tag**, the **GitHub Release**, and the **Zenodo deposit**.

## How to release

**Bump `version:` and `date-released:` in `CITATION.cff`. That's it.**

Everything downstream is automated. `.github/workflows/release.yml` watches `CITATION.cff` on
`main`; when its version has no matching tag, it tags the commit, publishes the GitHub Release with
that version's CHANGELOG section as the notes, and the GitHub↔Zenodo integration deposits from the
Release.

`CITATION.cff` is the trigger deliberately, rather than a new CHANGELOG heading: bumping the citable
record is an unambiguous act of intent. CHANGELOG entries get drafted, reworded, and staged long
before anyone means to ship — using them as the trigger would release half-finished bundles.

### The full sequence

| # | Step | Who |
|---|---|---|
| 1 | Decide the bundle version (see *Versioning*) | you |
| 2 | Write the CHANGELOG entry under `## [X.Y.Z] — YYYY-MM-DD` | you |
| 3 | Update `.zenodo.json` — `version` and the `related_identifiers` `tree/vX.Y.Z` URL | you |
| 4 | Update `CITATION.cff` — `version`, `date-released` (**the actual release date**) | you |
| 5 | Merge to `main` | you |
| 6 | Tag `vX.Y.Z` | **automated** |
| 7 | Publish the GitHub Release → **fires Zenodo** | **automated** |
| 8 | Add the minted version DOI to `CITATION.cff` `identifiers` | you — *see below* |

**Step 8 cannot be automated.** Zenodo mints the version DOI *during* deposit, so it does not exist
until after step 7. `scripts/check-release-drift.sh` warns every week until it is added — this is the
step most often skipped, and v1.2.0's version DOI was never added at all.

## The safety net

`scripts/check-release-drift.sh` compares four things that must agree:

1. `CHANGELOG.md` newest `## [X.Y.Z]` heading — what was written
2. `CITATION.cff` `version:` — what is citable
3. `.zenodo.json` `version` — what gets deposited
4. latest `vX.Y.Z` git tag — **what actually shipped**

Run it any time: `bash scripts/check-release-drift.sh`

`.github/workflows/release-drift.yml` runs it automatically:

- **on pull requests** touching the release files — `--files-only`, since on a release PR the version
  bump legitimately precedes the tag. Fails the PR if 1–3 disagree.
- **on push to `main`** — full, including the tag check.
- **weekly, Mondays** — full. This is the one that would have caught the original failure: drift
  appears while nobody is pushing, so a check that only runs on commits never sees it.

The same check also runs from `cinderlit-work-system`'s `scripts/weekly-check.sh`, so it surfaces in
the Thursday review even if GitHub notifications go unread.

## Versioning

Each constituent spec (`QSM`, `TSS`, `THRIVE`, `QSM-FAI`, `QSM-ARCH`) versions independently;
`CHANGELOG.md` tracks the **combined bundle**. A spec changing does not force a bundle minor — an
editorial fix to one spec is a bundle **patch**, and the spec file itself may not move at all.

State in every entry which constituent specs moved and which did not, and say explicitly whether
prior conformance claims remain valid. Implementers depend on that sentence.

## DOIs

- **Concept DOI `10.5281/zenodo.20436569`** — always resolves to the latest version. **Never
  changes.** Cite this one in prose; it stays in the top-level `doi:` field.
- **Version DOIs** — one per deposit, minted at release, accumulating in `identifiers`.

## Don'ts

- **Never rewrite a published spec file.** `specs/QSM-FAI-v1.0.1.md` and friends are shipped
  artifacts. Errata are corrected in the *current* version only and recorded in the CHANGELOG; older
  files stay as published so citations stay honest.
- **Never tag retroactively with an old date.** If a bundle was authored weeks ago and never shipped,
  cut a new patch dated today that carries it. A tag dated to the authoring day asserts a publication
  that did not happen. (This is why 1.3.0 and 1.4.0 shipped inside **1.4.1** rather than as themselves.)
- **Never guess a version DOI.** Leave it absent until Zenodo mints it.
- **Never bump `CITATION.cff` speculatively.** On `main` that *is* the release trigger.
