# Analysis Phase

## Status

Normative — Workspace level

## Purpose

The Analysis phase defines **what the system must do**, **why it must do it**, and **under which constraints** — before any implementation decision is taken.

This phase is the foundation of:

* system correctness
* architectural coherence
* safety arguments
* long-term maintainability

Poor analysis cannot be compensated later by development or testing.

---

## Scope

The Analysis phase applies to:

* new system capabilities
* changes to existing behavior
* safety-related modifications
* architectural or interface changes

Out of scope:

* coding activities
* detailed design or optimization

---

## Objectives

The Analysis phase aims to:

* identify stakeholder needs
* define functional intent
* capture assumptions and constraints
* identify hazards and risks
* decide *whether* and *how* to proceed

No code shall be written until analysis objectives are met.

---

## Inputs

Typical inputs include:

* stakeholder requests
* regulatory or safety constraints
* operational context
* existing system limitations
* feedback from verification or deployment

All inputs shall be explicit and traceable.

---

## Core Activities

### 1. Problem Definition

Each analysis starts with a **clear problem statement**:

* what is missing or incorrect
* in which context
* why it matters

This statement shall be recorded in a GitHub Issue.

---

### 2. Functional Intent

The expected system behavior shall be described:

* at system level
* without implementation assumptions

This includes:

* nominal behavior
* degraded behavior
* failure handling expectations

---

### 3. Assumptions and Constraints

All assumptions shall be explicitly documented:

* operating environment
* hardware availability
* timing expectations
* external dependencies

Assumptions are first-class artifacts and shall be revisited.

---

### 4. Hazard Identification (if applicable)

For safety-relevant changes:

* potential hazards shall be identified
* operational scenarios shall be considered
* misuse and failure cases shall be analyzed

This activity feeds directly into the Safety Case.

---

### 5. Decision Preparation

If multiple solutions are possible:

* options shall be identified
* trade-offs shall be documented
* impacts shall be assessed

This prepares the creation of an ADR.

---

## Artifacts

The Analysis phase produces the following artifacts:

| Artifact               | Description              |
| ---------------------- | ------------------------ |
| Analysis Issue         | Primary tracking item    |
| Functional description | What the system shall do |
| Assumptions list       | Explicit constraints     |
| Hazard records         | If safety-relevant       |
| ADR (if needed)        | Decision rationale       |

Artifacts shall be stored in repositories and referenced explicitly.

---

## Relation to GitHub Projects

In GitHub Projects, Analysis work is represented by:

* lifecycle = Analysis
* type = feature / hazard / decision
* module = workspace or target module

Completion of Analysis is required before moving to Development.

---

## Exit Criteria

The Analysis phase is considered complete when:

* problem is clearly stated
* functional intent is documented
* assumptions are explicit
* hazards are identified (if applicable)
* decisions are either taken or planned via ADR

All criteria shall be visible and reviewable.

---

## Anti-Patterns

The following practices are prohibited:

* coding before analysis is complete
* implicit assumptions
* skipping hazard analysis for safety-related work
* undocumented decisions

---

## Relation to Other Phases

* Feeds into: `development.md`
* Informed by: `verification.md`, `deployment.md`

---

## Summary

The Analysis phase transforms **ideas and needs** into **structured, auditable intent**.

It ensures that development effort is:

* justified
* aligned
* safe by design
