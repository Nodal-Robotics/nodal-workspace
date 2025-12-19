---
title: Tooling
nav_order: 8
---

# Tooling

This section defines the **engineering tooling framework** used across the Axion Robotics / NODAL ecosystem.

Tooling is considered a **system-level concern**:
it directly impacts quality, safety, traceability, and long-term maintainability.

---

## 🎯 Objectives

Tooling exists to:

- enforce engineering discipline
- reduce ambiguity and human error
- guarantee reproducibility
- support safety and compliance objectives
- scale across multiple repositories and teams

---

## 🧠 Guiding Principles

- Tooling must be **deterministic**
- Tooling must be **documented**
- Tooling must be **version-controlled**
- Tooling must be **reviewable**
- Tooling must be **auditable**

No undocumented tooling is allowed in safety-relevant paths.

---

## 🧩 Scope

Tooling covers:

- build systems
- CI/CD pipelines
- version control workflows
- documentation generation
- simulation and test infrastructure

It does **not** define:
- module implementation details
- application logic

---

## 📂 Contents

- Build tooling
- CI policy and implementation
- Git workflow
- Documentation rules
- Simulation tooling

Each subsection defines **mandatory rules**, not suggestions.
