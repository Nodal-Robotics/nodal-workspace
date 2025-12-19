# Verification Phase — Safety Activities

## Status

Normative — Workspace level

## Purpose

This document defines the **safety-specific activities during the Verification phase** of the system lifecycle. 

Verification is where safety claims are **validated with objective evidence**.

The focus is on:

* executing planned verification activities
* collecting evidence that mitigations work
* confirming hazard closure
* identifying residual risks

---

## Scope

This document applies to:

* verification of safety requirements
* testing of mitigations
* analysis of implementation
* evidence collection and traceability

It does **not** prescribe:

* specific test frameworks
* detailed test case authorship
* performance optimization

---

## Core Principle

> **Safety is not verified by belief or best practice — only by objective evidence.**

---

## Safety Verification Objectives

During Verification, the following objectives must be met:

1. **Execute all planned verification activities** (tests, analyses, inspections)
2. **Collect objective evidence** that SRs are satisfied
3. **Confirm hazard closure** — verify that mitigations are effective
4. **Identify residual risks** that remain post-mitigation
5. **Prepare for deployment** with complete evidence trail

---

## Pre-Verification Gate

Before verification starts, confirm: 

* ✅ all implementations are complete
* ✅ code is merged and stable
* ✅ verification plan exists for all SRs
* ✅ test environment is ready
* ✅ traceability is established

---

## Activities

### 1. Verification Planning

For each safety requirement, define:

* **verification method**: test, analysis, inspection, or simulation
* **test cases or scenarios**: specific conditions to evaluate
* **pass/fail criteria**: objective acceptance conditions
* **environment**: hardware, software, configuration
* **independence**: who executes (peer vs. independent reviewer)

Document in a **verification plan issue** linked to the SR.

---

### 2. Test Execution

Execute planned tests: 

* **nominal cases**: expected behavior
* **boundary cases**: limits of specified ranges
* **error cases**: how the system handles failures
* **integration cases**: interaction between modules

For each test:

* record the execution date and environment
* document inputs and outputs
* confirm pass/fail against acceptance criteria

---

### 3. Test Evidence Collection

Capture evidence: 

* **test logs**: detailed execution record
* **coverage reports**: what code was exercised
* **failure traces**: if any test failed, detailed debugging information
* **configuration**:  exact build, environment, parameters used

---

### 4. Analysis Activities

In addition to testing, perform:

* **static analysis**: code review for safety-relevant patterns
* **timing analysis**: verify that timing requirements are met
* **fault tree analysis**: confirm that identified failure modes are mitigated
* **interface analysis**: verify interaction contracts

Document analysis results and findings. 

---

### 5. Inspection and Review

For safety-critical code or design:

* conduct structured inspections
* document inspection findings
* require fixes for safety issues identified

---

### 6. Simulation and Modeling

Where appropriate:

* simulate failure modes
* verify that mitigations respond correctly
* confirm safe-state transitions

---

### 7. Hazard Closure Verification

For each identified hazard:

* verify that the assigned mitigation is effective
* confirm that residual risk is reduced to acceptable level
* document evidence linking hazard → SR → verification → evidence

Close the hazard issue with reference to evidence.

---

### 8. Failed Test Analysis

If a test fails: 

* **identify root cause**: is this an implementation bug or a requirement misunderstanding?
* **assess impact**: does this failure affect hazard closure?
* **plan correction**: is it a code fix, requirement change, or test update? 
* **re-test**: confirm the fix resolves the issue

All failed tests and resolutions must be documented.

---

### 9. Residual Risk Identification

After verification:

* identify any **unverifiable claims** or assumptions
* identify any **unmitigated hazards** or edge cases
* document these as **residual risks** for consideration in Deployment

---

### 10. Verification Completeness Review

Verify that: 

* ✅ all SRs have verification activities
* ✅ all verification activities are executed
* ✅ all evidence is collected and linked
* ✅ no orphan hazards remain
* ✅ traceability is complete

---

## Verification Evidence Standards

Evidence must meet these standards:

| Standard          | Requirement                             |
| ----------------- | --------------------------------------- |
| Objective         | Results are measurable, not subjective  |
| Reproducible      | Independent person can repeat           |
| Traceable         | Clearly linked to SR and hazard         |
| Complete          | Covers all acceptance criteria          |
| Independent       | Preferably by someone not in dev team  |
| Immutable         | Not altered once produced               |
| Proportional      | Rigor matches risk level                |

---

## GitHub Integration

Verification work is tracked using:

* **Verification issues** (type:  `verification` or `test`)
* **Test result issues** linking to SRs
* **Evidence artifacts** (links to logs, reports, CI artifacts)
* **Project fields**:
  * `Lifecycle = Verification`
  * `Verification Status = Planned / In Progress / Passed / Failed`
  * `Evidence Link = <URL>`

---

## Verification Records

Each verification activity produces a record including:

* SR ID verified
* verification method
* date executed
* environment and configuration
* results (pass/fail)
* evidence artifacts
* responsible reviewer

---

## Independence Requirements

For different risk levels:

| Risk Class | Verification Independence                  |
| ---------- | ------------------------------------------ |
| RC0/RC1    | Peer review acceptable                     |
| RC2        | Independent review recommended             |
| RC3        | Independent verification required          |
| RC4        | Not applicable (unacceptable risk)         |

Independent verifier must not be original implementer.

---

## Handling Verification Findings

### Minor Findings

Non-safety issues (cosmetic, minor bugs):

* log and fix
* re-test if necessary

### Major Findings

Safety-relevant issues:

* **immediately stop** further development
* **escalate** to Safety Authority
* **assess impact** on other SRs and hazards
* **plan correction** — code fix or requirement change
* **re-verify** after fix

---

## Exit Criteria

The Verification phase is complete when:

* ✅ all planned verification activities are executed
* ✅ all SRs have supporting evidence
* ✅ no critical or major findings remain open
* ✅ residual risks are identified and documented
* ✅ traceability is verified complete
* ✅ Safety Authority approves verification readiness

---

## Anti-Patterns

The following practices are **prohibited**:

* testing without a documented plan
* declaring verification "done" without evidence
* accepting "it works in practice" without objective proof
* skipping verification for "low-risk" changes
* incomplete traceability (evidence without linked SR)

---

## Relation to System Verification Phase

The safety verification phase is embedded in the system verification phase defined in [`../../lifecycle/verification.md`](../../lifecycle/verification.md).

Safety verification: 

* validates that mitigations work
* provides evidence for safety claims
* informs deployment decisions

---

## Next Phase Gate

Before transitioning to Deployment, confirm: 

* ✅ all SRs are verified or residual risk is accepted
* ✅ evidence is complete and traceable
* ✅ no critical findings remain
* ✅ Safety Authority approves readiness

---

## Related Documents

* Evidence expectations: [`../traceability/evidence-expectations. md`](../traceability/evidence-expectations.md)
* Traceability model: [`../traceability/traceability-model.md`](../traceability/traceability-model. md)
* Safety requirements: [`../safety-requirements/`](../safety-requirements/)
* Lifecycle overview: [`./index.md`](./index.md)

---

## Summary

The Verification phase **validates that safety mitigations work** and **builds objective evidence** for safety claims. 

Rigorous verification: 

* provides confidence in safety
* supports certification and compliance
* enables safe deployment
* creates an auditable record