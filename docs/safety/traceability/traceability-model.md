# Traceability Model

## Purpose

This document defines the **traceability model** used in the Axion Robotics / NODAL safety framework.

Traceability ensures that every safety-relevant decision, requirement, and implementation element is:

* justified
* linked
* auditable
* verifiable

The objective is to maintain an unbroken chain from **hazard identification** to **verification evidence**.

---

## Core Principles

1. **End-to-end traceability**
   Every hazard must be traceable to implemented and verified mitigations.

2. **Bidirectional links**
   Traceability must work forward and backward (top-down and bottom-up).

3. **Single source of truth**
   GitHub Issues and Pull Requests are the authoritative traceability backbone.

4. **Explicit links only**
   Implicit or assumed relationships are not acceptable.

5. **Living traceability**
   Traceability is continuously maintained, not generated at the end.

---

## Traceability Chain Overview

The mandatory traceability chain is:

```
Hazard
  ↓
Risk Classification
  ↓
Safety Requirement (SR)
  ↓
Feature / Implementation
  ↓
Verification Activity
  ↓
Evidence
```

A break at any level is considered a **safety non-conformity**.

---

## Traceability Elements

### 1. Hazard

* Represented as a GitHub Issue (type: `hazard`)
* Identified in `hazard-identification.md`
* Classified per `risk-classification.md`

Required links:

* linked Safety Requirement(s)

---

### 2. Safety Requirement

* Represented as a GitHub Issue (type: `safety-requirement`)
* Defined using `requirement-format.md`

Required links:

* originating Hazard(s)
* implementing Feature(s)

---

### 3. Feature / Implementation

* Represented as GitHub Issue or Pull Request
* Implements one or more SRs

Required links:

* implemented Safety Requirement(s)
* verification activity

---

### 4. Verification Activity

* Test, analysis, inspection, or simulation
* May be represented as:

  * test cases
  * verification issues
  * CI jobs

Required links:

* verified Safety Requirement(s)
* produced evidence

---

### 5. Evidence

Evidence demonstrates that verification objectives are met.

Examples:

* test reports
* CI logs
* coverage results
* simulation outputs

Evidence must be:

* immutable
* identifiable
* reproducible

---

## Traceability Rules

The following rules are mandatory:

* Each Hazard must link to ≥ 1 SR
* Each SR must link to ≥ 1 Feature
* Each Feature must link to ≥ 1 Verification Activity
* Each Verification Activity must produce ≥ 1 Evidence artifact

No orphan elements are permitted.

---

## GitHub Implementation Model

### Link Mechanisms

Traceability links are implemented using:

* issue references (`#123`)
* issue relationships ("blocks", "is blocked by")
* pull request references
* project fields (single select, text, number)

---

### Recommended GitHub Fields

| Field               | Purpose                              |
| ------------------- | ------------------------------------ |
| Type                | Hazard / SR / Feature / Verification |
| Risk Class          | From risk classification             |
| Verification Status | Planned / Passed / Failed            |
| Evidence Link       | URL or artifact reference            |

---

## Traceability Across Repositories

Traceability may span multiple repositories:

* Hazards and system SRs typically live in the workspace
* Module SRs and features live in module repositories

Cross-repository links are mandatory and supported by GitHub.

---

## Audit Expectations

An auditor must be able to:

* start from a hazard and reach evidence
* start from evidence and identify the originating hazard
* identify who approved acceptance and when

Any missing link is considered a finding.

---

## Relationship to Other Documents

* Hazard management → `hazard-management/`
* Safety requirements → `safety-requirements/`
* Verification lifecycle → `safety-lifecycle/verification-phase.md`

---

## Summary

The traceability model ensures that:

* safety decisions are justified
* implementation matches intent
* verification is meaningful
* audits are feasible

Traceability is not documentation overhead — it is a safety control mechanism.
