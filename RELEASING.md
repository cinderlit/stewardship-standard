# Releasing The Stewardship Standard

**Why this file exists:** bundles **1.3.0** and **1.4.0** were authored on 2026-07-06 and never
released. They were not tagged, not published, and not deposited. The gap went unnoticed for
nineteen days because nothing in the repo described what a release *is* — the CHANGELOG entry felt
like the finish line, and it isn't. Writing the changelog entry is step 2 of 7.

There is no CI here. Every step below is manual and every one of them has been forgotten at least
once.

## The invariant

**A CHANGELOG entry is not a release.** The only things the outside world can see are the **git
tag**, the **GitHub Release**, and the **Zenodo deposit**. Until all three exist, the version does
not exist — no matter how finished the specs are.

Current evidence of drift, as of 2026-07-25: the DOI resolved to **v1.2.0 (2026-06-25)** while the
repo had moved two bundles past it, so every citation pointed at a standard predating QSM-FAI
v1.3.0's `action_tier` field.

## Steps

1. **Decide the bundle version.** Each constituent spec (`QSM`, `TSS`, `THRIVE`, `QSM-FAI`,
   `QSM-ARCH`) versions independently; `CHANGELOG.md` tracks the *combined bundle*. A spec changing
   does not force a bundle minor — an editorial fix to one spec is a bundle **patch**.
2. **Write the CHANGELOG entry.** State which constituent specs moved and which did not. Say
   explicitly whether prior conformance claims remain valid — implementers depend on that sentence.
3. **Update `CITATION.cff`** — `version`, `date-released` (the *actual* release date, not the
   authoring date).
4. **Update `.zenodo.json`** — `version` and the `related_identifiers` URL (`tree/vX.Y.Z`).
5. **Tag and push.** `git tag vX.Y.Z && git push origin vX.Y.Z`. The tag must exist before the
   GitHub Release.
6. **Publish the GitHub Release** against that tag. **This is what triggers Zenodo** via the
   GitHub↔Zenodo integration — there is no workflow file doing it for you.
7. **Add the new version DOI back into `CITATION.cff`.** Zenodo mints it *during* the deposit, so
   it cannot be written in advance. This is the step most often skipped: as of 2026-07-25 the
   `identifiers` list held a version DOI for **v1.0.0 only** — v1.2.0's was never added.

## DOIs — which is which

- **Concept DOI `10.5281/zenodo.20436569`** — always resolves to the latest version. **Never
  changes.** This is the one to cite in prose and to leave in the top-level `doi:` field.
- **Version DOIs** — one per deposit, minted at release. These accumulate in `identifiers`. Adding
  them is step 7 and is purely record-keeping; nothing breaks immediately if it is skipped, which
  is exactly why it gets skipped.

## Don'ts

- **Never rewrite a published spec file.** `specs/QSM-FAI-v1.0.1.md` and friends are shipped
  artifacts. Errata are corrected in the *current* version only and recorded in the CHANGELOG; older
  files stay as published so citations stay honest.
- **Never tag retroactively with an old date.** If a bundle was authored weeks ago and never
  shipped, cut a new patch dated today that carries it. A tag dated to the authoring day asserts a
  publication that did not happen.
- **Never guess a version DOI.** Leave it absent until Zenodo mints it.
