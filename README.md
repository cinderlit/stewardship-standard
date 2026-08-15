# The Stewardship Standard

**An open standard for making stewardship legible, measurable, and safely automatable — and the first open standard designed explicitly as a fiduciary AI substrate.**

[![License: CC BY 4.0](https://img.shields.io/badge/Spec%20License-CC%20BY%204.0-blue.svg)](LICENSE-SPEC)
[![License: Apache 2.0](https://img.shields.io/badge/Schema%20License-Apache%202.0-green.svg)](LICENSE-SCHEMAS)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.20436569-blue.svg)](https://doi.org/10.5281/zenodo.20436569)

**Author:** Caitlin Stokes
**Publisher:** Cinderlit ([cinderlit.com](https://cinderlit.com))
**Standard home:** The Stewardship Standard ([stewardshipstandard.org](https://stewardshipstandard.org))
**Implementation partner:** Excentropy ([excentropy.com](https://excentropy.com))¹
**Status:** Final Draft — Public Release Candidate
**First published:** 2026-05-28
**Current release:** v1.2.0 (2026-06-25) — see [`CHANGELOG.md`](CHANGELOG.md)

---

## What this is

The Stewardship Standard is a layered open standard for representing people, places, systems, responsibilities, needs, values, and relationships in a way that makes **stewardship** — the responsible, values-aligned care of resources, relationships, and systems — legible, measurable, and improvable for both humans and AI agents.

It is built so that an AI agent can act on behalf of a human principal only within a formally declared scope, with the legal duties of care, loyalty, and disclosure encoded in the data architecture itself rather than bolted on as a policy layer. To our knowledge, **QSM-FAI is the first open standard designed explicitly as a fiduciary AI substrate.**

---

## The specification stack

The standard is composed of interdependent specifications. **TSS is the normative umbrella; the other specs are domain layers it governs.**

| Spec | Version | Role |
|------|---------|------|
| **[QSM-OVERVIEW](specs/QSM-OVERVIEW-v1.0.md)** | 1.0.0 | **Conceptual front door** — three orienting questions, five contexts, how the specs relate. Read this first. |
| **[QSM](specs/QSM-v1.1.0.md)** | 1.1.0 | **Quantified Stewardship Model** — the domain-agnostic ontology and methodology. Defines what exists in a stewardship domain, what it needs, and what follows from that. |
| **[QSM-ARCH](specs/QSM-ARCH-v1.2.0.md)** | 1.2.0 | **Layer and Engine Operating Model** — eight structural layers, per-layer contracts, cross-cutting planes, context lifecycle. The bridge between doctrine and running systems. |
| **[TSS](specs/TSS-v1.2.0.md)** | 1.2.0 | **The Stewardship Standard** — the normative umbrella. Defines required objects, conformance levels (T0–T3), records, and audit rules. **The primary audit standard.** |
| **[THRIVE](specs/THRIVE-v1.1.0.md)** | 1.1.0 | **Self and Wellness Context Layer** — personal capacity, load, needs, routines, and recovery. Supplies the SELF context. |
| **[QSM-FAI](specs/QSM-FAI-v1.3.0.md)** | 1.3.0 | **Fiduciary AI Interface** — conditions under which an AI agent may act as a fiduciary within a stewardship context. |
| **[QSM-GLOSSARY](specs/QSM-GLOSSARY.md)** | 1.0.0 | **Vocabulary reference** — canonical definitions for terms used across the stack (non-normative). |

Previous versions remain available in `specs/`, each marked superseded with a pointer
to its replacement. See [`CHANGELOG.md`](CHANGELOG.md) for what changed and why.

### How they relate

```
TSS (normative umbrella — conformance, records, audit)
│
├── QSM-OVERVIEW (conceptual entry point)
├── QSM-ARCH (eight-layer operating model)
├── QSM-GLOSSARY (shared vocabulary)
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
├── glossary.md                   ← legacy table; see specs/QSM-GLOSSARY.md
├── LICENSE-SPEC                  ← CC BY 4.0 (specification text)
├── LICENSE-SCHEMAS               ← Apache 2.0 (reference schemas)
├── .zenodo.json                  ← metadata for Zenodo DOI minting
├── specs/
│   ├── QSM-OVERVIEW-v1.0.md
│   ├── QSM-ARCH-v1.2.0.md
│   ├── QSM-GLOSSARY.md
│   ├── QSM-LAYER-MATRIX.md
│   ├── QSM-v1.1.0.md
│   ├── TSS-v1.2.0.md
│   ├── THRIVE-v1.1.0.md
│   ├── QSM-FAI-v1.3.0.md
│   └── (superseded versions kept alongside, marked superseded)
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
| — | — | H4 | — | Integrated (THRIVE: world domains, intent profile, developmental/temporal context) |

QSM-ARCH **A-levels** (A0–A3) measure architectural completeness separately from the C/T/H/L ladder. See TSS Appendix Z.3 and QSM-ARCH §8.3.

---

## Getting started

1. Read **[QSM-OVERVIEW](specs/QSM-OVERVIEW-v1.0.md)** for the conceptual foundation.
2. Read **[QSM](specs/QSM-v1.1.0.md)** and **[QSM-ARCH](specs/QSM-ARCH-v1.2.0.md)** for the ontology and operating model.
3. Read **[TSS](specs/TSS-v1.2.0.md)** for conformance and audit requirements.
4. If you are building an AI agent, read **[QSM-FAI](specs/QSM-FAI-v1.3.0.md)**.
5. If you are modeling personal capacity and wellbeing, read **[THRIVE](specs/THRIVE-v1.1.0.md)**.
6. Use **[QSM-GLOSSARY](specs/QSM-GLOSSARY.md)** for shared vocabulary.
7. Validate your data against the JSON schemas in [`schemas/`](schemas/); see [`samples/`](samples/) for worked examples.

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

If you reference or build on this standard, please cite it. See [`CITATION.cff`](CITATION.cff):

> Stokes, Caitlin. *The Stewardship Standard: QSM, TSS, THRIVE, and QSM-FAI* (v1.2.0). The Stewardship Standard, 2026. DOI: [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569). https://github.com/cinderlit/stewardship-standard

---

## Contributing

This standard is open for comment and contribution. See [CONTRIBUTING.md](CONTRIBUTING.md) and [GOVERNANCE.md](GOVERNANCE.md). Especially welcome: counterexamples, prior art, domain-specific use cases, and implementation experience.

---

¹ Excentropy is the official implementation partner for The Stewardship Standard, published by Cinderlit.

*© 2026 Caitlin Stokes / The Stewardship Standard. Specification text under CC BY 4.0; reference schemas under Apache 2.0.*
