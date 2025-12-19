---
title: Hazard Identification
nav_order: 1
parent: Hazard Management
---

# Hazard Identification

## Purpose

This document defines **how hazards are identified, described, and documented** within the  NODAL safety framework.

Its objective is to ensure that hazard identification is:

* systematic
* consistent across modules
* explicit and reviewable

Hazard identification is the **first mandatory step** of the hazard management process.

---

## When to Identify Hazards

Hazard identification must be performed:

* during system and architectural analysis
* when introducing new functionality
* when modifying existing behavior
* when changing interfaces or assumptions
* after discovering incidents or near-misses

Hazard identification is not a one-time activity; it is **continuous**.

---

## Sources of Hazards

Hazards may originate from:

* functional behavior
* incorrect or unexpected inputs
* hardware failures
* software faults
* timing or performance violations
* integration between modules
* misuse or foreseeable misuse
* organizational or process failures

All plausible sources must be considered.

---

## Hazard Description Requirements

Each hazard must be documented with the following minimum information:

### 1. Hazard Title

A concise, descriptive name.

---

### 2. Hazard Description

A clear explanation of:

* what can go wrong
* how harm could occur
* what is affected

Avoid vague or generic descriptions.

---

### 3. Triggering Conditions

Conditions or events that could lead to the hazard, such as:

* specific system states
* failures
* environmental conditions
* incorrect usage

---

### 4. Affected Elements

Identification of:

* modules
* interfaces
* lifecycle phases
* operational contexts

---

### 5. Assumptions

Explicit assumptions relied upon when identifying the hazard.

If assumptions change, the hazard must be re-evaluated.

---

## Level of Abstraction

Hazards should be identified at an **appropriate level of abstraction**:

* high enough to be system-relevant
* low enough to be actionable

Avoid:

* purely implementation-level bugs
* overly abstract or non-actionable statements

---

## Hazard Uniqueness

Each hazard:

* must be uniquely identifiable
* must not duplicate existing hazards

Related hazards should be linked, not merged indiscriminately.

---

## Hazard Recording

Hazards are recorded as:

* dedicated GitHub issues
* tagged as safety-relevant
* classified using project fields

The issue description must contain all required information.

---

## Review and Validation

All identified hazards must be:

* reviewed by maintainers
* validated by the Safety Authority

Unreviewed hazards are considered **open and blocking**.

---

## Common Pitfalls

The following practices are discouraged:

* delaying hazard identification until late phases
* assuming hazards are "obvious"
* hiding hazards inside implementation issues
* skipping documentation due to uncertainty

Uncertainty should be documented, not ignored.

---

## Relationship With Other Documents

This document feeds into:

* risk classification
* safety requirement definition
* traceability model

---

## Change Management

Changes to hazard identification rules:

* require a documented decision (ADR)
* must be reviewed by the Safety Authority

---

## Status

This document is normative for hazard identification across the  NODAL ecosystem.
