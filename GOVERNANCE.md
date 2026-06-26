# Governance

## Steward organization

The Stewardship Standard is published and maintained by **Cinderlit**
(cinderlit.com), founded and authored by Caitlin Stokes. The standard is
hosted at stewardshipstandard.org. **Excentropy** (excentropy.com) is the
official implementation partner and maintains the reference implementations.

## Maintainer

- **Author / lead maintainer:** Caitlin Stokes

## Decision-making

This standard is published openly under CC BY 4.0 (specification) and Apache
2.0 (schemas). Anyone may implement, extend, or fork it. Changes to the
*canonical* specification are governed as follows:

1. **Proposals** are raised as GitHub issues with a use case and example data.
2. **Discussion** happens in the open on the issue and in Discussions.
3. **Maintainer review** occurs on a quarterly cycle.
4. **Acceptance** results in a versioned change recorded in `CHANGELOG.md`.

## Amendment process

Per the change-control sections of each spec:

- **MAJOR** changes (breaking changes to required objects or conformance rules)
  require a documented migration path.
- **MINOR** changes (new context types, new optional fields) must preserve
  backward compatibility.
- **PATCH** changes (clarifications, errata) must not alter conformance.

Proposed amendments SHOULD include example data and at least one use case.

## Conformance authority

The **Stewardship Conformance Authority (SCA)** is the conformance and
attestation function of the stack, documented in
[`conformance/CONFORMANCE.md`](conformance/CONFORMANCE.md). It is distinct
from spec authorship: the standards body writes the rules; the SCA helps
implementations declare, validate, and discover claims against those rules.

**TSS T-level is the primary audit standard** for the stack. QSM (C-level),
THRIVE (H-level), and QSM-FAI (L-level) define domain-specific interpretations
of the same conformance tiers, as specified in TSS Appendix Z. QSM-ARCH
(A-level) measures architectural completeness. Layer Maturity (M-level)
measures per-layer practice maturity — see
[`specs/QSM-LAYER-MATURITY.md`](specs/QSM-LAYER-MATURITY.md).

A conformance claim is self-declared and must be explicit and versioned
(TSS §12.2). Claims are published in
[`conformance/registry/`](conformance/registry/). The SCA does not currently
operate a paid certification body; spec authors must not self-certify at T2+
or A2+ without independent review (see CONFORMANCE.md §Attestation).

## Trademarks

Names including "The Stewardship Standard," "Quantified Stewardship Model,"
"QSM," "THRIVE," and "QSM-FAI" are used to identify this standard and its
canonical specifications. The open license grants rights to the specification
text and schemas; it does not grant rights to use these names in a way that
implies endorsement or official status. See the README for attribution
guidance.

## Stewardship of the standard itself

In keeping with the standard's own principles, governance of this standard is
treated as an ongoing stewardship responsibility: open, accountable,
auditable through the changelog and issue history, and oriented toward
long-term health over short-term expansion.
