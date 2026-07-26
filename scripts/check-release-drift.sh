#!/usr/bin/env bash
# check-release-drift.sh — "is anything written but not released?"
#
# Bundles 1.3.0 and 1.4.0 were authored 2026-07-06 and never tagged, never released,
# never deposited. The gap went unnoticed for nineteen days, during which every citation
# of this standard resolved to v1.2.0 — a version predating QSM-FAI v1.3.0's action_tier
# field. Nothing was broken. Nothing failed. There was simply no check.
#
# A release lives in four places that must agree:
#
#   1. CHANGELOG.md   newest "## [X.Y.Z]" heading      ← what was written
#   2. CITATION.cff   version:                          ← what is citable
#   3. .zenodo.json   "version": "vX.Y.Z"               ← what gets deposited
#   4. git tag        latest vX.Y.Z                     ← what actually shipped
#
# 1–3 are edited by hand and drift silently. 4 is the only one the outside world sees.
#
# Usage:
#   bash scripts/check-release-drift.sh              # full — includes the tag check
#   bash scripts/check-release-drift.sh --files-only # skip the tag check (PR mode)
#
# --files-only exists because on a release PR the version bump lands BEFORE the tag, so
# a missing tag is expected, not drift. On main it is drift.
#
# Exit 0 = consistent. Exit 1 = drift. Meant to fail a build.

set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

FILES_ONLY=0
[[ "${1:-}" == "--files-only" ]] && FILES_ONLY=1

RED=$'\033[31m'; AMB=$'\033[33m'; GRN=$'\033[32m'; DIM=$'\033[2m'; OFF=$'\033[0m'
[[ -n "${CI:-}" ]] && { RED=""; AMB=""; GRN=""; DIM=""; OFF=""; }
FAIL=0
bad()  { printf '  %s✗%s %s\n' "$RED" "$OFF" "$1"; FAIL=1; }
warn() { printf '  %s!%s %s\n' "$AMB" "$OFF" "$1"; }
ok()   { printf '  %s✓%s %s\n' "$GRN" "$OFF" "$1"; }

printf '═══ release drift check ═══\n'

# ── 1. Extract the four versions ─────────────────────────────────────────────
changelog=$(grep -m1 -oE '^## \[[0-9]+\.[0-9]+\.[0-9]+\]' CHANGELOG.md 2>/dev/null | tr -d '#[] ')
citation=$(grep -m1 -oE '^version: *"?[0-9]+\.[0-9]+\.[0-9]+"?' CITATION.cff 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')
zenodo=$(grep -m1 -oE '"version": *"v?[0-9]+\.[0-9]+\.[0-9]+"' .zenodo.json 2>/dev/null | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')

[[ -z "$changelog" ]] && bad "CHANGELOG.md — no '## [X.Y.Z]' heading found (is the newest entry an unversioned label like 'Errata'?)"
[[ -z "$citation"  ]] && bad "CITATION.cff — no 'version:' field found"
[[ -z "$zenodo"    ]] && bad "'.zenodo.json' — no 'version' field found"
[[ $FAIL -eq 1 ]] && { printf '\n%s═══ could not read one or more version fields — fix that first.%s\n' "$RED" "$OFF"; exit 1; }

printf '%s  CHANGELOG %s · CITATION %s · zenodo %s%s\n' "$DIM" "$changelog" "$citation" "$zenodo" "$OFF"

# ── 2. The three files must agree ────────────────────────────────────────────
if [[ "$changelog" == "$citation" && "$citation" == "$zenodo" ]]; then
  ok "CHANGELOG, CITATION.cff and .zenodo.json all agree at $changelog"
else
  bad "version mismatch across files — CHANGELOG=$changelog CITATION.cff=$citation .zenodo.json=$zenodo"
  printf '      %sRELEASING.md steps 2-4: all three move together, every time.%s\n' "$DIM" "$OFF"
fi

# ── 3. Has it actually shipped? ──────────────────────────────────────────────
# This is THE check. Everything above can be perfect while nothing has been released.
if [[ $FILES_ONLY -eq 1 ]]; then
  printf '  %s· tag check skipped (--files-only): on a release PR the bump precedes the tag.%s\n' "$DIM" "$OFF"
else
  latest_tag=$(git tag --list 'v*' --sort=-v:refname 2>/dev/null | head -1)
  latest_tag_ver="${latest_tag#v}"
  if [[ -z "$latest_tag" ]]; then
    bad "no vX.Y.Z tags exist at all — nothing has ever been released"
  elif [[ "$latest_tag_ver" == "$citation" ]]; then
    ok "tag $latest_tag matches CITATION.cff — the written version has shipped"
  else
    bad "UNRELEASED: files say $citation, latest tag is $latest_tag"
    printf '      %sThis is the exact failure that hid 1.3.0 and 1.4.0 for nineteen days.%s\n' "$DIM" "$OFF"
    printf '      %sThe DOI resolves to %s. Anyone citing this standard gets that, not %s.%s\n' "$DIM" "$latest_tag_ver" "$citation" "$OFF"
    printf '      %sFix: merge to main and let release.yml tag it, or see RELEASING.md step 5.%s\n' "$DIM" "$OFF"
  fi

  # ── 4. Version DOI recorded? (warn only — needs Zenodo to have minted it) ──
  if [[ -n "$latest_tag" ]] && ! grep -q "version DOI for $latest_tag\b" CITATION.cff 2>/dev/null; then
    warn "CITATION.cff has no 'Version DOI for $latest_tag' entry in identifiers (RELEASING.md step 7)"
    printf '      %sNot a failure — Zenodo mints it during deposit, so it lands after the release.%s\n' "$DIM" "$OFF"
    printf '      %sBut it is the step most often skipped: v1.2.0'"'"'s version DOI was never added.%s\n' "$DIM" "$OFF"
  fi
fi

printf '\n'
if [[ $FAIL -eq 0 ]]; then
  printf '%s═══ no drift.%s\n' "$GRN" "$OFF"
  exit 0
fi
printf '%s═══ drift found — see RELEASING.md.%s\n' "$RED" "$OFF"
exit 1
