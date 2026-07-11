> Rendering of `inputs-memory-canon-pipeline.md` @ 2026-07-11. **Candidate, not normative.** Gated on the
> `inputs-memory-allocation-ontology.md` review (2026-10-01). Do not cite as settled standard text.
> Formal register; source of the underlying model is the internal pipeline note.

# Candidate sub-model: Inputs, Encoding, and Retention (Layer 4, Memory)

**Status: candidate.** This section proposes a sub-model for the Memory layer of the Quantified
Stewardship Model. It is not yet normative. It is published here as a candidate pending the internal
review scheduled for 2026-10-01, and it must not be treated as a conformance requirement before it is
accepted.

## Motivation

The Memory layer today names the kinds of retained knowledge (episodic, semantic,
procedural, priming) but does not specify how an input becomes a retained fact, nor what a conformant
implementation must preserve when it does. Stewardship systems that cannot show where a durable fact came
from cannot be audited, which is the property the model exists to protect.

## The model

An input enters as an **episodic** record: specific, time-stamped, and carrying its
provenance (who, what, when, where, source). **Encoding** determines whether an episodic record is
retained, and is governed by four factors: attention, repetition, salience, and context. A durable
**semantic** fact is one that has been distilled from one or more episodic records. Distillation
generalizes, but it does not sever origin.

## Proposed statements

- A conformant memory implementation SHOULD represent new inputs as episodic records before any
  distillation into semantic facts.
- A conformant memory implementation MUST retain, for every semantic fact, a reference to the episodic
  record or records it was distilled from. A semantic fact with no traceable origin is not conformant.
- A conformant memory implementation SHOULD treat retention as an outcome of encoding, not as a default.
  Inputs that are not encoded are expected to decay, and decay is a valid state, not a defect.

## Relationship to existing layers

This sub-model sits inside Layer 4 (Memory) and connects upward to
practice (retained facts are what practice draws on) and downward to intake (episodic records are what
intake produces). It reuses the existing memory-type vocabulary rather than introducing a parallel one.

## Why it waits

The full input-to-retention model is still being validated internally against real use.
Publishing it as normative before it has answered real questions would place a conformance obligation on
an unproven model, which the standard's own governance discipline forbids. It graduates from candidate to
normative only if it proves out at the review.
