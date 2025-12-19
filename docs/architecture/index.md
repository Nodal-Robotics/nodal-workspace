---
title: Architecture
nav_order: 2
has_children: true
status: <draft/normative/informative>
related:
  - "System boundaries"
  - "Architectural assumptions"
  - "Modularity principles"
  - "Architecture decisions"

---

# System Architecture Overview

## 1. Purpose

This document defines the **system-level architectural vision** of the NODAL ecosystem.

It establishes:

* what the NODAL system *is*
* how responsibilities are partitioned
* which architectural principles are **mandatory**

This document is **normative** and applies to all NODAL-related projects.

---

## 2. Scope

This document covers:

* system boundaries and roles
* high-level decomposition principles
* interaction model between components

This document does **not** cover:

* module internal implementation details
* APIs or function-level design
* performance benchmarks or tuning

Module-level design is documented in each module repository.

---

## 3. Architectural Intent

NODAL is designed as a **modular robotics system framework**, inspired by
**automotive ECU-based architectures**.

The intent is to enable:

* independent development of functional units
* controlled integration at system level
* long-term maintainability and evolution
* safety-oriented reasoning and traceability

> A NODAL system is composed, not handcrafted.

---

## 4. System Decomposition Model

The system is decomposed into **independent modules** interacting through
**explicitly defined interfaces**.

### 4.1 Module Definition

A module is:

* a self-contained functional unit
* with a clearly defined responsibility
* owning its internal state and behavior

A module:

* can be developed, tested, and versioned independently
* exposes only its declared interfaces
* does not rely on internal knowledge of other modules

---

### 4.2 Workspace Role

The **workspace**:

* defines global rules and constraints
* orchestrates integration
* provides governance and tooling

The workspace:

* does not implement functional behavior
* does not duplicate module documentation

---

## 5. Interaction Principles

All interactions between modules must:

* be explicit
* be documented
* respect ownership boundaries

Implicit coupling is **forbidden**.

Allowed interaction mechanisms include:

* defined software interfaces
* declared data contracts
* controlled communication channels

---

## 6. Separation of Concerns

The architecture enforces strict separation between:

* **System definition** (workspace)
* **Functional implementation** (modules)
* **Execution and tracking** (GitHub Projects)
* **Rationale and justification** (ADR)

Each concern has its own artifacts and lifecycle.

---

## 7. Safety and Architecture

Architecture decisions directly impact system safety.

Therefore:

* architectural constraints feed the Safety Case
* hazards may result in architectural requirements
* major architectural choices require ADR

Safety considerations are treated as **first-class inputs** to architecture.

---

## 8. Evolution and Stability

The architecture is designed to be:

* stable at its core
* extensible at its edges

Changes to architectural principles:

* are exceptional
* require an ADR
* must consider backward compatibility and safety impact

---

## 9. Related Documents

* System boundaries: `system-boundaries.md`
* Architectural assumptions: `assumptions.md`
* Modularity principles: `modularity-principles.md`
* Architecture decisions: `../governance/adr/`

---

> This document defines the *shape* of the system.
> Everything else must fit within it.
