#!/usr/bin/env python3
"""
Reference conformance claim evaluator for the Stewardship Conformance Authority.

Usage:
    python conformance/tools/evaluate_claim.py <claim.json>
    python conformance/tools/evaluate_claim.py --registry
    python conformance/tools/evaluate_claim.py --registry --strict
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from typing import Any

try:
    from jsonschema import Draft7Validator, ValidationError
except ImportError:
    print("jsonschema is required: pip install jsonschema", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SCHEMA_PATH = os.path.join(REPO_ROOT, "schemas", "conformance-claim.schema.json")
REGISTRY_DIR = os.path.join(REPO_ROOT, "conformance", "registry")

# TSS Appendix Z alignment ladder
AXIS_LADDER = {
    "T": ["T0", "T1", "T2", "T3"],
    "C": ["C0", "C1", "C2", "C3"],
    "H": ["H0", "H1", "H2", "H3", "H4"],  # H4 Integrated (THRIVE v1.1.0) — THRIVE-only, see TSS Z.1
    "L": ["L0", "L1", "L2", "L3"],
}

ARCH_LEVELS = ["A0", "A1", "A2", "A3"]
MATURITY_LEVELS = ["M0", "M1", "M2", "M3"]

# Layers required at each A-level (QSM-ARCH §8.1)
A_LEVEL_LAYERS = {
    "A0": {"governance", "practice", "observation"},
    "A1": {"governance", "practice", "observation", "intake", "memory", "signal"},
    "A2": set(),  # all 8 — checked separately
    "A3": set(),  # all 8 + planes
}

ALL_LAYERS = {
    "intent",
    "governance",
    "intake",
    "memory",
    "practice",
    "observation",
    "signal",
    "adaptation",
}

# Which named rules a claimed level on each axis rests on.
#
# This table lives in the tool and NOT in the schema on purpose. A closed enum of rule IDs in a
# published JSON Schema goes stale the moment a spec release adds a rule, and a stale published
# schema is worse than no schema — it rejects valid claims. Tools are cheap to update; a schema
# with a permanent $id is not. The schema validates rule IDs by SHAPE; this table checks COVERAGE.
#
# QSM-FAI is deliberately absent: §8 defines L0-L3 in prose, with no numbered minimum-conformance
# list to check against. Inventing one here would be this repository asserting a normative list
# the spec does not contain. Evidence on fai_level is therefore required but not coverage-checked.
AXIS_MIN_RULES = {
    "conformance_level": ("TSS §12.3", ["TSS-01", "TSS-02", "TSS-03", "TSS-04", "TSS-05"]),
    "qsm_level": ("QSM §12", ["QSM-01", "QSM-02", "QSM-03", "QSM-04", "QSM-05"]),
    "thrive_level": ("THRIVE §12.2", ["THRIVE-01", "THRIVE-02", "THRIVE-03", "THRIVE-04"]),
    "arch_level": ("QSM-ARCH §8.2", ["ARCH-01", "ARCH-02", "ARCH-03", "ARCH-04", "ARCH-05"]),
}

LEVEL_FIELDS = ["conformance_level", "qsm_level", "thrive_level", "fai_level", "arch_level"]


def level_of(value: Any) -> str | None:
    """Read a level from either the bare-string form or the v1.3 evidence-bearing object."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        lvl = value.get("level")
        return lvl if isinstance(lvl, str) else None
    return None


def evidence_of(value: Any) -> list[dict[str, Any]]:
    if isinstance(value, dict):
        ev = value.get("evidence")
        if isinstance(ev, list):
            return [e for e in ev if isinstance(e, dict)]
    return []


