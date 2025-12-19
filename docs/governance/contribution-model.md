---
title: Contribution Model
nav_order: 2
parent: Governance
---

# Contribution Model

## Purpose

This document defines **who can contribute, how contributions are made, and how responsibility is distributed** across the Nodal Robotics / NODAL ecosystem.

It is intentionally **process‑oriented**, not technical. Module‑specific contribution rules may extend this model but **must not contradict it**.

---

## Scope

This contribution model applies to:

* `nodal-workspace`
* all `nodal-*` software modules
* hardware and tooling repositories
* documentation and safety artefacts

---

## Core Principles

### 1. Contribution Is Structured Engineering Work

Contributions are not free‑form patches.
They are:

* intentional
* reviewable
* traceable
* aligned with lifecycle and safety constraints

### 2. Authority Is Contextual

Authority depends on:

* **repository scope** (workspace vs module)
* **impact** (local vs system‑wide)
* **safety relevance**

### 3. Decisions Precede Implementation

No significant contribution is merged without:

* an explicit intent (issue)
* and, when required, a documented decision (ADR)

---

## Contribution Roles

### Contributors

Anyone who:

* opens issues
* proposes changes
* submits pull requests

Contributors:

* do not merge their own PRs
* do not approve safety‑critical changes

---

### Maintainers (Module Level)

Maintainers are responsible for **a specific module or repository**.

They:

* triage issues
* review pull requests
* ensure lifecycle compliance
* enforce coding and documentation standards

They **cannot**:

* change global architecture rules
* override safety policies

---

### System Maintainers (Workspace Level)

System maintainers are responsible for:

* `nodal-workspace`
* cross‑module coherence
* lifecycle and governance enforcement

They:

* validate system‑level changes
* arbitrate cross‑module conflicts
* approve ADRs with system impact

---

### Safety Authority

A Safety Authority role is required for:

* hazard management
* safety requirements
* acceptance of residual risk

This role:

* is independent from feature ownership
* can block releases
* has veto power on safety matters

---

## Contribution Flow (Standard)

1. **Issue Creation**

   * feature, bug, documentation, or decision
   * properly typed and scoped

2. **Triage & Classification**

   * module
   * lifecycle phase
   * safety relevance

3. **Decision (if required)**

   * ADR created and approved

4. **Implementation**

   * pull request linked to issue

5. **Review & Validation**

   * technical review
   * safety review (if applicable)

6. **Merge & Traceability Update**

---

## Pull Request Rules

All pull requests must:

* reference at least one issue
* respect repository coding rules
* include documentation updates when applicable

Additional requirements apply for:

* safety‑relevant changes
* architectural changes

---

## Safety‑Relevant Contributions

A contribution is safety‑relevant if it:

* affects safety requirements
* modifies hazard mitigations
* impacts verification evidence

Such contributions require:

* explicit safety tagging
* safety authority review
* traceability updates

---

## Forbidden Practices

The following are not allowed:

* direct commits to protected branches
* undocumented architectural changes
* merging without review
* bypassing safety validation

---

## Relationship With Lifecycle

This contribution model is aligned with:

* Analysis → intent and decisions
* Development → implementation
* Verification → validation evidence
* Deployment → release control

---

## References

* Governance index
* Decision process
* Lifecycle documentation
* Safety policy
