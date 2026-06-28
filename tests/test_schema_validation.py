"""
Schema validation tests.
Every entry in SAMPLE_SCHEMA_MAP is validated against its declared schema.
Add new samples here when they are added to samples/.
"""

import pytest
from jsonschema import validate, ValidationError
from conftest import load_json, schema_path, sample_path

# Map: sample filename → schema path relative to schemas/
SAMPLE_SCHEMA_MAP = {
    "hearth-context.json": "context.schema.json",
    "hearth-fiduciary-context.json": "fiduciary-context.schema.json",
    "self-fiduciary-context.json": "fiduciary-context.schema.json",
    "charter-fiduciary-context.json": "fiduciary-context.schema.json",
    "default-conformance-claim.json": "conformance-claim.schema.json",
    "escalation-outbox-entry.json": "escalation-outbox-entry.schema.json",
    "scenario-pattern.json": "scenario-pattern.schema.json",
}


def instances_for_sample(sample, instance):
    """Return one or more schema instances from a sample file (handles bundle wrappers)."""
    if sample == "hearth-context.json":
        return [instance["context"]]
    if sample == "escalation-outbox-entry.json":
        return instance["escalation_outbox"]
    return [instance]


@pytest.mark.parametrize("sample,schema_rel", SAMPLE_SCHEMA_MAP.items())
def test_sample_validates_against_schema(sample, schema_rel):
    instance = load_json(sample_path(sample))
    schema = load_json(schema_path(schema_rel))
    for idx, sub_instance in enumerate(instances_for_sample(sample, instance)):
        try:
            validate(instance=sub_instance, schema=schema)
        except ValidationError as e:
            label = f"{sample}[{idx}]" if len(instances_for_sample(sample, instance)) > 1 else sample
            pytest.fail(f"{label} failed schema validation: {e.message} (path: {list(e.path)})")