def check_evidence(claim: dict[str, Any]) -> list[str]:
    """Schema v1.3: every claimed level SHOULD carry per-rule evidence.

    This is the check that closes the class. Every false level found in the 2026-07-25 review
    survived because a level was a number someone typed: an A1 whose ARCH-05 `sensitivity_level`
    had never existed in the repository's history, and an H1 whose THRIVE Need and Routine objects
    were never modelled. Neither could have been written down as `satisfied_by` without the author
    running into the absence. No validator can verify a citation is TRUE; what it can do is refuse
    to let a level be stated without one.
    """
    warnings: list[str] = []
    for field in LEVEL_FIELDS:
        value = claim.get(field)
        if value is None:
            continue
        if isinstance(value, str):
            warnings.append(
                f"DEPRECATED: {field} is a bare string level. Schema v1.3 expects "
                f'{{"level": "{value}", "evidence": [...]}}. Bare levels are accepted for ONE '
                "release (TSS §14.2 deprecation policy) and will be rejected after it."
            )
            continue
        cited = {e.get("rule") for e in evidence_of(value)}
        source, required = AXIS_MIN_RULES.get(field, (None, []))
        missing = [r for r in required if r not in cited]
        if missing:
            warnings.append(
                f"{field}={level_of(value)} cites no evidence for "
                f"{', '.join(missing)} ({source}). Cite the rule and what satisfies it, or "
                "record the gap in deviations."
            )
        for item in evidence_of(value):
            sat = (item.get("satisfied_by") or "").strip()
            if sat.lower() in ("", "tbd", "todo", "n/a", "none", "?"):
                warnings.append(
                    f"{field} evidence for {item.get('rule')} has a placeholder "
                    f"satisfied_by ({item.get('satisfied_by')!r}). A placeholder citation is a "
                    "claim with no evidence wearing the shape of one."
                )
    return [f"WARN: {w}" for w in warnings]


def load_json(path: str) -> dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def level_index(ladder: list[str], level: str) -> int:
    try:
        return ladder.index(level)
    except ValueError:
        return -1


