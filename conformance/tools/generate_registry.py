#!/usr/bin/env python3
"""
The ONLY writer of conformance/registry/index.json and REGISTRY.md.

Usage:
    python conformance/tools/generate_registry.py                 # regenerate
    python conformance/tools/generate_registry.py --check         # fail if stale/hand-edited
    python conformance/tools/generate_registry.py --verify-sources
    python conformance/tools/generate_registry.py --hash <file>   # print a source content_hash

Why --check exists
------------------
`index.json` and `REGISTRY.md` are generated artifacts that look exactly like hand-maintained
ones. Nothing stopped anybody editing them directly, so the registry could disagree with its own
claim files and no build would notice. --check regenerates in memory and compares byte-for-byte;
it is meant to fail a build.

Why --verify-sources is separate
--------------------------------
A registry entry is a POINTER: the source of truth for a claim is the implementation's own claim
file. Entries carry `source.content_hash`, so divergence from source is DETECTABLE. It is not
always CHECKABLE from public CI — some implementations are in private repositories, and this is a
public repository. So source verification is its own mode, run where the sources are reachable.

It fails loudly on an unreachable source rather than skipping it. A check that quietly passes when
it could not run is worse than no check: it reports "verified" for something it never looked at.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRY_DIR = os.path.join(REPO_ROOT, "conformance", "registry")

# Claims that MUST NOT be registered, and why. Registration is a MUST (CONFORMANCE.md), so the
# absence of an entry is otherwise indistinguishable from an oversight — which is exactly how a
# malformed claim went unevaluated in the first place. Recording the withdrawal makes "not here"
# a decision rather than a gap.
WITHDRAWN = [
    {
        "id": "cc-quantified-estate-001",
        "status": "withdrawn",
        "reason": (
            "The claim was withdrawn rather than corrected in place: its levels were not "
            "derived from an assessment, so no edit to them would have been evidence-based "
            "either. Re-issue after a real assessment against the schema's evidence form."
        ),
    },
]


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def canonical_bytes(obj) -> bytes:
    """Canonical JSON for hashing: sorted keys, compact separators, UTF-8.

    Hashing raw file bytes would make a reformat look like a substantive change, and every
    false-positive teaches a reader to ignore the check.
    """
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def content_hash(obj) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(obj)).hexdigest()


def level_str(value) -> str:
    """Levels may be a bare string (deprecated) or the v1.3 {level, evidence} object."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict) and isinstance(value.get("level"), str):
        return value["level"]
    return ""


def claim_files() -> list[str]:
    return [
        f
        for f in sorted(os.listdir(REGISTRY_DIR))
        if f.endswith(".json") and f != "index.json"
    ]


def build() -> tuple[str, str]:
    """Return the (index.json, REGISTRY.md) content this registry should have."""
    claims_meta = []
    table_rows = []

    for filename in claim_files():
        claim = load_json(os.path.join(REGISTRY_DIR, filename))
        evidenced = [
            f
            for f in ("conformance_level", "qsm_level", "thrive_level", "fai_level", "arch_level")
            if isinstance(claim.get(f), dict)
        ]
        claims_meta.append(
            {
                "id": claim["id"],
                "claimant": claim.get("claimant", ""),
                "implementation_url": claim.get("implementation_url", ""),
                "context_types": claim.get("context_types", []),
                "conformance_level": level_str(claim.get("conformance_level")),
                "qsm_level": level_str(claim.get("qsm_level")) or None,
                "arch_level": level_str(claim.get("arch_level")) or None,
                "claimed_at": claim.get("claimed_at", ""),
                "evidence_bearing_levels": evidenced,
                "source": claim.get("source"),
                "file": filename,
            }
        )

        impl = claim.get("implementation_url", "")
        impl_label = impl.replace("https://", "") if impl else "—"
        ev = f"{len(evidenced)}/5" if evidenced else "—"
        table_rows.append(
            f"| [{claim['id']}]({filename}) | {claim.get('claimant', '—')} | "
            f"[{impl_label}]({impl}) | {', '.join(claim.get('context_types', []))} | "
            f"{level_str(claim.get('conformance_level')) or '—'} | "
            f"{level_str(claim.get('qsm_level')) or '—'} | "
            f"{level_str(claim.get('arch_level')) or '—'} | "
            f"{ev} | {(claim.get('claimed_at') or '')[:10]} |"
        )

    index = {
        "version": "1.1.0",
        "generated_at": "GENERATED_AT",
        "claims": claims_meta,
        "withdrawn": WITHDRAWN,
    }
    index_text = json.dumps(index, indent=2, ensure_ascii=False) + "\n"

    header = """# Conformance Claim Registry

Published self-declared conformance claims for stewardship stack implementations.

**Authority:** [Stewardship Conformance Authority](../CONFORMANCE.md)
**Schema:** [`schemas/conformance-claim.schema.json`](../../schemas/conformance-claim.schema.json) v1.3
**Evaluate:** `python conformance/tools/evaluate_claim.py --registry`

> **Generated file — do not edit by hand.** `generate_registry.py` is the only writer, and
> `--check` fails the build when this file disagrees with the claim files beside it.

> **Registration is required.** An implementation MUST NOT publish a conformance claim without
> registering it here. An unregistered claim is unvalidated by construction — nothing in this
> authority can see it.

---

## Registered claims

`Evidence` counts how many of the five level axes carry per-rule evidence rather than a bare
level. A bare level is accepted for one release and is deprecated.

| ID | Claimant | Implementation | Contexts | T | C | A | Evidence | Filed |
|---|---|---|---|---|---|---|---|---|
"""

    withdrawn_rows = "\n".join(
        f"| `{w['id']}` | {w['status']} | {w['reason']} |" for w in WITHDRAWN
    )
    footer = f"""

---

## Withdrawn / not registered

Recorded so that an absence reads as a decision rather than an oversight.

| ID | Status | Why |
|---|---|---|
{withdrawn_rows}

---

## Filing a claim

1. Copy an existing claim JSON as a template
2. Fill in all required fields and optional multi-axis levels
3. **Give each claimed level `evidence`** — the minimum-conformance rules it rests on and, for
   each, the artifact that satisfies it. This is the point of the format: a level you have to
   justify is a different thing from a level you type.
4. List deviations explicitly
5. Validate: `python conformance/tools/evaluate_claim.py your-claim.json`
6. Open a PR adding your claim to this directory
7. Run `python conformance/tools/generate_registry.py` to refresh this index

---

*Registry maintained by the Stewardship Conformance Authority · CC BY 4.0*
"""
    return index_text, header + "\n".join(table_rows) + footer


