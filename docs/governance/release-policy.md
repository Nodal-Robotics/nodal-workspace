---
title: Release Policy
nav_order: 3
parent: Governance
---

# Release Policy

## Purpose

This document defines **how releases are planned, approved, versioned, and delivered** across the NODAL ecosystem.

The release policy ensures that every release is:

* intentional
* traceable
* verifiable
* compatible with safety and lifecycle constraints

---

## Scope

This policy applies to:

* `nodal-workspace`
* all `nodal-*` software modules
* hardware reference repositories
* tooling and infrastructure repositories

Module repositories may define additional rules but **must comply with this policy**.

---

## Core Principles

### 1. Releases Are Engineering Events

A release is not a side effect of merged code.
It is a **controlled system event** that marks a validated state of the system.

### 2. No Release Without Verification

Every release must be supported by:

* verification evidence
* traceability to requirements
* explicit acceptance criteria

### 3. Safety Overrides Delivery

When safety is involved:

* safety acceptance is mandatory
* delivery timelines do not override safety decisions

---

## Release Authority

### Module Releases

Module maintainers may:

* prepare and propose module releases
* manage module-level versioning

They **cannot**:

* declare system-level readiness
* bypass safety or verification requirements

---

### System Releases (Workspace)

System releases are approved by:

* system maintainers
* safety authority (if applicable)

`nodal-workspace` is the **single source of truth** for:

* system compatibility
* cross-module alignment
* lifecycle completion

---

## Release Types

### Development Releases

Purpose:

* internal testing
* integration validation

Characteristics:

* may be unstable
* not safety-approved
* clearly marked as non-production

---

### Candidate Releases

Purpose:

* final verification
* pre-deployment validation

Requirements:

* verification complete
* known limitations documented
* safety review performed (if applicable)

---

### Production Releases

Purpose:

* deployment in real systems

Requirements:

* verification evidence complete
* safety acceptance (if required)
* full traceability established

---

## Versioning Scheme

Nodal Robotics follows **Semantic Versioning**, with additional constraints:

* **MAJOR**: incompatible or safety-impacting changes
* **MINOR**: backward-compatible functional additions
* **PATCH**: backward-compatible fixes

### Pre-1.0 Versions

* `0.x` releases are considered unstable
* interfaces may change
* safety claims are limited or absent

---

## Safety and Versioning

A version change **requires safety review** if it:

* modifies safety requirements
* impacts hazard mitigation
* alters verification assumptions

Such releases:

* must update safety documentation
* require explicit safety acceptance

---

## Release Gates

Before any production release, the following gates must be satisfied:

1. All blocking issues closed
2. Verification completed
3. Traceability updated
4. Safety acceptance recorded (if applicable)
5. Release documentation published

---

## Documentation Requirements

Each release must provide:

* release notes
* known limitations
* verification summary
* safety statement (if applicable)

Documentation is published via:

* repository tags
* GitHub releases
* associated documentation updates

---

## Forbidden Practices

The following are not allowed:

* releasing unverified code
* skipping version increments
* retroactive modification of released artefacts
* safety acceptance after deployment

---

## Relationship With Lifecycle

Releases occur at the **end of the lifecycle flow**:

* Analysis → intent defined
* Development → implementation complete
* Verification → evidence produced
* Deployment → release authorized

---

## References

* Governance index
* Contribution model
* Decision process
* Lifecycle documentation
* Safety policy
