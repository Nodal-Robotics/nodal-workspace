---
title: Deployment Phase — Safety Activities
nav_order: 5
parent: Safety Lifecycle
---

# Deployment Phase — Safety Activities

## Status

Normative — Workspace level

## Purpose

This document defines the **safety-specific activities during the Deployment phase** of the system lifecycle.

Deployment is where:

* the system is **released** for operational use
* **residual risks are formally accepted** by authority
* **operational constraints** are documented
* **safety responsibility** transitions to operators

---

## Scope

This document applies to:

* release authorization
* residual risk acceptance
* operational documentation
* deployment constraints

It does **not** prescribe:

* operational procedures (those are integrator responsibility)
* field support or maintenance
* post-deployment monitoring (beyond safety-critical alerts)

---

## Core Principle

> **Only a verified and explicitly accepted system may be deployed.**

Unresolved safety issues **block release**. No schedule pressure overrides safety. 

---

## Safety Deployment Objectives

During Deployment, the following objectives must be met:

1. **Confirm verification completeness** — all SRs verified
2. **Identify and document residual risks** — what remains after mitigation
3. **Formalize risk acceptance** — authorized decision on residual risks
4. **Define operational constraints** — how system must be used safely
5. **Authorize release** — gate-checked decision to deploy

---

## Pre-Deployment Gate

Before deployment activities start, confirm:

* ✅ Verification phase is complete
* ✅ all verification evidence is collected and linked
* ✅ no critical or major findings remain open
* ✅ Safety Authority has approved verification readiness

---

## Activities

### 1. Verification Completeness Review

Confirm that: 

* **all SRs are verified** or residual risk is explicitly identified
* **all evidence is complete** and traceable to SRs
* **all hazards are closed** (either mitigated and verified, or accepted)
* **no orphan artifacts** exist (unlinked hazards, SRs, evidence)

---

### 2. Residual Risk Identification

Identify risks that **remain after mitigation and verification**:

* **implementation limits**:  known constraints or edge cases
* **unverifiable assumptions**: things we assume but cannot prove
* **operational constraints**: conditions required for safe operation
* **monitoring needs**: issues requiring continued observation

Document each residual risk clearly. 

---

### 3. Risk Acceptance Review

For each residual risk:

* **assess acceptability**:  does residual risk fall within tolerance?
* **document justification**: why is it acceptable?
* **define conditions**: what constraints must be observed?
* **plan monitoring**: how will risk be tracked post-deployment? 

Risks that exceed tolerance: 

* **cannot be deployed** (must be mitigated further or scope reduced)
* require escalation and decision

---

### 4. Operational Constraints Documentation

Document any constraints required for safe operation:

* **environment limits**: temperature, humidity, radiation, etc.
* **usage patterns**: duty cycles, load limits, frequency of operation
* **maintenance requirements**: calibration, inspection intervals
* **configuration constraints**: parameters that must not be changed
* **fault handling procedures**: what to do if certain faults occur

These constraints are part of the **safety case** and must be communicated to operators.

---

### 5. Safety Authority Review and Approval

The Safety Authority reviews:

* verification evidence completeness
* residual risk assessment
* operational constraints
* overall readiness for deployment

The Safety Authority may:

* ✅ approve deployment
* ⚠️ approve with conditions (e.g., additional monitoring)
* ❌ reject deployment (requires further mitigation)

This decision is **final and binding**.

---

### 6. Release Documentation

Prepare release materials including:

* **Release notes**: scope, changes, known limitations
* **Safety statement**: safety objectives met, residual risks accepted
* **Operational constraints**: requirements for safe use
* **Verification summary**: evidence that mitigations work
* **Assumptions and limitations**: what might change this
* **Contact for safety issues**: escalation path if problems arise

---

### 7. Release Authorization

Formally authorize release: 

* Safety Authority signs off
* System maintainer approves
* Release is tagged in repository
* Release notes are published

Only **approved and signed releases** may be deployed operationally.

---

### 8. Deployment Record

Document: 

* release version and date
* systems/installations where deployed
* deployment configuration
* any deviations from standard deployment

