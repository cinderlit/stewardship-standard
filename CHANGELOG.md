# Changelog

All notable changes to The Stewardship Standard are documented here. This
project follows [Semantic Versioning](https://semver.org). Each constituent
spec is versioned independently; this changelog tracks the combined release
bundle.

## [1.0.0] — 2026-05-28

Initial public release of the four-document stewardship stack.

### Specifications included
- **QSM v1.0.1** — Quantified Stewardship Model: domain-agnostic ontology and methodology.
- **TSS v1.1.1** — The Stewardship Standard: normative umbrella, conformance levels (T0–T3), records, and audit rules.
- **THRIVE v1.0.1** — Self and Wellness Context Layer.
- **QSM-FAI v1.0.1** — Fiduciary AI Interface: FiduciaryContext, action tiers, rationale, and TENURE audit records.

### Reference schemas
- TSS core: `context`, `entity`, `relationship`, `record`, `conformance-claim`.
- QSM-FAI: `fiduciary-context`, `rationale`, `tenure-entry`.
- THRIVE: `self-context`, `capacity-profile`, `need`, `routine`, `wellness-record`.

### Samples
- `hearth-context.json`, `hearth-fiduciary-context.json`, `default-conformance-claim.json`.

### Notes
- HEARTH (the Quantified Home) is the first hardened context and the normative reference implementation.
- TSS T-level is established as the primary audit standard; QSM C-level, THRIVE H-level, and QSM-FAI L-level are domain interpretations of the same conformance tier (TSS Appendix Z).
- Specification text licensed under CC BY 4.0; reference schemas under Apache 2.0.
- Each specification carries front matter for Status of This Document, Use of AI-Assisted Tools, and Openness and Governance. A canonical AI-use disclosure is provided in `AI-USE.md`.

[1.0.0]: https://github.com/cinderlit/stewardship-standard/releases/tag/v1.0.0
