# Development Phase

## Status

Normative — Workspace level

## Purpose

The Development phase defines **how approved intent is transformed into concrete implementation** while preserving architectural, safety, and lifecycle constraints.

This phase is about **execution with discipline**, not exploration.

All development activities shall remain:

* traceable to analysis artifacts
* compliant with architectural rules
* compatible with safety arguments

---

## Scope

The Development phase applies to:

* software implementation
* hardware design activities
* interface realization
* configuration and integration work

Out of scope:

* requirement discovery (Analysis)
* evidence validation (Verification)

---

## Preconditions

Development may start only if:

* Analysis exit criteria are met
* scope is clearly defined
* assumptions are documented
* required ADRs are approved
* safety impact is understood

Starting development without these conditions is prohibited.

---

## Core Principles

### Intent Preservation

Development shall **implement the intent defined in Analysis** — not reinterpret it.

If implementation constraints require deviation:

* Analysis shall be updated
* a new decision shall be documented

Silent deviation is not acceptable.

---

### Modularity and Isolation

All implementation shall respect:

* module boundaries
* interface contracts
* ownership rules

No module shall rely on:

* undocumented behavior
* internal details of another module

---

### Traceability by Construction

Every development activity shall be traceable to:

* a GitHub Issue
* a defined lifecycle phase
* a target module
  nTraceability shall be visible in:
* commit messages
* pull requests
* project fields

---

## Development Activities

### 1. Implementation

Implementation shall:

* follow coding standards
* respect architectural constraints
* avoid speculative features

Safety-relevant code shall be clearly identified.

---

### 2. Interface Realization

Interfaces shall be implemented:

* exactly as specified
* with explicit error handling
* with defined timing behavior

Interface changes require:

* impact analysis
* documentation update
* potential ADR

---

### 3. Change Management

Any change to:

* scope
* behavior
* assumptions
* interfaces

shall be explicitly documented and reviewed.

---

### 4. Documentation Updates

Development shall update documentation when:

* behavior changes
* interfaces evolve
* assumptions are refined

Documentation lag is considered a defect.

---

## Artifacts

The Development phase produces:

| Artifact      | Description                     |
| ------------- | ------------------------------- |
| Source code   | Implementation                  |
| Configuration | Build/runtime configs           |
| Updated docs  | Architecture, lifecycle, safety |
| Pull requests | Reviewable change units         |

---

## Relation to GitHub Projects

In GitHub Projects, Development work is represented by:

* lifecycle = Development
* type = feature / mitigation / implementation
* linked pull requests

A Development item is not complete until:

* implementation is merged
* documentation is updated

---

## Exit Criteria

The Development phase is complete when:

* implementation matches analysis intent
* code is reviewed and merged
* interfaces are stable
* documentation is consistent
* readiness for verification is demonstrated

---

## Anti-Patterns

The following practices are prohibited:

* implementing without traceability
* modifying behavior without updating analysis
* bypassing review for safety-relevant changes
* deferring documentation

---

## Relation to Other Phases

* Follows: (`analysis.md`)[./analysis.md]
* Feeds into: [`verification.md`](./verification.md)

---

## Summary

The Development phase ensures that **what is built** is:

* intentional
* modular
* reviewable
* ready for verification

Discipline at this stage is essential to system integrity.
