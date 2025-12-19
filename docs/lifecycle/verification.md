---
title: Verification Phase
nav_order: 3
parent: Lifecycle
---

# Verification Phase

## Status

Normative — Workspace level

## Purpose

The Verification phase defines **how evidence is produced to demonstrate that the implemented system satisfies its intended behavior, constraints, and safety requirements**.

Verification answers the question:

> *Did we build the system right?*

It is distinct from validation, which asks whether the right system was built.

---

## Scope

The Verification phase applies to:

* software modules
* hardware designs
* interfaces and integrations
* safety mitigations
* lifecycle and process compliance

Out of scope:

* requirement discovery (Analysis)
* operational acceptance (Deployment)

---

## Core Principles

### Evidence Over Confidence

Verification is based on **objective evidence**, not belief or experience.

Acceptable evidence includes:

* test results
* analysis reports
* inspections and reviews
* formal arguments

A feature is not verified until evidence exists.

---

### Requirement-Centric Verification

All verification activities shall be traceable to:

* functional requirements
* safety requirements
* architectural constraints

Tests without traceability are insufficient.

---

### Proportional Rigor

Verification rigor shall be proportional to:

* criticality
* safety impact
* system exposure

Safety-relevant functionality requires stronger evidence.

---

## Verification Activities

### 1. Test Design

Tests shall be designed to:

* cover nominal behavior
* exercise boundary conditions
* demonstrate failure handling

Test intent shall be documented.

---

### 2. Test Execution

Tests may include:

* unit tests
* integration tests
* system tests
* hardware-in-the-loop tests

Automated tests are preferred when feasible.

---

### 3. Analysis and Review

Not all properties are tested.

Verification may also rely on:

* static analysis
* timing analysis
* design reviews
* code inspections

---

### 4. Evidence Collection

All verification results shall be:

* recorded
* versioned
* linked to requirements and issues

Evidence shall be reproducible.

---

## Artifacts

The Verification phase produces:

| Artifact         | Description                  |
| ---------------- | ---------------------------- |
| Test cases       | Defined verification actions |
| Test results     | Execution outcomes           |
| Analysis reports | Non-test evidence            |
| Evidence records | Traceable proof              |

---

## Relation to GitHub Projects

In GitHub Projects, Verification work is represented by:

* lifecycle = Verification
* type = test / evidence
* linked pull requests or reports

An item is not complete until evidence is attached.

---

## Exit Criteria

The Verification phase is complete when:

* all planned verification activities are executed
* evidence demonstrates requirement satisfaction
* safety mitigations are verified
* unresolved issues are explicitly accepted or deferred

---

## Anti-Patterns

The following practices are prohibited:

* declaring verification complete without evidence
* relying solely on manual testing for critical functions
* unverifiable claims
* undocumented test results

---

## Relation to Other Phases

* Follows: [`development.md`](./development.md)
* Feeds into: [`deployment.md`](./deployment.md)
* Supports: Safety Case

---

## Summary

The Verification phase provides **objective confidence** that the system behaves as intended.

It transforms implementation into **defensible evidence**, enabling safe deployment and credible claims.