---

### 9. Post-Deployment Monitoring Plan

Define (if applicable):

* **safety metrics** to track (e.g., incident rates, anomaly frequency)
* **reporting requirements** (e.g., if a residual risk manifests)
* **escalation procedures** (who to contact if safety concern arises)
* **review schedule** (when to re-evaluate assumptions or risks)

---

### 10. Feedback Loop Closure

After deployment:

* operational feedback is captured
* if issues arise, new Analysis is triggered
* if assumptions prove invalid, safety case is updated
* lessons learned are documented

---

## Residual Risk Record

Each accepted residual risk is documented with:

| Field              | Content                            |
| ------------------ | ---------------------------------- |
| Risk ID            | Unique identifier                  |
| Description        | What risk remains                  |
| Initial hazard     | Link to originating hazard         |
| Mitigations tried  | What was attempted                 |
| Residual risk      | Post-mitigation classification    |
| Acceptance rationale | Why it is acceptable              |
| Conditions/limits  | Constraints on use                 |
| Monitoring         | How risk will be tracked           |
| Acceptance date    | When approved                      |
| Approved by        | Authority role                     |

---

## GitHub Integration

Deployment work is tracked using: 

* **Deployment issues** (type: `deployment`, `release`)
* **Release tag** in repository
* **Risk acceptance issues** linked to hazards
* **Project fields**:
  * `Lifecycle = Deployment`
  * `Release Version = <version>`
  * `Approval Status = Pending / Approved / Deployed`

---

## Approval Gates

The following must be satisfied before release:

| Gate                           | Authority          |
| ------------------------------ | ------------------ |
| Verification complete          | QA Lead            |
| Safety evidence reviewed       | Safety Authority   |
| Residual risks accepted        | Safety Authority   |
| Operational constraints clear  | System maintainer  |
| Release documentation complete | Maintainer         |

**All gates must be approved before deployment.**

---

## Release Conditions

Deployment may be conditional: 

* ✅ Unconditional approval:  full deployment authorized
* ⚠️ Conditional approval: deployment allowed only under specific conditions
  * e.g., "only in lab environments until further evidence is collected"
  * e.g., "operator training on residual risks required"
* ❌ Approval rejected: further mitigation required

---

## Handling Deployment Rejection

If safety concerns block release:

* clearly identify the blocking issue
* determine whether fix is in code or requirements
* plan corrective action
* go back through the lifecycle (likely Verification or Development)
* re-plan deployment

---

## Exit Criteria

The Deployment phase is complete when:

* ✅ Safety Authority approves release
* ✅ residual risks are formally accepted
* ✅ release documentation is published
* ✅ system is deployed (or release is available for use)

---

## Anti-Patterns

The following practices are **prohibited**:

* deploying without Safety Authority approval
* hiding or understating residual risks
* deploying unverified changes
* skipping documentation due to schedule pressure
* informal risk acceptance (without documented evidence)

---

## Relation to System Deployment Phase

The safety deployment phase is embedded in the system deployment phase defined in [`../../lifecycle/deployment.md`](../../lifecycle/deployment.md).

Safety activities: 

* validate readiness
* formalize risk decisions
* gate the release

---

## Feedback to Analysis

Deployment may reveal:

* operational constraints not anticipated
* assumptions proven wrong
* need for additional monitoring
* improvement opportunities

This feedback triggers new Analysis and begins a new cycle of the lifecycle.

---

## Related Documents

* Risk acceptance: [`../hazard-management/risk-acceptance.md`](../hazard-management/risk-acceptance.md)
* Safety policy: [`../safety-policy. md`](../safety-policy.md)
* Release policy: [`../../governance/release-policy.md`](../../governance/release-policy.md)
* Lifecycle overview: [`./index.md`](./index.md)

---

## Summary

The Deployment phase **formalizes safety acceptance** and **authorizes release**. 

Disciplined deployment: 

* ensures nothing is released without authority approval
* makes residual risks explicit and accepted
* provides operators with clear constraints
* closes the safety lifecycle loop