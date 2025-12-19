---
title: Governance
nav_order: 4
has_children: true
---
# Governance

## Status

Normative — Workspace level

## Purpose

This section defines **how decisions are made, how contributions are accepted, and how releases are governed** across all NODAL projects.

Governance ensures that:

* technical decisions are explicit and traceable
* contributions align with architectural and safety constraints
* the project evolves in a controlled and auditable manner

Governance is not bureaucracy; it is an **engineering control mechanism**.

---

## Scope

The governance model applies to:

* the workspace repository
* all module repositories (`nodal-*`)
* hardware and tooling repositories
* documentation and safety artifacts

Out of scope:

* organization-level legal governance
* commercial or licensing agreements (defined elsewhere)

---

## Governance Principles

### Explicit Decisions

All significant decisions shall be:

* documented
* reviewable
* traceable

Implicit or undocumented decisions are not acceptable.

---

### Separation of Roles

Governance distinguishes between:

* **contributors** (who propose changes)
* **reviewers** (who assess correctness and impact)
* **maintainers** (who accept responsibility)

Authority is tied to responsibility, not activity volume.

---

### Safety and Architecture First

No decision may:

* violate architectural principles
* weaken safety arguments
* bypass lifecycle constraints

If a conflict arises, safety and architecture take precedence.

---

### Transparency

Governance artifacts shall be:

* publicly accessible within the organization
* versioned
* linked to issues and pull requests

Decisions must be understandable by future contributors.

---

## Governance Mechanisms

Governance is enforced through:

* **Decision process (ADR)** — how technical decisions are made
* **Contribution model** — how changes are proposed and reviewed
* **Release policy** — how versions are defined and accepted

Each mechanism is defined in a dedicated document.

---

## Relation to Lifecycle

Governance spans all lifecycle phases:

* Analysis: decision framing and approval
* Development: controlled change implementation
* Verification: acceptance of evidence
* Deployment: release and acceptance authority

Lifecycle execution without governance is invalid.

---

## Relation to GitHub

GitHub is the execution platform for governance:

* Issues capture proposals and problems
* Pull Requests capture implementation and review
* GitHub Projects provide state and visibility
* ADR documents capture decisions

Governance rules apply regardless of repository.

---

## Governance Documents

* [`decision-process.md`](decision-process.md)
* [`contribution-model.md`](contribution-model.md)
* [`release-policy.md`](release-policy.md)

---

## Summary

The governance model ensures that NODAL evolves:

* deliberately
* safely
* transparently

It provides long-term stability without preventing innovation.
