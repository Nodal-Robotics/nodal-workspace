---
title: System Documentation
nav_order: 1
permalink: /
---

# Nodal Robotics – System Documentation

Welcome to the **Nodal Robotics workspace documentation**.

This documentation defines the **global system foundations** shared across all Nodal Robotics projects:
architecture principles, lifecycle processes, safety governance, and engineering rules.

> ⚠️ This repository does **not** contain module-level documentation.  
> Each software or hardware module maintains its own technical documentation in its dedicated repository.

---

## 1. Documentation Scope

This documentation applies to:

- System-level architecture and assumptions
- Engineering and safety governance
- Development lifecycle definition
- Safety Case structure and traceability
- Tooling, CI, and contribution rules

It is intended for:

- System architects
- Safety engineers
- Technical leads
- Auditors and certification bodies
- Contributors working on Nodal Robotics projects

---

## 2. System Lifecycle

The Nodal Robotics system follows a structured lifecycle, defined in [`/lifecycle`](./lifecycle/index.md).

### Lifecycle Phases

| Phase | Purpose |
|------|--------|
| **Analysis** | Requirements, hazards, feasibility, assumptions |
| **Development** | Design and implementation of features |
| **Verification** | Testing, validation, evidence collection |
| **Deployment** | Release, integration, operational readiness |

Each phase:
- is tracked via GitHub Projects
- produces auditable artifacts
- may have safety implications

➡️ See: **Lifecycle documentation**  
[`lifecycle/index.md`](./lifecycle/index.md)

---

## 3. Safety Case Overview

Safety is treated as a **system property**, not a feature.

The Safety Case is documented under [`/safety`](./safety/index.md) and provides a structured justification that the system is acceptably safe for its intended use.

### Safety Case Structure

The Safety Case is built from:

1. **Hazard Management**
   - Hazard identification
   - Risk classification
   - Risk acceptance criteria

2. **Safety Requirements**
   - Derived from hazards
   - Allocated to modules or processes
   - Managed through change control

3. **Verification & Evidence**
   - Tests, reviews, analyses
   - Linked to requirements and hazards

4. **Traceability**
   - End-to-end linkage:
     hazard → requirement → feature → evidence

➡️ See:  
[`safety/index.md`](./safety/index.md)

---

## 4. Architecture Decision Records (ADR)

Architecture Decision Records (ADR) capture **significant technical or organizational decisions** made at system level.

ADR answer the question:

> *Why was this solution chosen over alternatives?*

They are:
- concise
- decision-focused
- immutable once accepted

ADR are located in ``docs/governance/adr/``

### When is an ADR required?

An ADR is required when a decision:
- affects multiple modules
- impacts safety, lifecycle, or compliance
- introduces a long-term constraint
- changes architectural principles

ADR are typically **derived from GitHub issues**, not written in isolation.

➡️ See:
- ADR index: [`governance/adr/index.md`](./governance/adr/index.md)
- ADR template: [`governance/adr/template.md`](./governance/adr/template.md)

---

## 5. Relation to GitHub Projects

This documentation is **not a task tracker**.

Instead:
- GitHub Projects manage **work and status**
- Documentation provides **structure and rationale**

Every documented concept (hazard, requirement, decision):
- has a corresponding issue or item in GitHub Projects
- is referenced via links
- remains traceable and auditable

---

## 6. How to Navigate This Documentation

- **Start here**: this page
- **Understand the system**: `/architecture`
- **Understand the process**: `/lifecycle`
- **Understand safety**: `/safety`
- **Understand decisions**: `/governance`

---

## 7. Change Management

All changes to this documentation:
- follow the defined governance process
- may require an ADR
- must preserve traceability and safety consistency

---

> This documentation is a **living system**, but its structure is stable by design.
