---
title: Safety Requirement Change Management
nav_order: 3
parent: Safety Requirements
---

# Safety Requirement Change Management

## Purpose

This document defines how **changes to Safety Requirements (SR)** are managed, reviewed, approved, and traced within the  NODAL safety framework.

Safety Requirements are **controlled safety artifacts**. Any change to a SR may have system-wide safety implications and must therefore follow a **formal change management process**.

---

## Core Principles

1. **No uncontrolled changes**
   A Safety Requirement shall never be modified without explicit review and approval.

2. **Change equals potential risk**
   Any SR change is assumed to potentially impact safety until proven otherwise.

3. **Traceability must be preserved**
   Hazard, risk classification, verification, and acceptance links must remain valid after change.

4. **Impact first, implementation later**
   Safety impact analysis precedes any implementation work.

5. **Versioned requirements**
   Safety Requirements evolve through versions, not silent edits.

---

## Types of Changes

Safety Requirement changes are classified into the following categories:

| Change Type | Description                                  |
| ----------- | -------------------------------------------- |
| Editorial   | Clarification without semantic change        |
| Technical   | Change in behavior, threshold, or constraint |
| Allocation  | Change of ownership or allocation level      |
| Derivation  | Change in parent/child relationship          |
| Removal     | Deletion or invalidation of a requirement    |

Only **Editorial changes** may be approved with reduced process.

---

## Change Triggers

A SR change may be triggered by:

* hazard reclassification
* architecture modification
* failed verification or test
* operational feedback or incident
* interface change
* regulatory or standard update

---

## Change Management Workflow

### Step 1 — Change Proposal

A change request shall be created as a **dedicated GitHub Issue** linked to the affected SR.

The proposal must include:

* reason for change
* affected SR ID(s)
* preliminary safety impact assessment

---

### Step 2 — Safety Impact Analysis

The following impacts shall be assessed:

* affected hazards
* risk classification changes
* affected derived requirements
* verification artifacts to be updated

If impact cannot be assessed, the change is blocked.

---

### Step 3 — Review and Approval

Approval authority depends on **impact level**:

| Impact              | Approval Required       |
| ------------------- | ----------------------- |
| No safety impact    | Module Lead             |
| Local safety impact | System Architect        |
| System-wide impact  | Safety Lead + Architect |

---

### Step 4 — Implementation

Only after approval may the SR be updated and implementation work started.

Implementation must:

* update requirement version
* update traceability links
* update verification plans if needed

---

### Step 5 — Re-verification

Modified requirements **must be re-verified**.

Previous verification evidence may only be reused if explicitly justified.

---

## Versioning Rules

Each Safety Requirement must include:

* version identifier
* change history

**Versioning guidelines:**

* Minor version: editorial or clarification changes
* Major version: technical or behavioral changes

---

## GitHub Integration

### Required Fields

* `SR Version`
* `Change Type`
* `Change Status`
* `Approved By`
* `Impact Level`

---

### Change Status Values

| Status         | Meaning                  |
| -------------- | ------------------------ |
| Proposed       | Change requested         |
| Under Analysis | Impact being assessed    |
| Approved       | Change approved          |
| Implemented    | Change applied           |
| Verified       | Re-verification complete |
| Rejected       | Change rejected          |

---

## Prohibited Practices

The following are strictly forbidden:

* editing SR text without change record
* implementing before approval
* deleting SRs without impact analysis
* bypassing re-verification

---

## Relationship to Other Documents

* Safety requirement format → `requirement-format.md`
* Allocation rules → `allocation-rules.md`
* Risk acceptance → `risk-acceptance.md`
* Traceability → `traceability/`

---

## Summary

Safety Requirement Change Management ensures that:

* safety intent is preserved over time
* changes are justified and controlled
* verification remains valid
* audits remain possible

An uncontrolled requirement change is treated as a safety non-conformity.
