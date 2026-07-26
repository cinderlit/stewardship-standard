# Conformance Claim Registry

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
| [cc-orgestra-001](cc-orgestra-001.json) | person_caitlin | [orgestra.org](https://orgestra.org) | SELF, HEARTH, CHARTER | T1 | C1 | — | — | 2026-06-25 |
| [cc-woodcrestwa-001](cc-woodcrestwa-001.json) | Woodcrest HOA | [woodcrestwa.com](https://woodcrestwa.com) | CHARTER, CREST | T0 | — | A2 | — | 2026-06-26 |

---

## Withdrawn / not registered

Recorded so that an absence reads as a decision rather than an oversight.

| ID | Status | Why |
|---|---|---|
| `cc-quantified-estate-001` | withdrawn | The claim was withdrawn rather than corrected in place: its levels were not derived from an assessment, so no edit to them would have been evidence-based either. Re-issue after a real assessment against the schema's evidence form. |

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
