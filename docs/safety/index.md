---
title: Safety
nav_order: 5
has_children: true
---

# Safety Case Overview

## Purpose

This section defines the **global safety framework** for the NODAL ecosystem.

It does **not** describe the safety of a specific robot or product.
Instead, it defines **how safety is engineered, justified, documented, and accepted** at the system level.

The objective is to ensure that safety is:

* systematic
* traceable
* auditable
* compatible with industrial safety standards

---

## Scope of the Safety Case

The safety case defined here applies to:

* the NODAL framework
* system integration via `nodal-workspace`
* cross-module interactions
* lifecycle and governance processes

It does **not replace**:

* module-level safety analyses
* product-specific certification activities

Instead, it provides a **common safety backbone** on top of which those activities can be built.

---

## Safety Philosophy

Nodal Robotics follows a **design-for-safety** approach inspired by automotive and aerospace practices.

Key principles:

* safety is addressed **from analysis to deployment**
* hazards are managed, not ignored
* decisions impacting safety are explicit
* residual risk is formally accepted

Safety is considered a **system property**, not a feature.

---

## Safety Case Structure

The global safety case is structured into the following pillars:

### 1. Safety Policy

Defines:

* safety objectives
* roles and responsibilities
* authority and veto rules

📄 [`safety-policy.md`](./safety-policy.md)

---

### 2. Scope and Assumptions

Defines:

* system boundaries
* environmental assumptions
* operational constraints

📄 [`safety-scope-and-assumptions.md`](./safety-scope-and-assumptions.md)

---

### 3. Hazard Management

Defines how hazards are:

* identified
* classified
* mitigated
* accepted

📁 `hazard-management/`

---

### 4. Safety Requirements

Defines:

* how safety requirements are written
* how they are allocated
* how changes are managed

📁 `safety-requirements/`

---

### 5. Safety Lifecycle

Defines how safety activities align with the engineering lifecycle:

* analysis
* development
* verification
* deployment

📁 `safety-lifecycle/`

---

### 6. Traceability and Evidence

Defines:

* traceability models
* evidence expectations
* linkage between hazards, requirements, and verification

📁 `traceability/`

---

## Relationship With Governance and Lifecycle

The safety case is tightly integrated with:

* **Governance**

  * decision authority
  * release approval
  * escalation paths

* **Lifecycle**

  * analysis → hazard identification
  * development → mitigation implementation
  * verification → evidence generation
  * deployment → risk acceptance

Safety considerations may:

* block a release
* require architectural decisions (ADR)
* override schedule constraints

---

## Safety and GitHub Projects

Safety activities are tracked using GitHub Projects:

* hazards, safety requirements, and mitigations are represented as issues
* lifecycle state is reflected via project fields
* traceability is achieved through explicit issue linking

GitHub is used as a **living safety case**, not just a task tracker.

---

## Safety Authority

A dedicated **Safety Authority** role exists to:

* review safety-relevant changes
* approve residual risk
* validate safety readiness for release

This role is independent from feature ownership and delivery pressure.

---

## Intended Audience

This safety case is intended for:

* system engineers
* safety engineers
* maintainers
* auditors and reviewers

It is written to be:

* explicit
* conservative
* defensible

---