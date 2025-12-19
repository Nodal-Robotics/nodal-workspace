---
title: Safety Requirements
nav_order: 3
parent: Safety Case
---

# Safety Requirements

This section defines how **safety requirements (SR)** are specified, structured, allocated, and managed across the  NODAL ecosystem.

Safety requirements are **normative**, **verifiable**, and **traceable** artifacts.
They represent the contractual link between:
- identified hazards
- accepted risk levels
- concrete technical mitigations

---

## 🎯 Purpose

The objectives of safety requirements are to:

- translate hazards into enforceable constraints
- ensure consistent mitigation strategies across modules
- enable objective verification and auditability
- support long-term maintainability and certification readiness

---

## 🧩 Scope

This section applies to:

- **Global safety requirements** defined at workspace level
- **Derived safety requirements** allocated to:
  - software modules
  - hardware components
  - tooling or process constraints

Module-specific SR implementations **must not redefine formats or rules** defined here.

---

## 🧠 Core Principles

Safety requirements must be:

- **Unambiguous**  
- **Testable / verifiable**
- **Traceable** to hazards
- **Version-controlled**
- **Change-managed**

No safety requirement may exist without:
- a parent hazard
- a defined verification strategy

---

## 📂 Structure

This section is organized as follows:

- **Requirement Format**  
  Defines how safety requirements are written and identified.

- **Allocation Rules**  
  Defines how requirements are mapped to modules, hardware, or processes.

- **Change Management**  
  Defines how safety requirements evolve over time.

---

## 🔗 Integration with GitHub

Each safety requirement is tracked as:
- a GitHub Issue (type: `Safety Requirement`)
- linked to:
  - one or more hazards
  - implementation issues
  - verification evidence

GitHub Projects are used as the **execution layer**, not as the source of truth.

---

## 📌 References

- Hazard Management
- Safety Lifecycle
- Traceability Model
