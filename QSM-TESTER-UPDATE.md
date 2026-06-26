# QSM — What's Changed and Why
### An update for people who tested the original stack

---

Thank you for spending time with the first version of QSM. Your feedback on the original six-piece stack helped clarify what was working and where the model had gaps. This document explains what changed, what stayed the same, and why — so you don't have to read the full specs to get oriented.

The short version: **the foundation is intact. We filled in three things that were missing and made the whole thing easier to enter.**

---

## What stayed the same

- The five context types: SELF, HEARTH, ESTATE, CHARTER, CREST
- The six operational layers you know from the original stack: Governance, Intake, Execution, Observation, Documentation, Dashboard — several of these were renamed in the new eight-layer architecture (see mapping below)
- All four specification documents: QSM, THRIVE, TSS, QSM-FAI
- Your conformance level claims — anything that was conformant before is still conformant
- The core vocabulary: context, entity, role, need, constraint, risk, action, record

Nothing you built or documented against the original stack is broken.

---

## What changed, and why

### 1 — The SELF needs model is now Max-Neef, not Maslow

**What was there:** The SELF context used Maslow's five-level hierarchy (Physiological → Safety → Belonging → Esteem → Self-Actualization) to organize management categories.

**What's there now:** Max-Neef's taxonomy of nine fundamental human needs, used simultaneously rather than sequentially.

The nine needs: Subsistence, Protection, Affection, Understanding, Participation, Leisure, Creation, Identity, Freedom.

**Why we changed it:**

Maslow's hierarchy is intuitive but empirically shaky — decades of research haven't been able to replicate the sequential activation idea. More importantly, it conflicts with what THRIVE is actually trying to do. If your finances are rocky, Maslow implies you can't have meaningful Identity or Freedom needs active at the same time. That's not how people work, and it's not how THRIVE is designed.

Max-Neef fixes this. All nine needs are always present. What varies is which *satisfiers* you're using — the specific practices, resources, and routines that address each need. This maps directly onto how QSM management categories already work: a management category is a satisfier. The conceptual fit is much cleaner.

The change also adds a "satisfier type" dimension — whether a practice genuinely addresses a need, addresses multiple needs at once (synergic), or only appears to while actually not helping (pseudo). This is analytically useful in a way Maslow couldn't be.

**What this means for you:** If you built a SELF model against Maslow levels, your management categories are still valid — they just need re-tagging to the new need vocabulary. The SELF model now has **16 management categories** (up from 15): Information & Digital Management was split into Information & Knowledge Management and Digital Autonomy & Privacy Management to give the Digital world domain and Freedom need adequate Primary coverage.

---

### 2 — Two layers were added to the operating model

**What was there:** Six layers — Governance, Intake, Execution, Observation, Documentation, Dashboard.

**What's there now:** Eight layers. The six you know map to renamed counterparts; two were added:

**Intent** (now Layer 1, sits above Governance; formerly Identity/Intent)
The "why" layer. Who is this context for, what is it trying to become, what values orient its decisions? This was always implicitly present — a context declaration gestures at it — but it wasn't a first-class layer. Without it, QSM is a well-organized system executing against unstated purposes. For the SELF context especially, the question "who am I trying to become" is the thing that makes everything else legible.

**Adaptation** (now Layer 8, sits after Signal; formerly Feedback/Learning)
The adaptation loop. Observation captures what happened. Memory stores it. But neither one formally closes the loop by asking: "what do we change about how we operate based on what we learned?" Without this layer, a QSM implementation monitors but never adapts. Adaptation is what turns the system from a record-keeper into something that improves over time.

**What this means for you:** Your existing implementation maps cleanly to Layers 2–7 of the new model (with renamed layers — see mapping table below). You don't need to rebuild anything. If you want to claim full conformance with the new architecture spec (QSM-ARCH), you'd add Intent and Adaptation. If not, your existing conformance level is still valid.

---

### 3 — THRIVE (SELF context) got three additions

The THRIVE spec now formally supports three concepts that were missing:

**World domains** — Physical, Digital, Metaphysical. The original THRIVE was implicitly about the physical world (body, health, space, finances). It had nothing to say about the digital world (attention, online presence, information diet, notification load) or the inner/metaphysical world (meaning, values, psychological interior, sense of purpose). These are real and distinct stewardship domains with their own failure modes. A conformant THRIVE implementation now should declare which worlds it's actively stewarding.

