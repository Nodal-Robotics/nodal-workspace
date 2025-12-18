# Safety Scope and Assumptions

## Purpose

This document defines the **scope, boundaries, and assumptions** of the global safety case for the  NODAL ecosystem.

Its purpose is to:

* clearly state what is covered by the safety framework
* explicitly state what is not covered
* document assumptions that safety claims rely on

This avoids ambiguity, misuse, and unrealistic safety expectations.

---

## Safety Scope

### In Scope

The following elements are within the scope of the global safety case:

* the NODAL framework architecture
* system integration via `nodal-workspace`
* cross-module interactions
* lifecycle and governance processes
* safety-related engineering practices

The safety case addresses **how safety is engineered**, not how a specific robot behaves in the real world.

---

### Out of Scope

The following are explicitly out of scope:

* certification of a specific product or robot
* compliance with country-specific regulations
* deployment environment-specific risks
* misuse or modification of modules outside defined assumptions

Product integrators are responsible for:

* system-level hazard analysis
* regulatory compliance
* operational safety validation

---

## System Boundaries

The global safety case assumes:

* modules interact only through defined interfaces
* integration is performed according to documented rules
* lifecycle and governance processes are followed

Violating these boundaries invalidates safety assumptions.

---

## Operational Assumptions

Safety claims rely on the following assumptions:

* the system is used in accordance with its documented purpose
* operating conditions remain within specified limits
* hardware behaves according to manufacturer specifications
* safety-related configuration parameters are not altered arbitrarily

---

## Organizational Assumptions

The safety framework assumes:

* contributors follow governance rules
* safety reviews are performed when required
* decisions impacting safety are documented
* releases follow the defined release policy

Failure to follow these assumptions compromises safety claims.

---

## Assumptions on Tooling

The safety case assumes:

* GitHub is used as the authoritative system for:

  * issue tracking
  * decision documentation
  * traceability

* project workflows are not bypassed

* history and traceability are preserved

---

## Assumptions on Change Management

It is assumed that:

* safety-relevant changes are identified
* impact analysis is performed before implementation
* safety documentation is updated accordingly

Undocumented changes invalidate related safety evidence.

---

## Handling of Assumption Violations

If an assumption is violated:

* related safety claims are considered invalid
* a safety review must be triggered
* corrective actions must be defined and tracked

---

## Relationship With Other Safety Documents

This document constrains and informs:

* hazard identification and classification
* safety requirement definition
* traceability expectations
* safety acceptance decisions

---

## Change Management

Changes to scope or assumptions:

* require a documented decision (ADR)
* must be reviewed by the Safety Authority
* may require re-evaluation of hazards and requirements

---

## Status

This scope and assumptions document is normative for the global safety case unless explicitly stated otherwise.
