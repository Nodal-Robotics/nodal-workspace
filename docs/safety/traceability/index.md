---
title: Traceability
nav_order: 5
parent: Safety Case
---

# Traceability

Traceability ensures that **every safety claim is justified by evidence** and that all safety-related decisions can be audited end-to-end.

This section defines the **traceability model** used across the Nodalworkspace.

---

## 🎯 Purpose

Traceability enables:

- verification that all hazards are mitigated
- proof that safety requirements are implemented
- confidence that changes do not break safety assumptions
- preparation for external audits or certification

Traceability is not optional for safety-related work.

---

## 🧩 Scope

Traceability applies to:

- hazards
- safety requirements
- architectural decisions (ADR)
- implementation work
- verification artifacts
- deployment constraints

It spans **multiple repositories**, but is governed centrally.

---

## 🔗 Traceability Chain

The canonical safety traceability chain is:

- Hazard
- Safety Requirement
- Design / ADR
- Implementation (Code / HW)
- Verification Evidence
- Safety Claim


Breaking any link invalidates the safety claim.

---

## 🧠 Traceability Principles

- **Explicit links only** (no implicit assumptions)
- **Bidirectional traceability**
- **Tool-supported, human-readable**
- **Version-aware**

Traceability must survive:
- refactoring
- repository splits
- long-term maintenance

---

## 🛠️ Implementation Strategy

Traceability is implemented using:

- GitHub Issues (typed and linked)
- Pull Requests
- Markdown documentation
- Project fields and relations

No external ALM tool is required.

---

## 📂 Structure

This section contains:

- **Traceability Model**  
  Defines entities, relationships, and rules.

- **Evidence Expectations**  
  Defines what counts as acceptable proof.

---

## 📌 References

- Safety Requirements
- Safety Lifecycle
- Governance / Decision Process