# NODAL – Documentation Policy

## Purpose

This document defines **how documentation is structured, written, maintained, and governed** across the NODAL ecosystem.

Its goal is to ensure that all documentation is:

✅ consistent
✅ readable
✅ maintainable
✅ scalable
✅ aligned with system architecture

This policy is **normative**.

---

## Scope

This policy applies to:

✅ `nodal-workspace`
✅ all NODAL software modules
✅ tooling repositories
✅ future hardware repositories (when applicable)

---

## Core Principles

### 1. Single Source of Truth

Each piece of information must have **one authoritative location**.

✅ No duplication
✅ No partial copies
✅ No diverging versions

References are preferred over repetition.

---

### 2. Separation of Concerns

Documentation is split into two distinct domains:

| Domain               | Location         | Purpose                                 |
| -------------------- | ---------------- | --------------------------------------- |
| System documentation | `docs/`          | Describe *what the system is✅           |
| Meta-documentation   | `documentation/` | Describe *how documentation is written✅ |

This separation is mandatory.

---

### 3. Audience Awareness

Each document must clearly target **one primary audience**:

✅ system architects
✅ module developers
✅ integrators
✅ contributors

If a document tries to serve everyone, it serves no one.

---

## Directory Responsibilities

### `docs/`

Contains **system-level documentation**.

Examples:

✅ architecture overview
✅ engineering standards
✅ timing and real-time constraints
✅ hardware assumptions
✅ safety assumptions

Rules:

✅ describes *what exists✅ and *what is expected*
✅ does **not** describe how to write documentation
✅ does **not** include templates

---

### `documentation/`

Contains **meta-documentation** and templates.

Examples:

✅ documentation policies
✅ style guides
✅ README / DEV templates
✅ API documentation rules
✅ diagram conventions
✅ badge rules

Rules:

✅ normative for all repositories
✅ referenced, never copied
✅ evolves independently from system behavior

---

## Documentation per Repository Type

### Module Repositories

Required files:

✅ `README.md`
✅ `DEV.md`

Optional:

✅ `docs/` (module-internal documentation)

Rules:

✅ README explains *what the module does*
✅ DEV explains *how to work on the module*
✅ module docs must not redefine global rules

---

### Workspace Repository

Responsibilities:

✅ host system-level documentation
✅ host integration and E2E tests
✅ define global standards

The workspace is the **authoritative reference**.

---

## Naming & Structure Rules

✅ File names are uppercase with underscores
✅ One document = one responsibility
✅ No nested documents without justification

Examples:

✅ `ARCHITECTURE_OVERVIEW.md`
✅ `ENGINEERING_STANDARD.md`

---

## Writing Rules

✅ Use clear, technical English
✅ Avoid marketing language
✅ Prefer lists and tables over prose
✅ State assumptions explicitly
✅ Document constraints, not wishes

---

## Evolution Rules

✅ Documentation evolves with the system
✅ Breaking documentation changes must be explicit
✅ Major restructurings require architectural agreement

---

## Enforcement

✅ Documentation is reviewed during PRs
✅ Non-compliant documentation may block merges
✅ Global documentation overrides local documentation

---

## Final Rule

> Documentation is part of the system interface.

Poor documentation is a system defect.

---

**This document is authoritative for all NODAL repositories.**
