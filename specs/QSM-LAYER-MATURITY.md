# QSM — Layer Maturity Scale
**Part of:** Stewardship Conformance Authority  
**Axis:** M-level (per-layer maturity)  
**Updated:** 2026-06-26

---

## Purpose

The **M-level (Layer Maturity)** scale measures how mature a **specific layer** is within an implementation. It answers: "For this layer, how intentional, repeatable, and improving is the practice?"

M-level is **independent** of:
- **T/C/H/L-level** — spec and object conformance (TSS Appendix Z)
- **A-level** — overall architectural coverage across all eight layers (QSM-ARCH §8.1)

Do not use A0–A3 for per-layer maturity. Use M0–M3.

---

## Scale definition

| Level | Label | Description |
|---|---|---|
| **M0** | Absent / ad hoc | Layer not intentionally implemented; work happens informally without structure |
| **M1** | Emerging | Minimum viable practices; basic artifacts exist but cadence is irregular |
| **M2** | Established | Documented, repeatable practices with a maintained cadence |
| **M3** | Optimizing | Measured, calibrated, and feeding improvements to other layers |

---

## Per-layer maturity criteria

### Layer 1 — Intent

| Level | Criteria |
|---|---|
| M0 | No stated purpose; priorities implicit or reactive |
| M1 | Context declared with at least one steward and a stated purpose |
| M2 | IdentityIntentProfile defined; values documented; horizon declared |
| M3 | Annual review cadence established; drift detection active; purpose reviewed against outcomes |

### Layer 2 — Governance

| Level | Criteria |
|---|---|
| M0 | No written decision rules; authority unclear |
| M1 | At least one named steward with declared authority scope |
| M2 | Decision thresholds documented; constraint register maintained; review cadence followed |
| M3 | Exception register active; governance outcomes logged and reviewed |

### Layer 3 — Intake

| Level | Criteria |
|---|---|
| M0 | No capture system; items arrive and disappear |
| M1 | At least one capture mechanism exists |
| M2 | Items classified by context and layer; triage cadence established; backlog bounded |
| M3 | Intake patterns observed and fed back to Governance |

### Layer 4 — Memory (Knowledge)

| Level | Criteria |
|---|---|
| M0 | Decisions and lessons live only in people's heads |
| M1 | Key decisions recorded somewhere retrievable |
| M2 | Decision records include rationale and outcome; reference system maintained |
| M3 | Pattern library maintained; recurring issues linked to past decisions |

### Layer 5 — Practice (Execution)

| Level | Criteria |
|---|---|
| M0 | No planning; reactive task completion only |
| M1 | Actions tracked and can be completed |
| M2 | Actions linked to context and layer; capacity modeled; load bounded |
| M3 | Execution patterns feed back to Adaptation layer |

### Layer 6 — Observation

| Level | Criteria |
|---|---|
| M0 | Status discovered only when something breaks |
| M1 | Manual checking occurs at defined intervals |
| M2 | Thresholds defined; breaches trigger alerts; at least one automated monitor per critical entity |
| M3 | Observation feeds directly into Signal layer in real time |

### Layer 7 — Signal

| Level | Criteria |
|---|---|
| M0 | No summary or alert mechanism; must dig for status |
| M1 | At least one regular status summary exists |
| M2 | Alerts routed to the right steward; signal available on demand |
| M3 | Signal adapts to steward capacity and context state |

### Layer 8 — Adaptation (Feedback / Learning)

| Level | Criteria |
|---|---|
| M0 | Same problems recur; retrospectives produce no changes |
| M1 | At least one retrospective occurs per cycle |
| M2 | Improvements dispatched to specific layers with owners; recurring patterns tracked |
| M3 | Adaptation loop closes; improvements verified in next cycle |

---

## Claiming layer maturity

Include a `layer_maturity` object in a conformance claim (see `conformance-claim.schema.json` v1.2):

```json
{
  "layer_maturity": {
    "intent": "M2",
    "governance": "M2",
    "intake": "M1",
    "memory": "M1",
    "practice": "M2",
    "observation": "M1",
    "signal": "M0",
    "adaptation": "M1"
  }
}
```

Layer keys use lowercase slugs matching QSM-ARCH layer names.

---

## Relationship to A-level

| A-level | Typical minimum layer maturity |
|---|---|
| A0 (3 layers) | Claimed layers at M1+; others M0 |
| A1 (6 layers) | Claimed layers at M1+; unclaimed M0 |
| A2 (8 layers) | All layers at M1+; majority at M2+ |
| A3 (8 layers + planes) | All layers at M2+; cross-cutting planes documented |

An A2 claim with several M0 layers is inconsistent and SHOULD be flagged by the reference evaluator.

---

*QSM Layer Maturity Scale — © 2026 Cinderlit · CC BY 4.0*
