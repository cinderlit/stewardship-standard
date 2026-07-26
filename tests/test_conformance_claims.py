"""
Conformance claim validation tests.
Validates registry claims and sample against conformance-claim.schema.json v1.2.
"""

import os
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


def test_orgestra_claim_has_multi_axis():
    path = os.path.join(REGISTRY_DIR, "cc-orgestra-001.json")
    if not os.path.isfile(path):
        pytest.skip("orgestra claim not found")
    claim = load_json(path)
    assert claim.get("qsm_level"), "orgestra claim should declare qsm_level"
    assert claim.get("arch_level"), "orgestra claim should declare arch_level"
    assert claim.get("layer_maturity"), "orgestra claim should declare layer_maturity"


def test_woodcrest_claim_has_arch_and_maturity():
    path = os.path.join(REGISTRY_DIR, "cc-woodcrestwa-001.json")
    if not os.path.isfile(path):
        pytest.skip("woodcrest claim not found")
    claim = load_json(path)
    assert claim.get("arch_level") == "A2"
    maturity = claim.get("layer_maturity", {})
    assert len(maturity) == 8, "woodcrest should declare all 8 layer maturity levels"
    assert "CHARTER" in claim.get("context_types", [])
    assert "CREST" in claim.get("context_types", [])