def validate_schema(claim: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    validator = Draft7Validator(schema)
    for error in sorted(validator.iter_errors(claim), key=lambda e: list(e.path)):
        path = ".".join(str(p) for p in error.path) or "(root)"
        errors.append(f"Schema: {path}: {error.message}")
    return errors


def check_tss_conf_rules(claim: dict[str, Any]) -> list[str]:
    """TSS-CONF-01 through TSS-CONF-05 structural checks."""
    errors: list[str] = []
    warnings: list[str] = []

    if not claim.get("id"):
        errors.append("TSS-CONF-01: claim MUST have a unique id")
    if not claim.get("tss_version"):
        errors.append("TSS-CONF-02: claim MUST specify tss_version")
    if not claim.get("context_types"):
        errors.append("TSS-CONF-03: claim MUST specify context_types")
    if not claim.get("conformance_level"):
        errors.append("TSS-CONF-04: claim MUST specify conformance_level")

    # deviations should be present (even if empty) for T1+
    t_level = level_of(claim.get("conformance_level")) or ""
    if t_level in ("T1", "T2", "T3") and "deviations" not in claim:
        warnings.append(
            "TSS-CONF-05: deviations field recommended for T1+ claims (use [] if none)"
        )

    return errors + [f"WARN: {w}" for w in warnings]


def check_axis_alignment(claim: dict[str, Any]) -> list[str]:
    """Warn when C/H/L levels diverge from T-level on the alignment ladder."""
    warnings: list[str] = []
    t_level = level_of(claim.get("conformance_level"))
    if not t_level:
        return warnings

    t_idx = level_index(AXIS_LADDER["T"], t_level)
    if t_idx < 0:
        return [f"Invalid T-level: {t_level}"]

    for axis_key, field in [("C", "qsm_level"), ("H", "thrive_level"), ("L", "fai_level")]:
        domain_level = level_of(claim.get(field))
        if domain_level is None:
            continue
        d_idx = level_index(AXIS_LADDER[axis_key], domain_level)
        if d_idx < 0:
            warnings.append(f"Invalid {axis_key}-level: {domain_level}")
            continue
        if abs(d_idx - t_idx) > 1:
            warnings.append(
                f"Axis misalignment: {field}={domain_level} vs conformance_level={t_level} "
                f"(differ by more than one tier; see TSS Appendix Z)"
            )
    return [f"WARN: {w}" for w in warnings]


def check_arch_maturity_consistency(claim: dict[str, Any]) -> list[str]:
    """Check A-level vs layer_maturity consistency."""
    warnings: list[str] = []
    arch = level_of(claim.get("arch_level"))
    maturity = claim.get("layer_maturity")
    if not arch or not maturity:
        return warnings

    arch_idx = level_index(ARCH_LEVELS, arch)
    if arch_idx < 0:
        return [f"Invalid A-level: {arch}"]

    # Count layers at M0
    m0_layers = [k for k, v in maturity.items() if v == "M0"]
    m1_plus = [k for k, v in maturity.items() if v in ("M1", "M2", "M3")]

    if arch == "A2" and m0_layers:
        warnings.append(
            f"A2 claimed but layer_maturity has M0 layers: {', '.join(m0_layers)}"
        )
    if arch == "A3" and any(v in ("M0", "M1") for v in maturity.values()):
        low = [k for k, v in maturity.items() if v in ("M0", "M1")]
        warnings.append(
            f"A3 claimed but layers below M2: {', '.join(low)}"
        )

    if arch == "A0":
        required = A_LEVEL_LAYERS["A0"]
        missing = required - set(m1_plus)
        if missing:
            warnings.append(f"A0 requires M1+ on {required}; missing: {', '.join(missing)}")

    if arch in ("A2", "A3"):
        missing_layers = ALL_LAYERS - set(maturity.keys())
        if missing_layers:
            warnings.append(
                f"{arch} requires all 8 layers in layer_maturity; missing: {', '.join(sorted(missing_layers))}"
            )

    return [f"WARN: {w}" for w in warnings]


def evaluate_claim(claim_path: str, schema: dict[str, Any], strict: bool = False) -> dict[str, Any]:
    claim = load_json(claim_path)
    claim_id = claim.get("id", os.path.basename(claim_path))

    results: list[str] = []
    results.extend(validate_schema(claim, schema))
    results.extend(check_tss_conf_rules(claim))
    results.extend(check_axis_alignment(claim))
    results.extend(check_arch_maturity_consistency(claim))
    results.extend(check_evidence(claim))

    errors = [r for r in results if not r.startswith("WARN:")]
    warnings = [r[6:] for r in results if r.startswith("WARN:")]

    if strict and warnings:
        errors.extend([f"STRICT: {w}" for w in warnings])

    return {
        "id": claim_id,
        "path": claim_path,
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
    }


def evaluate_registry(schema: dict[str, Any], strict: bool = False) -> list[dict[str, Any]]:
    results = []
    if not os.path.isdir(REGISTRY_DIR):
        print(f"Registry directory not found: {REGISTRY_DIR}", file=sys.stderr)
        sys.exit(1)

    for filename in sorted(os.listdir(REGISTRY_DIR)):
        if not filename.endswith(".json") or filename == "index.json":
            continue
        path = os.path.join(REGISTRY_DIR, filename)
        results.append(evaluate_claim(path, schema, strict=strict))
    return results


def print_report(result: dict[str, Any]) -> None:
    status = "PASS" if result["valid"] else "FAIL"
    print(f"\n[{status}] {result['id']} ({result['path']})")
    for err in result["errors"]:
        print(f"  ERROR: {err}")
    for warn in result["warnings"]:
        print(f"  WARN:  {warn}")
    if result["valid"] and not result["warnings"]:
        print("  No issues found.")


def main() -> int:
    parser = argparse.ArgumentParser(description="Evaluate TSS conformance claims")
    parser.add_argument("claim", nargs="?", help="Path to a claim JSON file")
    parser.add_argument("--registry", action="store_true", help="Evaluate all registry claims")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    args = parser.parse_args()

    if not args.claim and not args.registry:
        parser.print_help()
        return 1

    schema = load_json(SCHEMA_PATH)

    if args.registry:
        results = evaluate_registry(schema, strict=args.strict)
        all_valid = True
        for result in results:
            print_report(result)
            if not result["valid"]:
                all_valid = False
        print(f"\n{'All claims valid.' if all_valid else 'Some claims failed.'}")
        return 0 if all_valid else 1

    result = evaluate_claim(args.claim, schema, strict=args.strict)
    print_report(result)
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    sys.exit(main())
