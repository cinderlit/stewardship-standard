# What Authorizes an AI Agent to Act?

*A plain-language introduction to QSM-FAI and the case for a fiduciary AI substrate.*

---

When you hand your lawyer a matter, something specific happens that is easy to miss because it's so familiar: a relationship is declared. Your lawyer now owes you duties — of care, loyalty, and disclosure — that are enforceable, that define the scope of what they're authorized to do on your behalf, and that produce an obligation to account for what they did and why. The relationship doesn't just describe what they're allowed to do. It defines what they *are* in the context of your matter.

AI agents don't have this. Not yet, and not at the layer that matters.

This is the problem that the Quantified Stewardship Model — Fiduciary AI Interface (QSM-FAI) is trying to solve. Not through policy documents, not through behavioral training, and not through access control lists — but through a data architecture that encodes the stewardship relationship itself before an agent is allowed to act.

---

## The gap current approaches leave open

There are roughly three ways people are trying to make AI agents safer and more accountable right now, and each of them solves a real problem without solving this one.

**Training-time behavioral constraints** — Constitutional AI, model specs, RLHF-based alignment — shape how an agent reasons and responds. They're genuine advances. But they address behavior at the model level, not authorization at the deployment level. An agent trained to be helpful and harmless still has no formal record of who it's serving, what it's been authorized to do on their behalf, or what duties it owes them in this specific context.

**Runtime permission checks** — tool allowlists, function calling schemas, capability gates — restrict what an agent can call. Also real, also valuable. But they define constraints negatively: here's the list of things blocked. They don't describe the stewardship domain the agent is operating within, the principal it's accountable to, or what constitutes a duty of care in this context versus that one.

**Legal and policy frameworks** — "information fiduciary" scholarship, AI governance proposals, the EU AI Act's requirements for high-risk systems — describe what duties *should* exist in law or policy. This is important work. But a policy claim that an AI "operates under fiduciary duty" is not a machine-readable fact. You can't verify it against an implementation, and you can't build on it in a downstream system.

What's missing is a layer underneath all of these: a formal, structured declaration of the relationship between an agent and the principal it serves, expressed as data, before the agent takes its first action.

---

## What fiduciary duty actually means, and why it's the right model

A fiduciary is someone who holds authority on behalf of another — a trustee, a guardian, a financial advisor, a doctor. What distinguishes a fiduciary relationship from a contractual one is that three duties attach automatically to the role: care (act in the principal's best interest), loyalty (don't serve competing interests), and disclosure (account for what you did and why). These duties don't have to be specified for each task; they're inherited from the declaration of the relationship itself.

This is the right model for AI agents in high-stakes contexts because it shifts the question from "did the agent follow the rules" to "was the agent operating within an authorized relationship in the first place." A trustee who acts outside the terms of the trust instrument isn't just breaking a rule — they're acting without authorization. The trust instrument defines what the estate is, what the beneficiaries' interests are, and what the trustee is licensed to do on their behalf. An action outside that scope isn't blocked by a check; it simply isn't authorized by the relationship.

QSM-FAI applies this logic to AI agents.

---

## The architectural move

The core object in QSM-FAI is the `FiduciaryContext` — a structured, machine-readable declaration that an agent must hold before taking any action. The spec calls it the agent's "license to act."

A `FiduciaryContext` contains: who declared it (the steward), what scope of action has been delegated, what the entity set looks like (the people, systems, responsibilities, and relationships the agent is acting within), what tier of action requires human approval, what the spending limit is, what the audit log reference is, and what the current status is. It is not a list of permitted operations. It is a description of the stewardship domain itself — and an agent that acts outside that domain isn't violating a constraint, it's acting without a license.

This distinction matters. Negative constraints scale badly: you cannot enumerate every out-of-scope action in advance, and a novel action that wasn't on the blocklist can slip through. Positive scope definition scales differently: if the context doesn't cover a domain, no action within that domain is authorized, including ones nobody thought to block.

The spec's conformance rule is blunt about this: an agent without an active `FiduciaryContext` must not act. Full stop.

---

## What else the spec defines

The `FiduciaryContext` is the structural foundation, but QSM-FAI specifies several things that build on it.

A **delegation chain** records every steward who authorized the agent to act — primary, delegate, observer — with the scope of each grant and an optional track record of past outcomes. This is how you represent "I authorized this agent, and it earned its current autonomy tier through a history of acceptable decisions" as data rather than as a claim.

**Action tiers** (L0 through L3) define the autonomy gradient. A tier-0 action is observational — read-only, no notification required. A tier-3 action is irreversible, high-stakes, and requires human approval before execution. The tier is set per context, not per agent, which means the same agent operating in a household context and a business context can have different authorization ceilings for the same class of action.

**TENURE records** are the disclosure duty made machine-readable: a timestamped audit entry for every action the agent takes, linked to the entity it acted on, the rationale that justified the action, and the QSM model elements that authorized it. This is what "accounting for what you did and why" looks like structurally.

The **escalation taxonomy** formalizes the cases where an agent must stop and surface a decision to the human: uncertain decisions, scope boundary questions, rule conflicts, tool failures, concurrent write risks. Each has a required field set in the outbox entry. The escalation outbox is a standing, queryable collection of unresolved escalations — not a notification that disappears, but a record that persists until the steward acts.

---

## Why now

AI agents are moving from demos to real deployments in high-stakes environments — managing homes, coordinating care, running business operations, advising on finances. The industry's current toolkit for governing this transition is primarily behavioral: make the model align better, add more guardrails, write better system prompts. These are necessary. They're not sufficient.

What's needed alongside them is an architectural layer that makes the agent's relationship to its principal formal, inspectable, and persistent — something that can be referenced by an audit, extended by a downstream system, and verified rather than merely asserted. The fiduciary concept from law has been doing this work for human professionals for centuries. The question QSM-FAI is asking is: what does that look like as a data structure?

That's a question with a concrete answer. The spec, schemas, and a working reference implementation are at [github.com/cinderlit/stewardship-standard](https://github.com/cinderlit/stewardship-standard). DOI: [10.5281/zenodo.20436569](https://doi.org/10.5281/zenodo.20436569). Counterexamples, prior art, and implementation experience are especially welcome.

---

*QSM-FAI is part of The Stewardship Standard, a layered open standard for quantified stewardship maintained by Cinderlit. Specification text: CC BY 4.0. Reference schemas: Apache 2.0.*
