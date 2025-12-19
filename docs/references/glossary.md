---
title: Glossary
nav_order: 3
parent: References
---

# Glossary

## Purpose

This document defines the **standard terminology** used throughout the NODAL ecosystem documentation and governance. 

Consistent terminology is essential for:  

* clear communication across teams
* precise specification of requirements
* auditable documentation
* effective knowledge transfer

This glossary is **normative**. When in doubt about terminology, use the definitions provided here.

---

## A

### Acceptance (Risk Acceptance)

A formal, documented decision by authorized personnel to tolerate a known hazard or residual risk.  Acceptance is based on explicit justification, proportionate authority, and clear conditions.

See:  [`safety/hazard-management/risk-acceptance.md`](../safety/hazard-management/risk-acceptance.md)

### Allocation (Safety Requirement Allocation)

The process of assigning a safety requirement to a specific module, layer, component, or process that is responsible for implementing the requirement.

See: [`safety/safety-requirements/allocation-rules.md`](../safety/safety-requirements/allocation-rules.md)

### Architectural Decision Record (ADR)

A document that captures a significant technical or organizational decision, including its context, alternatives, chosen option, and consequences.  ADRs are immutable once accepted.

See: [`governance/decision-process. md`](../governance/decision-process.md)

### Architecture

The system-level structure that defines how modules interact, what responsibilities are allocated, and which constraints must be respected.

See: [`architecture/overview.md`](../architecture/overview.md)

---

## D

### Deployment

The phase of the lifecycle where verified and accepted artifacts are released for operational use, including formal risk acceptance and operational constraint documentation.

See: [`lifecycle/deployment.md`](../lifecycle/deployment.md)

### Development

The phase of the lifecycle where approved intent is transformed into concrete implementation while preserving architectural, safety, and lifecycle constraints.

See: [`lifecycle/development.md`](../lifecycle/development.md)

### Determinism (Timing Determinism)

A system property where behavior is **time-predictable by construction**.  Deterministic systems have bounded execution times, bounded latencies, and explicit scheduling assumptions.

See: [`architecture/timing_budget.md`](../architecture/timing_budget.md)

---

## E

### Evidence

Objective, reproducible, immutable artifacts produced during verification that demonstrate that a safety requirement is satisfied.  Examples:  test reports, CI logs, analysis results.

See: [`safety/traceability/evidence-expectations.md`](../safety/traceability/evidence-expectations.md)

---

## F

### Firm Real-Time

A timing category where occasional deadline misses are tolerated if stale data is discarded.  Used for functions where missing a deadline is acceptable if the result is not used.

See: [`architecture/timing_budget.md`](../architecture/timing_budget.md)

---

## G

### Governance

The model that defines how decisions are made, how contributions are accepted, and how the system evolves while respecting safety and architectural constraints.

See: [`governance/index.md`](../governance/index.md)

---

## H

### Hard Real-Time

A timing category where deadlines **must always be met**. Used for safety-critical functions where missing a deadline is unacceptable.

See: [`architecture/timing_budget.md`](../architecture/timing_budget. md)

### Hazard

A potential source of harm arising from system behavior, failure, misuse, or interaction with the environment.  Hazards may be functional, architectural, operational, or organizational.

See: [`safety/hazard-management/hazard-identification.md`](../safety/hazard-management/hazard-identification.md)

### Hazard Management

The systematic process for identifying, classifying, mitigating, and accepting hazards throughout the system lifecycle.

See: [`safety/hazard-management/index.md`](../safety/hazard-management/index.md)

---

## I

### Interface

A formal contract that defines interaction points between modules, including data exchanged, timing expectations, error handling behavior, and versioning rules.

See: [`architecture/interfaces.md`](../architecture/interfaces.md)

---

## L

### Lifecycle

The end-to-end process that governs how work flows through phases (Analysis, Development, Verification, Deployment) while maintaining safety, quality, and traceability.

See: [`lifecycle/index.md`](../lifecycle/index.md)

---

## M

### Mitigation

An action, design feature, procedure, or requirement that reduces or eliminates the risk associated with a hazard.

See: [`safety/hazard-management/index.md`](../safety/hazard-management/index.md)

