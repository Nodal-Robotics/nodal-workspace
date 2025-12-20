---
title: Architectural Assumptions
nav_order: 2
parent: Architecture
permalink: /architecture/assumptions/
---

# Architectural Assumptions

## 1. Purpose

This document defines the **explicit assumptions** on which the NODAL system architecture is based.

Assumptions are conditions believed to be true and relied upon when making architectural and safety decisions.

Making assumptions explicit is essential to:

* avoid hidden constraints
* bound system responsibility
* support safety reasoning and certification
* enable controlled system evolution

This document is **normative**.

---

## 2. Scope

This document applies to:

* system-level architecture
* lifecycle definition
* safety case construction

It does not define:

* module-specific assumptions (documented in module repositories)
* installation- or deployment-specific assumptions

---

## 3. Categories of Assumptions

Architectural assumptions are grouped into the following categories:

* Operational assumptions
* Technical assumptions
* Organizational assumptions
* Safety-related assumptions

Each assumption category must be considered when evaluating changes or introducing new modules.

---

## 4. Operational Assumptions

The NODAL system assumes that:

* the system is integrated and deployed by competent personnel
* operational procedures are defined outside the system boundary
* the system operates within documented environmental limits
* maintenance and updates follow defined release processes

Operational misuse beyond documented assumptions is **out of scope**.

---

## 5. Technical Assumptions

The architecture assumes that:

* modules communicate exclusively via defined interfaces
* module interfaces are stable within a major version
* timing and resource constraints are respected by modules
* failures are detected and reported according to defined rules

Implicit dependencies between modules are **not assumed** and are prohibited.

---

## 6. Organizational Assumptions

The system assumes that:

* contributors follow the defined governance model
* architectural rules are enforced through reviews and tooling
* significant decisions are documented using ADR
* deviations from standards are explicitly justified

The architecture relies on process discipline as a system property.

---

## 7. Safety-Related Assumptions

Safety reasoning assumes that:

* hazards are identified at system level
* safety requirements are derived and allocated appropriately
* verification activities provide objective evidence
* residual risks are explicitly accepted

Safety assumptions must be traceable and reviewed periodically.

---

## 8. Handling Assumption Violations

If an assumption is found to be invalid:

* the impact on architecture and safety must be assessed
* affected safety claims must be re-evaluated
* an ADR may be required

Invalid assumptions may require changes to:

* system boundaries
* safety scope
* lifecycle processes

---

## 9. Evolution of Assumptions

Assumptions are not static.

Changes to assumptions:

* must be explicit
* require review
* may trigger architectural or safety updates

Uncontrolled assumption drift is a major source of system risk.

---

## 10. Related Documents

* System boundaries: `system-boundaries.md`
* Safety scope and assumptions: `../safety/safety-scope-and-assumptions.md`
* Architecture decisions: `../governance/adr/`

---

> Assumptions are architectural commitments.
> Making them explicit is a safety measure.
