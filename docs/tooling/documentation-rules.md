---
title: Documentation Rules
nav_order: 1
parent: Tooling
---

# Documentation Rules

This document defines the rules governing **engineering documentation** within the  NODAL ecosystem.

Documentation is treated as a **first-class engineering artifact**.

---

## 🎯 Purpose

Documentation exists to:

- capture intent and rationale
- support review and audit
- enable long-term maintainability
- ensure consistency across repositories

Documentation is not marketing material.

---

## 🧠 Documentation Principles

All documentation must be:

- accurate
- explicit
- reviewable
- version-controlled
- aligned with the system state

Outdated documentation is considered **incorrect documentation**.

---

## 🧩 Scope

These rules apply to:

- architectural documentation
- lifecycle and governance documents
- safety case documentation
- tooling documentation
- ADRs

They do not apply to:
- user-facing manuals
- tutorials (unless explicitly stated)

---

## 📝 Format and Structure

- Markdown is mandatory
- Files must be human-readable without tooling
- Clear headings and logical structure are required
- Each document must state its scope and purpose

---

## 🔗 Traceability Requirements

Documentation must:

- reference related issues, PRs, or ADRs when relevant
- align with implemented behavior
- evolve alongside the system

Safety-related documentation must be traceable to:
- safety requirements
- hazards
- verification activities

---

## 🔁 Change Management

All documentation changes must:

- be made via pull request
- include rationale for the change
- be reviewed

For safety-relevant documentation:
- impact analysis is mandatory
- traceability must be updated

---

## 🛡️ Safety Constraints

Documentation that contributes to:
- safety arguments
- safety claims
- compliance justification

is considered **safety-relevant**.

Errors or ambiguities in such documentation are treated as defects.

---

## 🚫 Forbidden Practices

The following are explicitly forbidden:

- undocumented assumptions
- outdated references
- unreviewed documentation changes
- external documents not under version control
- screenshots as primary documentation

---

## 📌 Ownership and Responsibility

Documentation ownership is defined by repository scope.

Contributors are responsible for:
- keeping documentation accurate
- updating documentation when behavior changes

---

## 🛡️ Audit Readiness

An auditor must be able to:

1. identify the intent of a document
2. track its evolution through Git history
3. link it to implementation and evidence
4. understand its current validity

If this is not possible, the documentation is considered inadequate.