def read(path: str) -> str:
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def stamp(index_text: str, generated_at: str) -> str:
    return index_text.replace("GENERATED_AT", generated_at)


def cmd_check() -> int:
    index_text, md_text = build()
    index_path = os.path.join(REGISTRY_DIR, "index.json")
    md_path = os.path.join(REGISTRY_DIR, "REGISTRY.md")

    failed = False
    current_index = read(index_path)
    try:
        existing_stamp = json.loads(current_index).get("generated_at", "")
    except (ValueError, AttributeError):
        existing_stamp = ""
    # generated_at is a timestamp, not content — compare everything else.
    if current_index != stamp(index_text, existing_stamp):
        print("FAIL: conformance/registry/index.json is stale or hand-edited.", file=sys.stderr)
        failed = True
    if read(md_path) != md_text:
        print("FAIL: conformance/registry/REGISTRY.md is stale or hand-edited.", file=sys.stderr)
        failed = True

    if failed:
        print(
            "\ngenerate_registry.py is the only writer of these two files.\n"
            "Run `python conformance/tools/generate_registry.py` and commit the result.",
            file=sys.stderr,
        )
        return 1
    print("Registry artifacts are in sync with the claim files.")
    return 0


def cmd_verify_sources() -> int:
    failed = False
    checked = 0
    for filename in claim_files():
        claim = load_json(os.path.join(REGISTRY_DIR, filename))
        source = claim.get("source")
        if not source:
            print(f"FAIL: {filename} has no `source` block — it is a copy with no provenance.", file=sys.stderr)
            failed = True
            continue
        url = source["source_url"]
        if url == "self:registry":
            # Declared as having no external source. Reported, never silently passed over: the
            # point of the field is that "no provenance" is visible in the output.
            print(f"SELF-SOURCED: {filename} — registry entry is the source of record.")
            continue
        try:
            if url.startswith("file://"):
                payload = load_json(url[len("file://"):])
            elif url.startswith(("http://", "https://")):
                with urllib.request.urlopen(url, timeout=15) as r:  # noqa: S310
                    payload = json.loads(r.read().decode("utf-8"))
            else:
                raise ValueError(f"unsupported source_url scheme: {url}")
        except Exception as exc:  # noqa: BLE001
            # Deliberately an error, not a skip. See module docstring.
            print(f"FAIL: {filename}: could not read source {url}: {exc}", file=sys.stderr)
            failed = True
            continue

        checked += 1
        actual = content_hash(payload)
        if actual != source["content_hash"]:
            print(
                f"FAIL: {filename}: registry entry has DIVERGED from its source.\n"
                f"       recorded {source['content_hash']}\n"
                f"       actual   {actual}\n"
                f"       source   {url} (fetched_at {source.get('fetched_at')})",
                file=sys.stderr,
            )
            failed = True

    if failed:
        return 1
    print(f"All {checked} registry sources match their recorded hashes.")
    return 0


def cmd_write() -> int:
    index_text, md_text = build()
    generated_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    index_path = os.path.join(REGISTRY_DIR, "index.json")
    md_path = os.path.join(REGISTRY_DIR, "REGISTRY.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(stamp(index_text, generated_at))
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_text)
    print(f"Wrote {index_path} ({len(claim_files())} claims)")
    print(f"Wrote {md_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    parser.add_argument("--check", action="store_true", help="fail if artifacts are stale or hand-edited")
    parser.add_argument("--verify-sources", action="store_true", help="fail if a registry entry diverged from its source")
    parser.add_argument("--hash", metavar="FILE", help="print the content_hash of a source claim file")
    args = parser.parse_args()

    if args.hash:
        print(content_hash(load_json(args.hash)))
        return 0
    if args.check:
        return cmd_check()
    if args.verify_sources:
        return cmd_verify_sources()
    return cmd_write()


if __name__ == "__main__":
    sys.exit(main())
