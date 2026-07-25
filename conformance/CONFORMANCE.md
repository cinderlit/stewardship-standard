# Stewardship Conformance Authority (SCA)

**Status:** Active  
**Home:** `stewardshipstandard.org/conformance` (when the spec site is deployed)  
**Registry:** [`registry/`](registry/)  
**Evaluator:** [`tools/evaluate_claim.py`](tools/evaluate_claim.py)

---

## Purpose

The Stewardship Conformance Authority is the **conformance and attestation function** of the stewardship stack. It is distinct from spec authorship:

| Function | Who | Job |
|---|---|---|
| **Standards body** | Cinderlit / stewardshipstandard.org | Authors and maintains TSS, QSM, THRIVE, QSM-FAI, QSM-ARCH |
| **Conformance authority (SCA)** | This function | Defines conformance axes, maintains the claim registry, provides reference evaluation tools, and documents attestation process |

The standards body writes the rules. The conformance authority helps implementations **declare**, **validate**, and **discover** claims against those rules — without the author also being the sole judge of compliance.

---

## Conformance axes

Implementations MAY claim on **multiple independent axes**. Do not collapse them into a single score.

### Primary audit axis — T-level (TSS)

| Level | Label | Description |
|---|---|---|
| **T0** | Descriptive | Describes stewardship concepts informally |
| **T1** | Structured | Uses explicit objects and relationships |
| **T2** | Auditable | Maintains append-only records and exports them |
| **T3** | Normative | Fully implements required object types, context rules, and scenario support |

**T-level is the primary audit standard** (TSS §12.1). Every conformance claim MUST include a T-level.

### Domain axes — C / H / L (aligned ladder)

These measure **spec and object conformance** within a domain. They align with T-level when practical (TSS Appendix Z):

| QSM (C) | TSS (T) | THRIVE (H) | QSM-FAI (L) | Label |
|---|---|---|---|---|
| C0 | T0 | H0 | L0 | Observational / Informal |
| C1 | T1 | H1 | L1 | Structured |
| C2 | T2 | H2 | L2 | Operational / Auditable |
| C3 | T3 | H3 | L3 | Normative / Full |
| — | — | H4 | — | Integrated (THRIVE only) |

An implementation claiming T2 MAY also claim C2, H2, and L2 if it satisfies the respective domain rules.

**THRIVE runs one level past the shared ladder.** THRIVE v1.1.0 defines **H4 Integrated** — full H3 plus `WorldDomainScope`, `IdentityIntentProfile`, `DevelopmentalContext` and `TemporalCycleProfile`. It has no C/T/L counterpart because it extends the THRIVE domain model rather than audit rigour; an H4 implementation is at **T3** on the primary axis.

### Architectural axis — A-level (QSM-ARCH)

Measures **architectural completeness** — how many of the eight layers and five cross-cutting planes are implemented (QSM-ARCH §8.1):

| Level | Label | Requirements |
|---|---|---|
| **A0** | Minimal | Governance, Practice, and Observation layers |
| **A1** | Operational | Adds Intake, Memory, and Signal |
| **A2** | Complete | All 8 layers implemented |
| **A3** | Governed | All 8 layers plus all 5 cross-cutting planes formally supported |

A-levels are **independent** of T/C/H/L. Example: T2 + A1 is coherent (strong object conformance, partial architectural coverage).

### Layer maturity axis — M-level (per layer)

Measures **how mature a specific layer is within an implementation**, independent of whether other layers exist. Defined normatively in [QSM-LAYER-MATURITY.md](../specs/QSM-LAYER-MATURITY.md).

| Level | Label | Description |
|---|---|---|
| **M0** | Absent / ad hoc | Layer not intentionally implemented |
| **M1** | Emerging | Minimum viable practices for the layer |
| **M2** | Established | Documented, repeatable, reviewed on cadence |
| **M3** | Optimizing | Measured, calibrated, feeds back to other layers |

**Important:** M-level uses the prefix **M** deliberately. It is NOT the same as A-level (A0–A3), which measures overall architectural coverage. Do not use "A0–A3" for per-layer maturity.

---

## Claim format

Claims MUST validate against [`schemas/conformance-claim.schema.json`](../schemas/conformance-claim.schema.json) (v1.2+).

Required fields:
- `id` — unique claim identifier
- `tss_version` — TSS version claimed against
- `context_types` — context types supported (SELF, HEARTH, ESTATE, CHARTER, CREST)
- `conformance_level` — T-level (required)

Optional multi-axis fields:
- `qsm_level`, `thrive_level`, `fai_level` — domain axes
- `arch_level` — architectural completeness
- `layer_maturity` — per-layer M-level map
- `deviations` — explicit partial implementations
- `implementation_url` — where the implementation lives

See [`registry/`](registry/) for published claims.

---

## Attestation process

### Self-declaration (default)

Per TSS §12.2, conformance claims are **self-declared**. The claimant:
1. Evaluates their implementation against the relevant spec(s)
2. **Registers** the claim in [`registry/`](registry/)
3. Lists all deviations explicitly
4. Runs the reference evaluator: `python conformance/tools/evaluate_claim.py <claim.json>`

### Registration is not optional

> **An implementation MUST NOT publish a conformance claim without registering it in
> `conformance/registry/`.**

**An unregistered claim is unvalidated by construction — the suite cannot see it.** The reference
evaluator and the test suite read the registry; a claim file sitting in some other repository is
outside everything that could tell the claimant they are wrong.

This is stated as a MUST because the alternative was tried. Step 2 above previously read *"files a
claim JSON in the registry **or publishes one that validates**"*, and that `or` is the whole
failure: of three implementations known to carry a claim, the one with a malformed level was the
one never registered, so nothing ever evaluated it. Every part of this authority — schema, named
rules, CI — is reachable only through registration. Skipping it does not produce a weaker check;
it produces **no check**.

### Conflict of interest

**Spec authors MUST NOT self-certify without independent review** when claiming T2+ or A2+ for a reference implementation they maintain.

For Cinderlit-maintained reference implementations (orgestra, quantifiedly, woodcrestwa):
- Claims are filed by the implementation steward
- Deviations MUST be explicit
- T3/A3 claims require at least one external reviewer (GitHub issue or documented review)

### Third-party attestation (future)

The SCA does not currently operate a paid certification program. Third-party attestations MAY be recorded as additional metadata on a claim when a formal program exists.

---

## Reference evaluator

```bash
# Validate a single claim
python conformance/tools/evaluate_claim.py conformance/registry/cc-orgestra-001.json

# Validate entire registry
python conformance/tools/evaluate_claim.py --registry

# Regenerate registry index
python conformance/tools/generate_registry.py
```

The evaluator checks:
- JSON Schema validation (TSS-CONF-01 through TSS-CONF-05)
- Axis alignment warnings (T vs C/H/L ladder)
- Architectural consistency (A-level vs layer_maturity coverage)
- Registry integrity when run with `--registry`

---

## Relationship to other entities

| Entity | Role in conformance |
|---|---|
| **stewardshipstandard.org** | Hosts specs; SCA is a function within the standards repo |
| **quantifiedly.com** | Teaches the conformance framework; links here for claims and evaluation |
| **orgestra.org** | Reference implementation; files multi-axis claims |
| **woodcrestwa.com** | CHARTER→CREST instance; files architectural + maturity claims |
| **locusguild.org** | Practitioner network; may adopt SCA tools for member attestations (future) |

---

*Stewardship Conformance Authority — © 2026 Cinderlit · CC BY 4.0*
