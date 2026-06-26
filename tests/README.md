# Conformance Test Suite

Validates that all sample files in `samples/` conform to their schemas and that named
normative rules hold.

## Run locally

```bash
pip install -r tests/requirements-test.txt
pytest tests/ -v
```

## What is tested

- **Schema validation:** every sample file validated against its corresponding JSON Schema.
- **Named rule assertions:** selected MUST rules from QSM-FAI, QSM, and THRIVE verified
  against sample files.

## What is NOT tested

Behavioral rules that require runtime observation (e.g. THRIVE §6.6 "low-capacity phases MUST
trigger reduced-friction defaults") cannot be tested from JSON alone. These remain manual
conformance checklist items described in the spec conformance-level tables.