### Module

A self-contained functional unit with a clearly defined responsibility, independently developed and versioned, that exposes only declared interfaces and avoids implicit coupling.

See: [`architecture/modularity-principles.md`](../architecture/modularity-principles.md)

### Modularity

A system property where components are loosely coupled, have single clear responsibilities, interact only through explicit interfaces, and can be developed and verified independently.

See: [`architecture/modularity-principles.md`](../architecture/modularity-principles.md)

---

## N

### NODAL

The **Nodular ECU-based Design for Autonomous Locomotion** framework — a modular robotics system architecture inspired by automotive ECU-based design.

See: [`architecture/overview.md`](../architecture/overview.md)

---

## O

### Orphan (Traceability)

An artifact without required linkages — e.g., a hazard without a mitigating safety requirement, or evidence without a linked verification activity.  Orphans are considered traceability defects.

See: [`safety/traceability/traceability-model.md`](../safety/traceability/traceability-model.md)

---

## R

### Residual Risk

The risk that remains after mitigation has been implemented and verified. Residual risk may be accepted if it falls within organizational tolerance. 

See: [`safety/hazard-management/risk-acceptance.md`](../safety/hazard-management/risk-acceptance.md)

### Risk

A combination of **severity** (magnitude of potential harm) and **likelihood** (probability of occurrence). Risk may also consider **exposure** (frequency of hazardous situation).

See: [`safety/hazard-management/risk-classification.md`](../safety/hazard-management/risk-classification. md)

### Risk Classification

The process of systematically assigning risk levels (RC0–RC4) to hazards based on severity, probability, and exposure.

See: [`safety/hazard-management/risk-classification.md`](../safety/hazard-management/risk-classification.md)

---

## S

### Safety Authority

A role responsible for reviewing safety-relevant decisions, approving risk acceptance, and authorizing safety readiness for release.  This role is independent from feature ownership.

See: [`safety/safety-policy. md`](../safety/safety-policy.md)

### Safety Case

A structured justification that a system is acceptably safe for its intended use.  The safety case comprises hazard management, safety requirements, verification, and traceability.

See: [`safety/index.md`](../safety/index.md)

### Safety Requirement

A verifiable, traceable, and allocatable statement that specifies a behavior or constraint required to mitigate a hazard or reduce risk to acceptable levels. 

Notation: **SR-<LEVEL>-<DOMAIN>-<NUMBER>** (e.g., SR-SYS-CTRL-001)

See: [`safety/safety-requirements/requirement-format.md`](../safety/safety-requirements/requirement-format.md)

### Severity

A classification of the **magnitude of potential harm** if a hazard materializes. Severity ranges from negligible (S0) to catastrophic (S4).

See: [`safety/hazard-management/risk-classification. md`](../safety/hazard-management/risk-classification.md)

### Soft Real-Time

A timing category where latency impacts quality but not correctness. Missing deadlines is tolerable if the system continues to function correctly.

See: [`architecture/timing_budget.md`](../architecture/timing_budget.md)

---

## T

### Timing Budget

A system-level definition of timing constraints (execution time, end-to-end latency, jitter, communication delay) that modules must respect to enable safe composition.

See: [`architecture/timing_budget.md`](../architecture/timing_budget.md)

### Traceability

The property that safety artifacts (hazards, requirements, implementation, evidence) are **explicitly linked** and can be navigated in both directions (forward and backward).

See: [`safety/traceability/traceability-model.md`](../safety/traceability/traceability-model.md)

---

## V

### Verification

The phase of the lifecycle where evidence is produced to demonstrate that implemented systems satisfy their intended behavior, constraints, and safety requirements.

See: [`lifecycle/verification.md`](../lifecycle/verification.md)

---

## W

### Workspace

The central repository (`nodal-workspace`) that defines global rules, architecture, lifecycle, governance, and safety standards applicable to all NODAL projects.  The workspace does not implement functional behavior. 

See: [`architecture/system-boundaries.md`](../architecture/system-boundaries.md)

---

## Related Documents

* Abbreviations:  [`abbreviations. md`](./abbreviations.md)
* Safety terminology: [`safety/index.md`](../safety/index.md)