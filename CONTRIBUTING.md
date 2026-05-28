# Contributing to The Stewardship Standard

Thank you for your interest in improving The Stewardship Standard. This is an
open standard, and it gets better with real-world scrutiny, counterexamples,
and implementation experience.

## Ways to contribute

- **Spec comments** — ambiguities, gaps, or contradictions in the normative text.
- **Prior art** — if you know of existing work that overlaps with any part of this stack, we want to know. Open an issue labeled `prior-art`.
- **Use cases** — describe a stewardship context (home, estate, organization, self, civic) and how the model does or doesn't serve it.
- **Schema fixes** — corrections or improvements to the reference JSON schemas.
- **Implementation reports** — what worked, what didn't, when you built against the standard.

## How to contribute

1. **Open an issue** before large changes, labeled one of: `spec-comment`, `gap`, `use-case`, `prior-art`, `schema`, or `errata`.
2. **For text or schema changes**, submit a pull request against the relevant file in `specs/` or `schemas/`.
3. **Proposed normative changes** SHOULD be accompanied by at least one concrete example and one use case (per TSS §14 governance rules).

## Versioning

The standard follows semantic versioning per spec:

- **MAJOR** — breaking changes to required objects or conformance rules.
- **MINOR** — additive changes (new context types, optional fields).
- **PATCH** — clarifications and errata.

## Conduct

Engage in good faith. Critique ideas, not people. The standard centers care,
dignity, and accountability; contributions should reflect the same.

## Licensing of contributions

By contributing, you agree that your contributions to specification text are
licensed under CC BY 4.0 and contributions to reference schemas under Apache
2.0, consistent with the rest of the repository.

## Governance

Maintainer review happens on a quarterly cycle. See [GOVERNANCE.md](GOVERNANCE.md)
for decision-making and the amendment process.
