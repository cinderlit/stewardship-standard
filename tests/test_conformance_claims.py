"""
Conformance claim validation tests.
Validates registry claims and sample against conformance-claim.schema.json v1.2.
"""

import os
import sys

import pytest
from jsonschema import validate, ValidationError
from conftest import load_json, schema_path

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY_DIR = os.path.join(REPO_ROOT, "conformance", "registry")


def registry_claim_paths():
    if not os.path.isdir(REGISTRY_DIR):
        return []
    return [
        os.path.join(REGISTRY_DIR, f)
        for f in sorted(os.listdir(REGISTRY_DIR))
        if f.endswith(".json") and f != "index.json"
    ]


CLAIM_PATHS = registry_claim_paths() + [
    os.path.join(REPO_ROOT, "samples", "default-conformance-claim.json"),
]


@pytest.fixture(scope="module")
def claim_schema():
    return load_json(schema_path("conformance-claim.schema.json"))


@pytest.mark.parametrize("claim_path", CLAIM_PATHS, ids=lambda p: os.path.basename(p))
def test_claim_validates_against_schema(claim_path, claim_schema):
    if not os.path.isfile(claim_path):
        pytest.skip(f"{claim_path} not found")
    claim = load_json(claim_path)
    try:
        validate(instance=claim, schema=claim_schema)
    except ValidationError as e:
        pytest.fail(
            f"{os.path.basename(claim_path)} failed schema validation: "
            f"{e.message} (path: {list(e.path)})"
        )


def test_registry_index_matches_claim_files(claim_schema):
    index_path = os.path.join(REGISTRY_DIR, "index.json")
    if not os.path.isfile(index_path):
        pytest.skip("registry index not found")
    index = load_json(index_path)
    claim_files = {
        f for f in os.listdir(REGISTRY_DIR) if f.endswith(".json") and f != "index.json"
    }
    indexed_files = {entry["file"] for entry in index.get("claims", [])}
    assert claim_files == indexed_files, (
        f"index.json out of sync: files={claim_files}, indexed={indexed_files}"
    )


def level_of(value):
    """Levels may be a bare string (deprecated) or the v1.3 {level, evidence} object."""
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return value.get("level")
    return None


def test_orgestra_claim_reflects_the_2026_07_25_correction():
    """This test previously asserted `arch_level` was PRESENT.

    It passed for a month against a level that had never been true: QSM-ARCH §8.2 ARCH-05
    requires objects holding personal or sensitive data to declare `sensitivity_level`, and that
    field has never existed in the implementation's history. The A1 and H1 levels were entered to
    match the shape of the registry record rather than derived from the implementation, and a test
    asserting a field is non-empty cannot tell the difference. Inverted here so the correction
    cannot silently regress.
    """
    path = os.path.join(REGISTRY_DIR, "cc-orgestra-001.json")
    if not os.path.isfile(path):
        pytest.skip("orgestra claim not found")
    claim = load_json(path)
    assert claim.get("qsm_level"), "orgestra claim should declare qsm_level"
    assert claim.get("layer_maturity"), "orgestra claim should declare layer_maturity"
    assert "arch_level" not in claim, (
        "arch_level was withdrawn, not downgraded: ARCH-05's sensitivity_level has never existed "
        "in the implementation. Re-add only with evidence."
    )
    assert level_of(claim.get("thrive_level")) == "H0", (
        "thrive_level was corrected H1 -> H0: THRIVE §12.1 H1 requires explicit need and routine "
        "objects, and neither has ever been modelled."
    )


def test_every_registry_entry_points_at_a_source():
    """A registry entry is a pointer, not an independent document.

    With exactly two claims registered, the copies had already drifted: one published a deviation
    that had become false while omitting three that had become true. `source.content_hash` is what
    makes that detectable. This test asserts the field exists; `generate_registry.py
    --verify-sources` is what checks it still matches.
    """
    missing = []
    for path in registry_claim_paths():
        claim = load_json(path)
        if not claim.get("source"):
            missing.append(os.path.basename(path))
    assert not missing, (
        "registry entries with no `source` block (copies with no provenance): "
        + ", ".join(missing)
    )


def test_registry_artifacts_are_generated_not_hand_edited():
    """index.json and REGISTRY.md look hand-maintainable and are not."""
    import subprocess
    tool = os.path.join(REPO_ROOT, "conformance", "tools", "generate_registry.py")
    result = subprocess.run(
        [sys.executable, tool, "--check"], capture_output=True, text=True, cwd=REPO_ROOT
    )
    assert result.returncode == 0, (
        "registry artifacts are stale or hand-edited:\n"
        + result.stdout + result.stderr
        + "\nRun: python conformance/tools/generate_registry.py"
    )


def test_sample_claim_uses_the_evidence_bearing_form():
    """The sample is the documentation. If it shows a bare level, that is what gets copied."""
    path = os.path.join(REPO_ROOT, "samples", "default-conformance-claim.json")
    if not os.path.isfile(path):
        pytest.skip("sample claim not found")
    claim = load_json(path)
    level = claim.get("conformance_level")
    assert isinstance(level, dict), "sample should demonstrate the evidence-bearing object form"
    rules = {e["rule"] for e in level["evidence"]}
    assert {"TSS-01", "TSS-02", "TSS-03", "TSS-04", "TSS-05"} <= rules, (
        "sample should cite every TSS §12.3 minimum-conformance rule"
    )
    for item in level["evidence"]:
        assert item["satisfied_by"].strip().lower() not in ("", "tbd", "todo", "n/a"), (
            f"placeholder satisfied_by on {item['rule']} — the sample teaches the failure mode"
        )


def test_woodcrest_claim_has_arch_and_maturity():
    path = os.path.join(REGISTRY_DIR, "cc-woodcrestwa-001.json")
    if not os.path.isfile(path):
        pytest.skip("woodcrest claim not found")
    claim = load_json(path)
    assert level_of(claim.get("arch_level")) == "A2"
    maturity = claim.get("layer_maturity", {})
    assert len(maturity) == 8, "woodcrest should declare all 8 layer maturity levels"
    assert "CHARTER" in claim.get("context_types", [])
    assert "CREST" in claim.get("context_types", [])
