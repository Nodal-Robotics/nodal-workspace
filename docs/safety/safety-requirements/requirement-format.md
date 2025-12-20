---
title: Safety Requirement Format
nav_order: 1
parent: Safety Requirements
---

# Safety Requirement Format

## Purpose

This document defines the **mandatory format and structure** of Safety Requirements (SR) within the  NODAL framework.

Safety Requirements translate identified hazards and accepted residual risks into **verifiable, enforceable engineering constraints**.

This format applies to:

* system-level (workspace) safety requirements
* module-level safety requirements derived from system SRs

---

## Core Principles

1. **One requirement = one intent**
   A safety requirement shall address a single safety objective.

2. **Requirements are normative**
   Safety requirements use *shall*, not *should* or *may*.

3. **Requirements are testable**
   Each requirement must be verifiable by analysis, test, inspection, or simulation.

4. **Requirements are traceable**
   Each requirement must link back to:

   * at least one hazard
   * at least one risk classification

5. **Requirements are stable objects**
   Requirements have identity, versioning, and change control.

---

## Safety Requirement Types

Safety requirements are classified by **scope and intent**:

| Type    | Description                                  |
| ------- | -------------------------------------------- |
| SR-SYS  | System-level safety requirement              |
| SR-MOD  | Module-level safety requirement              |
| SR-INT  | Interface safety requirement                 |
| SR-PROC | Procedural or operational safety requirement |

---

## Mandatory Requirement Structure

Each Safety Requirement **must** contain the following fields.

### 1. Identifier

Unique and immutable identifier.

**Format:**

```
SR-<LEVEL>-<DOMAIN>-<NUMBER>
```

**Examples:**

* SR-SYS-CTRL-001
* SR-MOD-IO-014

---

### 2. Requirement Statement

A single, clear, normative statement.

**Template:**

> The system/module **shall** <behavior or constraint>.

**Example:**

> The motion control module shall transition to a safe torque-off state within 50 ms upon loss of communication.

---

### 3. Rationale

Explains *why* the requirement exists.

Must reference:

* the originating hazard(s)
* the associated risk class

---

### 4. Safety Integrity Context

Defines the criticality context.

Required fields:

* Originating Hazard ID(s)
* Initial Risk Class
* Residual Risk Class

---

### 5. Allocation

Defines where the requirement is implemented.

Possible values:

* Workspace / system
* Specific module(s)
* Hardware
* Software
* Process / operation

---

### 6. Verification Method

Defines how compliance is demonstrated.

Allowed methods:

* Test
* Analysis
* Inspection
* Simulation

At least one method is mandatory.

---

### 7. Acceptance Criteria

Objective, measurable condition for success.

**Example:**

> Communication loss is detected within ≤ 20 ms and torque output reaches zero within ≤ 50 ms.

---

### 8. Traceability Links

Each SR must link to:

* Hazard issue(s)
* Implementing feature / issue
* Verification artifact(s)

---

## GitHub Representation

Safety Requirements are represented as:

* GitHub Issues (type: `safety-requirement`)
* or Markdown records linked from issues

### Required GitHub Fields

* `Type = Safety Requirement`
* `Requirement ID`
* `Origin Hazard`
* `Risk Class`
* `Verification Method`
* `Status`

---

## Lifecycle Status

| Status      | Meaning               |
| ----------- | --------------------- |
| Draft       | Requirement defined   |
| Allocated   | Assigned to module(s) |
| Implemented | Design/code complete  |
| Verified    | Verification passed   |
| Rejected    | Invalidated           |

---

## Common Errors to Avoid

* Multiple safety objectives in one requirement
* Non-verifiable wording
* Missing hazard linkage
* Implicit assumptions
* Implementation details embedded in requirement text

---

## Relationship to Other Documents

* Hazard identification → [`hazard-identification.md`](../hazard-management/hazard-identification.md)
* Risk classification →[ `risk-classification.md`](../hazard-management/risk-classification.md)
* Risk acceptance →[ `risk-acceptance.md`](../hazard-management/risk-acceptance.md)
* Allocation rules →[ `allocation-rules.md`](./allocation-rules.md)
* Change management →[ `change-management.md`](./change-management.md)

---

## Summary

A Safety Requirement is:

* precise
* justified
* traceable
* verifiable
* controlled

If a requirement cannot be verified or traced, it is not a valid safety requirement.
