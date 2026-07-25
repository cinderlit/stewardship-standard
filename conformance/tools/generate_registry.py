#!/usr/bin/env python3
"""
Regenerate conformance/registry/index.json and REGISTRY.md from claim files.

Usage:
    python conformance/tools/generate_registry.py
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRY_DIR = os.path.join(REPO_ROOT, "conformance", "registry")


def load_json(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    claims_meta = []
    table_rows = []

    for filename in sorted(os.listdir(REGISTRY_DIR)):
        if not filename.endswith(".json") or filename == "index.json":
            continue
        path = os.path.join(REGISTRY_DIR, filename)
        claim = load_json(path)
        entry = {
            "id": claim["id"],
            "claimant": claim.get("claimant", ""),
            "implementation_url": claim.get("implementation_url", ""),
            "context_types": claim.get("context_types", []),
            "conformance_level": claim.get("conformance_level", ""),
            "qsm_level": claim.get("qsm_level"),
            "arch_level": claim.get("arch_level"),
            "claimed_at": claim.get("claimed_at", ""),
            "file": filename,
        }
        claims_meta.append(entry)

        date = (claim.get("claimed_at") or "")[:10]
        impl = claim.get("implementation_url", "")
        impl_label = impl.replace("https://", "") if impl else "—"
        table_rows.append(
            f"| [{claim['id']}]({filename}) | {claim.get('claimant', '—')} | "
            f"[{impl_label}]({impl}) | {', '.join(claim.get('context_types', []))} | "
            f"{claim.get('conformance_level', '—')} | "
            f"{claim.get('qsm_level', '—')} | "
            f"{claim.get('arch_level', '—')} | {date} |"
        )

    index = {
        "version": "1.0.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "claims": claims_meta,
    }

    index_path = os.path.join(REGISTRY_DIR, "index.json")
    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
        f.write("\n")

    md_path = os.path.join(REGISTRY_DIR, "REGISTRY.md")
    header = """# Conformance Claim Registry

Published self-declared conformance claims for stewardship stack implementations.

**Authority:** [Stewardship Conformance Authority](../CONFORMANCE.md)  
**Schema:** [`schemas/conformance-claim.schema.json`](../../schemas/conformance-claim.schema.json) v1.2  
**Evaluate:** `python conformance/tools/evaluate_claim.py --registry`

---

## Registered claims

| ID | Claimant | Implementation | Contexts | T | C | A | Filed |
|---|---|---|---|---|---|---|---|
"""
    footer = """
---

## Filing a claim

1. Copy an existing claim JSON as a template
2. Fill in all required fields and optional multi-axis levels
3. List deviations explicitly
4. Validate: `python conformance/tools/evaluate_claim.py your-claim.json`
5. Open a PR adding your claim to this directory
6. Run `python conformance/tools/generate_registry.py` to refresh this index

---

*Registry maintained by the Stewardship Conformance Authority · CC BY 4.0*
"""
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(header)
        f.write("\n".join(table_rows))
        f.write(footer)

    print(f"Wrote {index_path} ({len(claims_meta)} claims)")
    print(f"Wrote {md_path}")


if __name__ == "__main__":
    main()
