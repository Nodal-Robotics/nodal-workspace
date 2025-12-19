---
title: System Architecture Overview
nav_order: 1
parent: Governance
---

# Development Phase — Safety Activities

## Status

Normative — Workspace level

## Purpose

This document defines the **safety-specific activities during the Development phase** of the system lifecycle.

Development is where safety requirements are **implemented** and **made concrete** through code, design, and configuration.

The focus is on: 

* implementing identified mitigations correctly
* preserving safety intent through implementation
* maintaining traceability
* preparing for verification

---

## Scope

This document applies to:

* implementation of safety-relevant features
* safety-critical code and configuration
* architectural changes driven by safety
* interface implementation

It does **not** prescribe:

* coding style or languages
* build system details
* module-internal workflows beyond safety constraints

---

## Core Principle

> **Implementation shall conform to the safety intent defined in Analysis.**

Silent deviations, even minor ones, can break safety arguments.

---

## Safety Development Objectives

During Development, the following objectives must be met:

1. **Implement all assigned safety requirements** correctly
2. **Maintain full traceability** to analysis artifacts
3. **Respect architectural and interface constraints**
4. **Identify implementation hazards** not evident in analysis
5. **Prepare for verification** with testable, reviewable code

---

## Pre-Development Gate

Before development starts, confirm:

* ✅ all applicable safety requirements are approved
* ✅ assumptions from analysis are understood
* ✅ architectural constraints are clear
* ✅ interface safety specifications are defined
* ✅ development team has safety training or guidance

---

## Activities

### 1. Safety Requirement Allocation and Decomposition

For each safety requirement allocated to development:

* determine **who owns** the implementation (module, layer, component)
* if the requirement is high-level, **decompose** it into implementation-level details
* update traceability links to show allocation

---

### 2. Design for Safety

When designing the implementation:

* **Respect module boundaries**:  no circular dependencies or implicit coupling
* **Design for failure detection**: hazards must be detectable
* **Design for containment**: failures must not propagate unexpectedly
* **Plan for testing**: ensure requirements are verifiable

---

### 3. Implementation

Implement the feature:

* follow the design aligned with safety requirements
* reference the requirement ID in code comments when implementing safety-critical behavior
* avoid undocumented complexity

---

### 4. Safety-Critical Code Review

Before merge, safety-critical code must be reviewed by:

* **Peer reviewer**: for correctness and clarity
* **Safety reviewer** (if applicable): for compliance with safety intent

Review checklist: 

* ✅ Requirement ID is referenced
* ✅ Implementation matches requirement intent
* ✅ Error handling is explicit
* ✅ No silent failures possible
* ✅ Timing constraints are respected

---

### 5. Implementation-Level Hazard Analysis

As code takes shape, analyze for **implementation-level hazards** not evident in analysis:

* race conditions
* resource exhaustion
* error path failures
* timing violations

If new hazards are discovered: 

* document them
* classify them
* decide on mitigation or acceptance

---

### 6. Interface Implementation

For safety-relevant interfaces:

* implement exactly as specified in safety requirements
* document error handling behavior
* implement defensive checks (e.g., parameter validation)

---

### 7. Configuration and Integration

Configure the system:

* set safety-related parameters per specification
* document configuration assumptions
* validate that integrated modules interact correctly

---

### 8. Documentation Updates

Update documentation to reflect:

* any deviations from original design (with justification)
* implementation choices that affect safety
* assumptions about the runtime environment
* known limitations or constraints

---

## Traceability Maintenance

Throughout development: 

* each safety requirement has an **implementing PR or issue**
* each PR references its originating SR
* code comments reference requirement IDs
* no safety behavior is implemented without traceability

---

## Artifacts Produced

| Artifact               | Description                           |
| ---------------------- | ------------------------------------- |
| Implementation PR      | Code and design changes               |
| PR description         | References SRs, explains safety logic |
| Code comments          | Document safety-critical sections    |
| Design documentation   | Explain safety-relevant choices       |
| Updated assumptions    | Refine assumptions if needed          |

---

## GitHub Integration

Development work is tracked using:

* **Development issues** or **PRs** linked to safety requirements
* **Labels**:  `type: feature`, `type:mitigation`, `safety-critical`
* **Project fields**:
  * `Lifecycle = Development`
  * `Linked SR = SR-*-*-*`

---

## Safety Reviews

### Peer Review

All safety-relevant PRs must pass peer review focusing on:

* correctness of implementation
* adherence to requirements
* clarity and maintainability

### Safety Authority Review

High-risk mitigations (from RC3/RC4 hazards) require:

* approval from Safety Authority or delegate
* before merge

---

## Change Management

If implementation reveals that:

* a requirement cannot be met
* an assumption is invalid
* a design decision must change

Then:

* **stop development** of that requirement
* **update Analysis** (amend hazard, SR, or assumption)
* **get approval** before resuming
* **update traceability** to record the change

---

## Exit Criteria

The Development phase is complete when:

* ✅ all SRs have implementations
* ✅ code is reviewed and merged
* ✅ traceability is complete
* ✅ no open safety-related change requests remain
* ✅ implementation is ready for verification

---

## Anti-Patterns

The following practices are **prohibited**:

* implementing without reference to SRs
* silent deviations from safety requirements
* deferring error handling to "later"
* breaking interfaces without updating safety specs
* code review without safety consideration

---

## Relation to System Development Phase

The safety development phase is embedded in the system development phase defined in [`../../lifecycle/development.md`](../../lifecycle/development.md).

Safety activities: 

* shape architectural decisions
* constrain design choices
* inform code review

---

## Next Phase Gate

Before transitioning to Verification, confirm:

* ✅ all allocated SRs have implementations
* ✅ code is merged and builds successfully
* ✅ traceability links are established
* ✅ team is ready to plan and execute verification

---

## Related Documents

* Safety requirement format: [`../safety-requirements/requirement-format.md`](../safety-requirements/requirement-format. md)
* Allocation rules: [`../safety-requirements/allocation-rules.md`](../safety-requirements/allocation-rules.md)
* Modularity principles: [`../../architecture/modularity-principles.md`](../../architecture/modularity-principles.md)
* Lifecycle overview: [`./index.md`](./index.md)

---

## Summary

The Development phase **realizes safety intent** defined in Analysis. 

Disciplined development: 

* preserves safety logic through implementation
* maintains traceability
* identifies implementation hazards
* prepares for objective verification
