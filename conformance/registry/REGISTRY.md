# Conformance Claim Registry

Published self-declared conformance claims for stewardship stack implementations.

**Authority:** [Stewardship Conformance Authority](../CONFORMANCE.md)  
**Schema:** [`schemas/conformance-claim.schema.json`](../../schemas/conformance-claim.schema.json) v1.2  
**Evaluate:** `python conformance/tools/evaluate_claim.py --registry`

---

## Registered claims

| ID | Claimant | Implementation | Contexts | T | C | A | Filed |
|---|---|---|---|---|---|---|---|
| [cc-orgestra-001](cc-orgestra-001.json) | person_caitlin | [orgestra.org](https://orgestra.org) | SELF, HEARTH, CHARTER | T1 | C1 | A1 | 2026-06-25 |
| [cc-woodcrestwa-001](cc-woodcrestwa-001.json) | Woodcrest HOA | [woodcrestwa.com](https://woodcrestwa.com) | CHARTER, CREST | T0 | — | A2 | 2026-06-26 |

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
