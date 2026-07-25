"""
Named normative rule assertions derived from the spec.
Each test corresponds to a numbered rule in QSM-FAI, QSM, or THRIVE.
Tests are run against sample files. Implementations should run this harness
against their own data bundles to verify conformance.
"""

import pytest
from conftest import load_json, sample_path

# ---------------------------------------------------------------------------
# QSM-FAI rules
# ---------------------------------------------------------------------------

FC_SAMPLES = [
    "hearth-fiduciary-context.json",
    "self-fiduciary-context.json",
    "charter-fiduciary-context.json",
]


@pytest.mark.parametrize("sample", FC_SAMPLES)
def test_fc01_status_must_be_active(sample):
    """FC-01: An agent MUST NOT act without a FiduciaryContext in active status."""
    fc = load_json(sample_path(sample))
    assert fc.get("status") == "active", (
        f"FC-01 violation in {sample}: status must be 'active', got {fc.get('status')!r}"
    )


@pytest.mark.parametrize("sample", FC_SAMPLES)
def test_fc04_delegation_chain_has_primary(sample):
    """FC-04: delegation_chain MUST include at least one primary steward."""
    fc = load_json(sample_path(sample))
    roles = [entry.get("role") for entry in fc.get("delegation_chain", [])]
    assert "primary" in roles, (
        f"FC-04 violation in {sample}: no 'primary' role found in delegation_chain"
    )


@pytest.mark.parametrize("sample", FC_SAMPLES)
def test_fc_constraints_present(sample):
    """FC schema: constraints with max_action_tier and require_human_approval_above_tier are required."""
    fc = load_json(sample_path(sample))
    constraints = fc.get("constraints", {})
    assert "max_action_tier" in constraints, (
        f"{sample}: constraints.max_action_tier is required"
    )
    assert "require_human_approval_above_tier" in constraints, (
        f"{sample}: constraints.require_human_approval_above_tier is required"
    )


# ---------------------------------------------------------------------------
# QSM rules
# ---------------------------------------------------------------------------

def test_qsm_nf01_goal_driven_context_declares_needs_framework():
    """QSM-NF-01: Implementation SHOULD declare needs_framework on each Context."""
    bundle = load_json(sample_path("goal-driven-context.json"))
    context_obj = bundle.get("context", bundle)
    assert "needs_framework" in context_obj, (
        "QSM-NF-01: goal-driven-context.json context object should declare needs_framework"
    )


def test_goal_driven_context_declares_both_frameworks():
    """QSM-NF-01 + QSM-LF-01: goal-driven-context.json should declare needs and learning frameworks."""
    bundle = load_json(sample_path("goal-driven-context.json"))
    ctx = bundle.get("context", bundle)
    assert "needs_framework" in ctx, "QSM-NF-01: goal-driven context should declare needs_framework"
    assert "learning_framework" in ctx, "QSM-LF-01: goal-driven context should declare learning_framework"


# ---------------------------------------------------------------------------
# THRIVE rules
# ---------------------------------------------------------------------------

def test_thrive02_life_stage_sample_has_capacity():
    """THRIVE-02: A conformant THRIVE implementation MUST represent capacity and load."""
    bundle = load_json(sample_path("life-stage-transition.json"))
    assert "capacity_profile" in bundle, (
        "THRIVE-02: life-stage-transition.json must include a capacity_profile"
    )
    cap = bundle["capacity_profile"]
    assert "capacity" in cap, (
        "THRIVE-02: capacity_profile must include capacity dimensions"
    )


def test_thrive_life_stage_satisfiers_not_needs():
    """THRIVE §6.5: stage modifies satisfiers, not needs. Needs list should be stable."""
    bundle = load_json(sample_path("life-stage-transition.json"))
    assert "needs" in bundle, "life-stage-transition.json must include a needs block"
    assert len(bundle["needs"]) > 0, "needs list must not be empty — stage does not remove needs"


def test_behavior_design_fields_are_optional():
    """routine.schema.json v1.1: behavior_design is optional — routines without it are valid."""
    bundle = load_json(sample_path("behavior-design-routine.json"))
    routines = bundle.get("routines", [])
    assert len(routines) > 0, "behavior-design-routine.json must contain at least one routine"
    has_behavior_design = any("behavior_design" in r for r in routines)
    assert has_behavior_design, "At least one routine in behavior-design-routine.json should use behavior_design"


# ---------------------------------------------------------------------------
# Record rules
# ---------------------------------------------------------------------------

def test_decision_confidence_is_between_0_and_1():
    """record.schema.json v1.2: decision_confidence must be 0–1 when present."""
    bundle = load_json(sample_path("goal-driven-context.json"))
    records = bundle.get("records", [])
    for rec in records:
        if "decision_confidence" in rec:
            val = rec["decision_confidence"]
            assert 0 <= val <= 1, (
                f"decision_confidence must be between 0 and 1, got {val} in record {rec.get('id')}"
            )


def test_expected_outcome_at_decision_time_not_hindsight():
    """record.schema.json: expected_outcome should be present when decision_confidence is declared."""
    bundle = load_json(sample_path("goal-driven-context.json"))
    records = bundle.get("records", [])
    for rec in records:
        if "decision_confidence" in rec:
            assert "expected_outcome" in rec, (
                f"Record {rec.get('id')} has decision_confidence but no expected_outcome — "
                "both should be declared at decision time"
            )
