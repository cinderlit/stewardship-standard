# The Stewardship Standard

**An open standard for making stewardship legible, measurable, and safely automatable — and the first open standard designed explicitly as a fiduciary AI substrate.**

[![License: CC BY 4.0](https://img.shields.io/badge/Spec%20License-CC%20BY%204.0-blue.svg)](LICENSE-SPEC)
[![License: Apache 2.0](https://img.shields.io/badge/Schema%20License-Apache%202.0-green.svg)](LICENSE-SCHEMAS)
[![DOI](https://img.shields.io/badge/DOI-pending-lightgrey.svg)](#citation)

**Author:** Caitlin Stokes
**Publisher:** Cinderlit ([cinderlit.com](https://cinderlit.com))
**Standard home:** The Stewardship Standard ([stewardshipstandard.org](https://stewardshipstandard.org))
**Implementation partner:** Excentropy ([excentropy.com](https://excentropy.com))¹
**Status:** Final Draft — Public Release Candidate
**First published:** 2026-05-28
**Current release:** v1.1.0 (2026-06-22) — see [`CHANGELOG.md`](CHANGELOG.md)

---

## What this is

The Stewardship Standard is a layered open standard for representing people, places, systems, responsibilities, needs, values, and relationships in a way that makes **stewardship** — the responsible, values-aligned care of resources, relationships, and systems — legible, measurable, and improvable for both humans and AI agents.

It is built so that an AI agent can act on behalf of a human principal only within a formally declared scope, with the legal duties of care, loyalty, and disclosure encoded in the data architecture itself rather than bolted on as a policy layer. To our knowledge, **QSM-FAI is the first open standard designed explicitly as a fiduciary AI substrate.**

---

## The four-document stack

The standard is composed of four interdependent specifications. **TSS is the normative umbrella; the other three are domain layers it governs.**

| Spec | Version | Role |
|------|---------|------|
| **[QSM](specs/QSM-v1.1.0.md)** | 1.1.0 | **Quantified Stewardship Model** — the domain-agnostic ontology and methodology. Defines what exists in a stewardship domain, what it needs, and what follows from that. The foundation layer. |
| **[TSS](specs/TSS-v1.2.0.md)** | 1.2.0 | **The Stewardship Standard** — the normative umbrella. Defines required objects, conformance levels (T0–T3), records, and audit rules that govern the whole stack. **The primary audit standard.** |
| **[THRIVE](specs/THRIVE-v1.1.0.md)** | 1.1.0 | **Self and Wellness Context Layer** — represents personal capacity, load, needs, routines, and recovery without reducing wellbeing to a productivity metric. Supplies the SELF context. |
| **[QSM-FAI](specs/QSM-FAI-v1.1.0.md)** | 1.1.0 | **Fiduciary AI Interface** — the conditions and constraints under which an AI agent may act as a fiduciary within a stewardship context. Defines the FiduciaryContext, action tiers, rationale, and TENURE audit records. |

Previous versions (v1.0.x) remain available in `specs/`, each marked superseded with a pointer
to its replacement. See [`CHANGELOG.md`](CHANGELOG.md) [1.1.0] for what changed and why.

### How they relate

```
TSS (normative umbrella — conformance, records, audit)
│
├── QSM (world model: ontology + needs/values + relationships)
│     └── QSM-FAI (agent interface + fiduciary rules)
│
└── THRIVE (the SELF / wellness context layer)

        └── Hardened contexts: HEARTH · CREST · CHARTER · SELF · ESTATE
```

**HEARTH (the Quantified Home)** is the first formally hardened context and serves as the normative reference implementation throughout the stack.

---

## Why it matters

AI agents are increasingly deployed in high-stakes environments — estate and property operations, organizational governance, caregiving coordination — without a lawful, machine-readable model of *who they serve, what they are authorized to do, and what duties bind them*.

Existing responsible-AI frameworks address this at the policy, audit, or behavioral level. The Stewardship Standard addresses it at the **architectural** level: an agent operating under QSM-FAI cannot act outside its declared scope, because the FiduciaryContext that licenses it to act defines that scope structurally — not as a runtime check applied after the fact.

---

## Repository structure

```
stewardship-standard/
├── README.md                     ← this file
├── CHANGELOG.md
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── AI-USE.md                     ← canonical AI-use disclosure
├── CITATION.cff
├── glossary.md
├── LICENSE-SPEC                  ← CC BY 4.0 (specification text)
├── LICENSE-SCHEMAS               ← Apache 2.0 (reference schemas)
├── .zenodo.json                  ← metadata for Zenodo DOI minting
├── specs/
│   ├── QSM-v1.1.0.md
│   ├── TSS-v1.2.0.md
│   ├── THRIVE-v1.1.0.md
│   ├── QSM-FAI-v1.1.0.md
│   └── (superseded v1.0.x versions kept alongside, marked superseded)
├── schemas/
│   ├── context.schema.json
│   ├── entity.schema.json
│   ├── relationship.schema.json
│   ├── record.schema.json
│   ├── conformance-claim.schema.json
│   ├── assignment.schema.json
│   ├── fiduciary-context.schema.json
│   ├── rationale.schema.json
│   ├── tenure-entry.schema.json
│   ├── escalation-outbox-entry.schema.json
│   └── thrive/
│       ├── self-context.schema.json
│       ├── capacity-profile.schema.json
│       ├── need.schema.json
│       ├── routine.schema.json
│       └── wellness-record.schema.json
└── samples/
    ├── hearth-context.json
    ├── hearth-fiduciary-context.json
    ├── default-conformance-claim.json
    ├── charter-template-and-instance.json
    └── escalation-outbox-entry.json
```

---

## Conformance at a glance

TSS defines four conformance levels. Each domain layer mirrors them (see TSS Appendix Z); **TSS T-level is the primary audit standard.**

| TSS | QSM | THRIVE | QSM-FAI | Meaning |
|-----|-----|--------|---------|---------|
| T0 | C0 | H0 | L0 | Observational / informal |
| T1 | C1 | H1 | L1 | Structured |
| T2 | C2 | H2 | L2 | Operational / auditable |
| T3 | C3 | H3 | L3 | Normative / full |

---

## Getting started

1. Read **[QSM](specs/QSM-v1.1.0.md)** for the conceptual foundation.
2. Read **[TSS](specs/TSS-v1.2.0.md)** for conformance and audit requirements.
3. If you are building an AI agent, read **[QSM-FAI](specs/QSM-FAI-v1.1.0.md)**.
4. If you are modeling personal capacity and wellbeing, read **[THRIVE](specs/THRIVE-v1.1.0.md)**.
5. Validate your data against the JSON schemas in [`schemas/`](schemas/); see [`samples/`](samples/) for worked examples.

---

## Openness, governance, and AI-use disclosure

This is an open standard: publicly accessible, implementable by anyone without discrimination or royalty, and transparent in how it evolves.

- **Openness.** Specification text under [CC BY 4.0](LICENSE-SPEC); reference schemas under [Apache 2.0](LICENSE-SCHEMAS). No discriminatory use restrictions.
- **Governance.** Maintained by Cinderlit (Excentropy as implementation partner). Changes are proposed and reviewed publicly via the issue tracker, recorded in [`CHANGELOG.md`](CHANGELOG.md), and ratified on a quarterly maintainer cycle. Full process in [`GOVERNANCE.md`](GOVERNANCE.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).
- **Use of AI-assisted tools.** AI tools were used substantially and under human supervision in drafting and formalizing this standard, including normative text and schemas. The author defined the framework, reviewed and validated all output, and holds full accountability; AI is not an author. The complete disclosure is in [`AI-USE.md`](AI-USE.md) and in the front matter of each specification.

## License

- **Specification text** (`specs/`, prose docs): [Creative Commons Attribution 4.0](LICENSE-SPEC). Implement, extend, and build on it freely — attribution required.
- **Reference schemas** (`schemas/`): [Apache License 2.0](LICENSE-SCHEMAS). Maximally reusable in software, including patent grant.

---

## Citation

If you reference or build on this standard, please cite it. See [`CITATION.cff`](CITATION.cff). Once the Zenodo DOI is minted, cite:

> Stokes, Caitlin. *The Stewardship Standard: QSM, TSS, THRIVE, and QSM-FAI* (v1.1.0). The Stewardship Standard, 2026. DOI: [pending — Zenodo]. https://github.com/cinderlit/stewardship-standard

---

## Contributing

This standard is open for comment and contribution. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Especially welcome: counterexamples, prior art, domain-specific use cases, and implementation experience.

---

¹ Excentropy is the official implementation partner for The Stewardship Standard, published by Cinderlit.

*© 2026 Caitlin Stokes / The Stewardship Standard. Specification text under CC BY 4.0; reference schemas under Apache 2.0.*
