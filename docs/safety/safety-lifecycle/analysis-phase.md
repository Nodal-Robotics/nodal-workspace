---
title: System Architecture Overview
nav_order: 1
parent: Governance
---

# Analysis Phase — Safety Activities

## Status

Normative — Workspace level

## Purpose

This document defines the **safety-specific activities during the Analysis phase** of the system lifecycle.

Analysis is where safety begins.  Hazards are identified, classified, and translated into safety requirements before any implementation occurs.

---

## Scope

This document applies to: 

* system-level safety analysis
* cross-module interaction analysis
* interface safety analysis

It does **not** define:

* module-internal analysis
* product-specific certification activities

---

## Core Principle

> **No implementation shall proceed without complete safety analysis.**

If a feature cannot be analyzed for safety, it cannot be developed. 

---

## Safety Analysis Objectives

During Analysis, the following objectives must be met:

1. **Identify all credible hazards** related to the change or feature
2. **Classify each hazard** by risk level
3. **Derive safety requirements** to mitigate high-risk hazards
4. **Document assumptions** on which safety claims depend
5. **Prepare for development** by clearly stating safety intent

---

## Activities

### 1. Problem and Context Definition

Define the change being analyzed:

* what is new or modified
* operational context
* affected modules and interfaces
* boundary conditions

Record in a GitHub issue (type: `analysis`).

---

### 2. Hazard Identification

Systematically identify hazards using: 

* **Failure mode analysis**:  what can go wrong in each component or interface? 
* **Scenario analysis**: what harmful sequences are credible?
* **Standards and experience**: lessons from similar systems
* **Expert review**: domain expertise and safety knowledge

See: [`../hazard-management/hazard-identification. md`](../hazard-management/hazard-identification.md)

---

### 3. Hazard Characterization

For each identified hazard, document:

* **What can fail** (e.g., communication loss, sensor drift)
* **Why it can fail** (failure modes, root causes)
* **How harm results** (cascade of failures leading to harm)
* **Who or what is affected** (people, equipment, environment)
* **Under what conditions** (operational scenarios, environmental constraints)

---

### 4. Risk Classification

Classify each hazard using the risk model:

* **Severity (S)**: worst-case consequence
* **Probability (P)**: likelihood of occurrence
* **Exposure (E)**: frequency or duration of exposure

Determine **Risk Class (RC)** using the risk matrix. 

See: [`../hazard-management/risk-classification. md`](../hazard-management/risk-classification.md)

---

### 5. Mitigation Strategy Development

For each classified hazard, decide on a mitigation path:

**Option A: Implement Safety Requirement**

If risk is **RC2 or higher**, derive a safety requirement that: 

* mitigates the hazard
* is verifiable
* can be allocated to a module or system

See: [`../safety-requirements/requirement-format.md`](../safety-requirements/requirement-format.md)

**Option B: Accept Residual Risk**

If risk is **RC0 or RC1**, or if mitigation is infeasible:

* document justification
* prepare for formal acceptance in Deployment phase

See: [`../hazard-management/risk-acceptance.md`](../hazard-management/risk-acceptance. md)

**Option C: Change Scope or Architecture**

If mitigation is impossible or disproportionate:

* propose architectural change
* document via ADR
* restart analysis with new scope

---

### 6. Safety Requirement Definition

For each mitigation requiring a safety requirement:

* assign a unique identifier (SR-SYS-*, SR-MOD-*, etc.)
* write a clear, testable statement
* define verification method
* establish traceability to hazard and risk class

---

### 7. Assumption Documentation

Document all assumptions on which safety claims depend:

* environmental assumptions
* operational constraints
* hardware behavior assumptions
* module integration assumptions

See: [`../safety-scope-and-assumptions. md`](../safety-scope-and-assumptions.md)

---

### 8. Interface and Interaction Analysis

For features involving cross-module interfaces:

* identify interface safety requirements
* define timing and data integrity constraints
* document error handling expectations

---

## Artifacts Produced

| Artifact           | Description                      |
| ------------------ | -------------------------------- |
| Hazard issues      | GitHub issues (type: `hazard`)   |
| Risk classifications | SR, P, E, RC documented        |
| Safety requirements | GitHub issues (type: `safety-requirement`) |
| Assumptions record | Documented assumptions          |
| ADRs (if needed)   | Architectural decisions          |

---

## GitHub Integration

Analysis work is tracked using:

* **Analysis issues** (type: `analysis`)
* **Hazard issues** (type: `hazard`) — one per identified hazard
* **Safety requirement issues** (type: `safety-requirement`) — one per derived SR
* **Project fields**:
  * `Lifecycle = Analysis`
  * `Risk Class = RC0/RC1/RC2/RC3/RC4`

---

## Review and Approval

### Technical Review

All hazards and SRs must be reviewed by:

* a domain expert (module owner or architect)
* for completeness and correctness

### Safety Authority Review

High-risk hazards (RC3 or RC4) must be approved by:

* the Safety Authority
* before proceeding to Development

---

## Exit Criteria

The Analysis phase is complete when:

* ✅ all credible hazards are identified
* ✅ all hazards are classified
* ✅ all RC2+ hazards have safety requirements
* ✅ RC0/RC1 hazards are ready for acceptance decision
* ✅ assumptions are documented
* ✅ required ADRs are approved
* ✅ development team understands safety intent

---

## Anti-Patterns

The following practices are **prohibited**:

* analyzing only "obvious" hazards
* skipping analysis to start development early
* deferring hazard identification to later phases
* assuming module-level analysis is sufficient
* undocumented risk acceptance decisions

---

## Relation to System Analysis Phase

The safety analysis phase is **concurrent** with system analysis defined in [`../../lifecycle/analysis. md`](../../lifecycle/analysis.md).

Safety analysis provides:

* constraints on system design
* requirements for implementation
* evidence for design decisions

---

## Next Phase Gate

Before transitioning to Development, confirm:

* all hazards are classified
* all SRs are defined and approved
* assumptions are explicit
* development team is briefed on safety requirements

---

## Related Documents

* Hazard identification:  [`../hazard-management/hazard-identification.md`](../hazard-management/hazard-identification. md)
* Risk classification: [`../hazard-management/risk-classification.md`](../hazard-management/risk-classification.md)
* Safety requirement format: [`../safety-requirements/requirement-format.md`](../safety-requirements/requirement-format.md)
* Safety scope:  [`../safety-scope-and-assumptions.md`](../safety-scope-and-assumptions.md)
* Lifecycle overview: [`./index.md`](./index.md)

---

## Summary

The Analysis phase establishes the **safety foundation** for all subsequent work. 

Rigorous analysis at this stage: 

* prevents costly re-work later
* ensures complete hazard coverage
* enables informed design decisions
* supports compliance and certification