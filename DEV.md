# NODAL Workspace – Developer Guide

> **Status**: Normative (MUST be followed)
>
> **Scope**: nodal-workspace only
>
> **Audience**: Core maintainers, system integrators, senior contributors
>
> **Philosophy**: NODAL is treated as a **distributed embedded system**, not a classical software project.

---

## 0. Why This Document Exists

This document provides explicit and implicit rules for developing safety-critical systems under NODAL, in compliance with IEC 61508 standards. It ensures that both system-level processes and coding practices (following MISRA C) are followed

It captures:

✅ architectural intent
✅ non-negotiable constraints
✅ good and bad patterns
✅ system-level responsibilities
✅ safety-related system responsibilities

If a rule is not written elsewhere, **it lives here**.

---

## 1. Role of `nodal-workspace`

The `nodal-workspace` repository defines the safety-critical system integration boundary, ensuring functional safety according to IEC 61508 requirements.

Think of it as:

✅ The vehicle harness
✅ The ECU network
✅ The system bench

### 1.1 What the Workspace IS

✅  System orchestrator
✅  Integration and safety testing environment
✅  Dependency authority
✅  Global documentation host
✅  Functional safety authority

### 1.2 What the Workspace IS NOT

❌ A feature factory
❌ A module implementation repo
❌ A dumping ground
❌ A shortcut to bypass APIs

> **Rule**: If logic can live in a module, it MUST NOT live here.

---

## 2. Source of Truth Rules

| Concern        | Source of Truth |
| -------------- | --------------- |
| Architecture   | Workspace docs  |
| Interfaces     | Module APIs     |
| Integration    | Workspace       |
| Business logic | Modules         |

❌ **Bad pattern**

```text
Fixing a module bug directly inside the workspace
```

✅  **Good pattern**

```text
Fix module → release → update workspace dependency
```

---

## 3. Dependency & Integration Model

### 3.1 Module Ownership

Each module:

✅ lives in its own repository
✅ is versioned independently
✅ exposes explicit APIs

The workspace:

✅ pins versions
✅ validates compatibility
✅ never forks modules

❌ **Bad**: copying module code
✅  **Good**: referencing released versions

---

### 3.2 Dependency Changes

Any dependency change MUST:

1. be explicit
2. be documented
3. include integration test updates

PRs without impact analysis are rejected.

---

## 4. Development Workflow (Mandatory)

### 4.1 Adding a Module

Checklist:

✅ [ ] Module repository exists
✅ [ ] API is documented
✅ [ ] Version is tagged
✅ [ ] Workspace dependency updated
✅ [ ] Integration tests added

---

### 4.2 Making Changes

Required steps:

1. Identify affected modules
2. Assess system impact
3. Update documentation
4. Update tests
5. Submit PR with **system rationale**

❌ **Bad PR description**

> "Minor fix"

✅  **Good PR description**

> "Fix timing mismatch between scheduler and transport module (see TIMING_BUDGET.md)"

---

## 5. Testing Strategy (System-Oriented)

### 5.1 Unit Tests

✅ Live ONLY in module repos
✅ Never duplicated

### 5.2 Integration Tests

Workspace tests MUST cover:

✅ module interaction paths
✅ failure propagation
✅ timeout behavior
✅ degraded modes

❌ **Bad**: happy-path only
✅  **Good**: fault injection scenarios

---

## 6. Documentation Obligations

### 6.1 When Docs Are Mandatory

Docs MUST be updated when:

✅ interfaces change
✅ timing changes
✅ dependencies change
✅ behavior changes

"Code-only" PRs are unacceptable.

---

### 6.2 Documentation Hierarchy

Workspace docs:

✅ override module docs
✅ define system truth

Modules:

✅ must reference workspace rules
✅ must not redefine them

---

### 6.3 Normative References

The following documents are **normative** and must be followed:

✅ `GIT.md` – Git rules & workflow
✅ `DOCUMENTATION_POLICY.md` – Documentation structure and rules
✅ `STYLE_GUIDE.md` – Writing and formatting standards

Any conflict is resolved in favor of **workspace-level documents**.

---

### 6.2 Documentation Hierarchy

Workspace docs:

✅ override module docs
✅ define system truth

Modules:

✅ must reference workspace rules
✅ must not redefine them

---

## 7. Forbidden Patterns (Hard Rules)

The following WILL be rejected:

✅ accessing module internals
✅ monkey-patching dependencies
✅ implicit cross-module coupling
✅ undocumented side effects

---

## 8. Review Criteria

Every PR is reviewed for:

✅ architectural alignment
✅ dependency hygiene
✅ test coverage
✅ documentation impact

If reviewers cannot explain the change, it fails.

---

## 9. Mental Model (Read This Twice)

> The workspace is not a codebase.
> It is a **system contract**.

If a change breaks the mental model, it breaks NODAL.

---

## Final Rule

> **Clarity beats cleverness.**
> If it is not explicit, it is wrong.