**Developmental context** — An optional declaration of where someone is in their life arc (life stage, psychosocial stage, role transitions). This doesn't change which needs are present — it changes what satisfiers are appropriate and what's salient right now. Think of it as a modifier, not a replacement for the needs model.

**Temporal cycle profile** — Formal support for cycles that affect capacity: circadian rhythms, hormonal cycles, seasonal patterns, illness recovery. These already existed implicitly in the capacity/load model. Now they can be declared explicitly so routines and defaults can respond to them automatically.

---

### 4 — The architecture is now a formal specification

**What was there:** The six-layer operating model existed in the Excel working models but not as a normative document. It was implied, not specified.

**What's there now:** QSM-ARCH v1.1.0 — a specification document that defines the eight layers (each with a full per-layer contract and anti-patterns), the engines within each layer, five cross-cutting planes that apply to every object across all layers (Lifecycle State, Ownership, Versioning/Provenance, Metrics/Thresholds, Security/Privacy), context lifecycle (§6.6), and conformance-scale reconciliation with QSM/TSS (§8.3).

This matters for anyone building tools on top of QSM or writing conformance statements. The architecture was always there conceptually — now it has the same standing as the other specs.

---

### 5 — There's now a front door

**What was there:** To understand QSM, you started with the QSM spec and worked through the stack from the beginning.

**What's there now:** QSM-OVERVIEW — a conceptual overview document that sits in front of the entire stack. It introduces the model through three orienting questions, explains all five context types, shows how the specifications relate to each other, and includes a worked example for each context. Both new readers and AI agents implementing the stack read this first.

---

## The short version — before and after

| | Original stack | Updated stack |
|---|---|---|
| **SELF needs framework** | Maslow (5 hierarchical levels) | Max-Neef (9 simultaneous needs) |
| **Operating layers** | 6 | 8 (same 6 renamed + Intent + Adaptation) |
| **THRIVE world domains** | Implied physical only | Physical, Digital, Metaphysical declared explicitly |
| **Architecture spec** | Implied in Excel models | QSM-ARCH v1.1.0 (formal specification) |
| **SELF management categories** | 15 (Maslow-era) | 16 (Max-Neef; digital category split) |
| **Entry point** | QSM spec directly | QSM-OVERVIEW (conceptual front door) |
| **Existing conformance claims** | — | All still valid |
| **Context types** | SELF, HEARTH, ESTATE, CHARTER, CREST | Unchanged |
| **Core spec documents** | QSM, THRIVE, TSS, QSM-FAI | Same four + QSM-ARCH added |

---

## Layer name mapping (original → new)

If you built against the original six-layer model or the first eight-layer draft, use this table to reconcile your implementation:

| Original name | New name (QSM-ARCH v1.1.0) |
|---|---|
| Identity / Intent | **Intent** |
| Governance | Governance (unchanged) |
| Intake | Intake (unchanged) |
| Knowledge / Documentation | **Memory** (Documentation is a function inside Memory) |
| Execution | **Practice** |
| Observation | Observation (unchanged) |
| Dashboard / Signal | **Signal** |
| Feedback / Learning | **Adaptation** |

See [QSM-LAYER-MATRIX.md](specs/QSM-LAYER-MATRIX.md) for the question mapping, key structural rules, and cross-cutting planes.

---

## What we'd love your feedback on

If you're willing to review the updated stack, the most useful things to look at are:

**The Max-Neef mapping** — Does the mapping of management categories to the nine needs feel right? Are there categories that feel misclassified? Are there needs that feel underserved?

**The two new layers** — Do Intent and Adaptation feel like genuine additions or like things that could live inside the existing layers? Where would you have put them?

**The worked examples in QSM-OVERVIEW** — Are they concrete enough? Do they make the model feel usable for real situations? Where do they feel off?

**The THRIVE additions** — Do the three new dimensions (world domains, developmental context, temporal cycles) feel like they belong in a personal stewardship spec, or do they feel like scope creep?

Any format works — notes in a doc, a conversation, a voice memo. We're specifically not looking for typo corrections at this stage; we're looking for places where the model doesn't match how you think about stewardship in practice.

---

*QSM Tester Update — 2026-06-25 · Excentropy*  
*Questions: reach out directly to Caitlin*
