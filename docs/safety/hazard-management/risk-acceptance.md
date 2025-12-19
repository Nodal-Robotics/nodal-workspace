---
title: System Architecture Overview
nav_order: 1
parent: Governance
---

# Risk Acceptance

## Purpose

This document defines how **risk acceptance decisions** are made, justified, documented, and approved within the  NODAL safety framework.

Risk acceptance is a **controlled engineering decision**, not an informal acknowledgement. Any accepted risk must be:

* explicitly justified
* approved at the appropriate authority level
* traceable to evidence
* reviewable over time

This document applies at the **system (workspace) level** and governs all modules integrated into the system.

---

## Core Principles

1. **No implicit acceptance**
   A risk is never considered accepted by default, inactivity, or silence.

2. **Acceptance is proportional to risk**
   Higher risk levels require higher authority and stronger justification.

3. **Acceptance is reversible**
   A previously accepted risk may be re-opened if assumptions change.

4. **Acceptance is evidence-based**
   Decisions must reference analysis, mitigation status, and verification evidence.

5. **Acceptance does not remove responsibility**
   Accepting a risk does not mean ignoring it; monitoring obligations remain.

---

## Risk Acceptance Levels

Risk acceptance authority is determined by the **Risk Class (RC)** defined in `risk-classification.md`.

| Risk Class | Description | Acceptance Authority    |
| ---------- | ----------- | ----------------------- |
| RC0        | Negligible  | Automatic (documented)  |
| RC1        | Low         | Module Lead             |
| RC2        | Medium      | System Architect        |
| RC3        | High        | Safety Lead + Architect |
| RC4        | Critical    | **Not acceptable**      |

> RC4 risks **cannot be accepted**. The system design must be changed.

---

## Acceptance Preconditions

A risk may only be considered for acceptance if **all** of the following conditions are met:

* Hazard is correctly identified and classified
* All **reasonably practicable** mitigations have been implemented
* Residual risk has been re-classified
* Verification evidence exists or is planned
* Assumptions are explicitly documented

If any condition is not met, the risk **must remain open**.

---

## Acceptance Justification

Each accepted risk must include a **written justification**, covering:

* Hazard summary
* Initial risk classification
* Implemented mitigations
* Residual risk classification
* Rationale for acceptance
* Operational or procedural constraints
* Monitoring or review conditions

Acceptance without justification is invalid.

---

## GitHub Integration

### Representation

Risk acceptance is represented using **GitHub Issues** (Hazard issues) and **GitHub Projects fields**.

Required fields:

* `Risk Class` (single select)
* `Risk Status` (single select)
* `Accepted By` (text or user)
* `Acceptance Rationale` (text)
* `Acceptance Date` (date)

---

### Risk Status Values

| Status             | Meaning                            |
| ------------------ | ---------------------------------- |
| Open               | Risk identified, not yet mitigated |
| Mitigated          | Mitigations implemented            |
| Pending Acceptance | Awaiting approval                  |
| Accepted           | Residual risk accepted             |
| Rejected           | Acceptance refused                 |
| Reopened           | Risk reopened due to change        |

---

## Change and Re-acceptance

Risk acceptance must be **re-evaluated** if any of the following occur:

* Change in system architecture
* Change in operating conditions
* New hazard discovered
* Failed verification or incident
* Modification of assumptions

Re-evaluation may result in:

* reaffirmation
* escalation
* rejection

---

## Audit Expectations

For audit readiness, each accepted risk must be:

* traceable to its hazard record
* linked to safety requirements
* linked to verification evidence
* time-stamped and attributed

Auditors must be able to answer:

> Who accepted this risk, when, why, and based on what evidence?

---

## Relationship to Other Documents

* Hazard identification → `hazard-identification.md`
* Risk classification → `risk-classification.md`
* Safety requirements → `safety-requirements/`
* Traceability → `traceability/`
* Safety lifecycle → `safety-lifecycle/`

---

## Summary

Risk acceptance in Nodal is:

* explicit
* documented
* authority-based
* evidence-driven
* reversible

No undocumented risk acceptance is permitted.