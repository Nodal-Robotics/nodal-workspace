# Decision Process

## Status

Normative — Workspace level

## Purpose

This document defines **how technical and architectural decisions are made, documented, reviewed, and enforced** across all NODAL projects.

The goal is to ensure that decisions are:

* explicit
* traceable
* justified
* durable over time

Decisions are treated as **engineering artifacts**, not informal discussions.

---

## Scope

The decision process applies to:

* architectural choices
* interface definitions
* safety-related trade-offs
* lifecycle or governance changes
* significant technical deviations

Out of scope:

* day-to-day implementation details
* purely cosmetic changes

---

## Decision Types

Decisions are categorized to determine the required rigor:

| Type          | Description                            |
| ------------- | -------------------------------------- |
| Architectural | System structure, boundaries, patterns |
| Interface     | APIs, protocols, contracts             |
| Safety        | Hazard mitigations, risk acceptance    |
| Lifecycle     | Process or workflow changes            |
| Tooling       | Build, CI, verification tools          |

Higher criticality decisions require stronger justification.

---

## When a Decision Is Required

A formal decision is required when:

* multiple viable options exist
* a choice has long-term impact
* safety or architecture is affected
* a rule or assumption is changed

If in doubt, treat it as a decision.

---

## Decision Artifacts (ADR)

Decisions shall be documented using **Architecture Decision Records (ADR)**.

An ADR:

* captures context
* documents alternatives
* explains the chosen option
* records consequences

ADRs are immutable once accepted.

---

## ADR Lifecycle

### 1. Proposal

* Decision need is identified
* Context and problem are described
* Alternatives are listed

---

### 2. Review

* Technical and safety impacts are assessed
* Stakeholders provide input
* Trade-offs are challenged

---

### 3. Acceptance

* A maintainer approves the decision
* Rationale is finalized
* Status is set to *Accepted*

---

### 4. Enforcement

* Implementation shall follow the decision
* Deviations require a new ADR

---

## Relation to GitHub Issues

Decisions are typically triggered by:

* feature issues
* safety or hazard issues
* architectural refactoring proposals

The issue shall:

* reference the ADR
* not duplicate the decision content

Issues track execution; ADRs capture intent.

---

## Decision Authority

Decision authority depends on impact:

* Module-level decisions: module maintainers
* Workspace-level decisions: workspace maintainers
* Safety-critical decisions: designated safety authority

Authority implies accountability.

---

## Conflict Resolution

If consensus cannot be reached:

* escalate to higher governance level
* prioritize safety and architectural integrity
* document dissenting opinions if relevant

Undocumented conflicts are not acceptable.

---

## Anti-Patterns

The following practices are prohibited:

* undocumented decisions
* retroactive ADRs without justification
* modifying accepted ADRs
* bypassing the decision process

---

## Relation to Lifecycle

Decisions typically:

* originate during Analysis
* constrain Development
* are validated during Verification
* remain effective through Deployment

---

## Summary

The decision process ensures that NODAL evolves through **deliberate, reviewable choices**.

It protects the project from erosion of intent, architectural drift, and safety regression.
