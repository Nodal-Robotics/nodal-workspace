# Safety Policy

## Purpose

This document defines the **global safety policy** for the NODAL ecosystem.

It establishes:

* safety objectives
* responsibilities and authority
* decision and escalation rules
* non-negotiable safety principles

This policy is **normative** and applies to all repositories governed by `nodal-workspace`.

---

## Safety Objectives

The primary safety objectives are:

1. Prevent unacceptable risk to people, property, and the environment
2. Ensure safety is addressed systematically throughout the lifecycle
3. Make safety decisions explicit, traceable, and reviewable
4. Prevent schedule, cost, or convenience from overriding safety

Safety is considered a **first-class engineering concern**.

---

## Safety Scope

This policy applies to:

* system-level architecture decisions
* cross-module interactions
* lifecycle processes
* tooling and integration mechanisms

It does **not** certify:

* a specific robot
* a deployed product
* regulatory compliance for a given market

Product-level safety certification remains the responsibility of downstream integrators.

---

## Safety Principles

The following principles are mandatory:

### 1. Safety by Design

Safety is designed into the system from the earliest phases, not added afterward.

### 2. Explicit Hazard Management

All identified hazards must be:

* documented
* classified
* mitigated or explicitly accepted

### 3. Traceability

Safety claims must be supported by traceable evidence linking:

* hazards
* safety requirements
* implementation
* verification

### 4. Independence

Safety decisions must be reviewed independently from feature delivery pressure.

---

## Roles and Responsibilities

### Safety Authority

A Safety Authority role is defined with the following responsibilities:

* approve safety policies and updates
* review safety-relevant decisions and changes
* approve residual risk acceptance
* authorize safety readiness for release

The Safety Authority:

* is independent from feature ownership
* has veto power over releases and merges

---

### System Maintainers

System maintainers:

* ensure compliance with this safety policy
* enforce safety processes at workspace level
* escalate safety concerns when required

---

### Module Maintainers

Module maintainers:

* apply safety rules within their scope
* identify and report hazards
* implement assigned safety requirements

---

### Contributors

Contributors:

* must follow safety processes
* must not bypass safety reviews
* must report safety concerns immediately

---

## Safety Decision Rules

The following rules apply:

* safety concerns override delivery objectives
* unresolved safety issues block releases
* safety-relevant changes require explicit review
* undocumented safety decisions are invalid

---

## Escalation and Veto

If a safety concern cannot be resolved:

1. The issue is escalated to the Safety Authority
2. The Safety Authority may:

   * request further analysis
   * block the change
   * require architectural decision documentation

The Safety Authority’s decision is final for safety matters.

---

## Policy Enforcement

Compliance with this policy is enforced through:

* governance rules
* GitHub Projects workflows
* pull request review requirements
* release gates

Non-compliance may result in:

* rejection of contributions
* rollback of changes
* blocking of releases

---

## Relationship With Other Documents

This policy is complemented by:

* safety scope and assumptions
* hazard management process
* safety requirements definition
* safety lifecycle alignment
* traceability and evidence rules

---

## Change Management

Changes to this safety policy:

* require a documented decision (ADR)
* must be reviewed by the Safety Authority
* are versioned and traceable

---

## Status

This safety policy is in effect for all governed repositories unless explicitly stated otherwise.
