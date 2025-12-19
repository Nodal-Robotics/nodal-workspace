---
title: Continuous Integration
nav_order: 8
parent: Tooling
---

# Continuous Integration (CI)

This document describes how **Continuous Integration (CI)** is implemented and used within the  NODAL ecosystem.

CI is considered a **system-level engineering tool** that enforces quality, safety, and traceability rules.

---

## 🎯 Purpose

The objectives of CI are to:

- verify changes automatically
- prevent regressions
- enforce tooling and safety policies
- provide reproducible verification outputs
- act as a controlled source of safety evidence

CI is not optional and not a convenience feature.

---

## 🧠 Role of CI in the System

CI is an **execution mechanism**, not a decision authority.

CI:
- executes defined checks
- produces objective results
- blocks integration when requirements are not met

CI does **not**:
- make architectural decisions
- override governance rules
- replace human review

---

## 🧩 Scope

CI applies to:

- all repositories in the organization
- all pull requests
- all merges to protected branches
- all tagged releases

Safety-relevant repositories have **additional constraints**.

---

## 🔁 CI Triggers

CI pipelines must be triggered on:

- pull request creation and update
- merge to protected branches
- release tag creation

Manual execution is allowed **only** for debugging.

---

## 🛠️ Mandatory CI Stages

Each CI pipeline must include, at minimum:

1. **Build**
   - deterministic
   - toolchain explicitly defined

2. **Static Analysis**
   - language-appropriate
   - blocking when safety-relevant

3. **Testing**
   - unit tests
   - integration tests when applicable
   - explicit pass/fail criteria

4. **Formatting / Linting**
   - deterministic
   - non-blocking unless safety-relevant

---

## 🛡️ Safety Constraints

For safety-relevant repositories:

- CI must be **blocking**
- failures must be explicit
- logs must be preserved
- artifacts must be retained or referenced
- tool versions must be visible

CI results may be used as **safety evidence** if referenced and reproducible.

---

## 📦 Artifacts and Logs

CI must:

- expose logs for all stages
- preserve safety-relevant artifacts
- ensure traceability to:
  - commit
  - pull request
  - pipeline run

Artifacts without traceability are invalid.

---

## 🔗 Integration with GitHub

CI is integrated with GitHub via:

- pull request status checks
- branch protection rules
- linked CI runs

A pull request cannot be merged unless CI requirements are satisfied.

---

## 🔁 Change Management

Changes to CI configuration are:

- version-controlled
- reviewed via pull request
- subject to impact analysis when safety-relevant

---

## 🛡️ Audit Readiness

CI must allow an auditor to:

1. identify which checks were executed
2. retrieve logs and artifacts
3. link results to a specific commit
4. reproduce the execution

If this is not possible, CI outputs are **not acceptable** as evidence.
