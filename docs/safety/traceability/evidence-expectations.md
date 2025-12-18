# Evidence Expectations

## Purpose

This document defines what constitutes **acceptable safety evidence** within the Axion Robotics / NODAL safety framework.

Evidence is the objective demonstration that a **Safety Requirement (SR)** has been correctly implemented and verified.

This document prevents:

* superficial or cosmetic verification
* unverifiable claims
* non-reproducible test results

---

## Core Principles

1. **Evidence is mandatory**
   A safety requirement is not considered verified without evidence.

2. **Evidence is objective**
   Opinions, assertions, or code comments are not evidence.

3. **Evidence is reproducible**
   An independent engineer must be able to reproduce the result.

4. **Evidence matches risk level**
   Higher risk requires stronger and more rigorous evidence.

5. **Evidence is immutable**
   Once produced, evidence shall not be altered.

---

## Evidence Types

Acceptable evidence types include:

| Evidence Type     | Description                                 |
| ----------------- | ------------------------------------------- |
| Test Report       | Results from executed test cases            |
| Analysis Report   | Formal analysis or calculation              |
| Simulation Output | Logged and parameterized simulation results |
| Inspection Record | Structured inspection checklist             |
| CI Artifact       | Automated pipeline outputs                  |

Evidence must always reference the **exact SR ID** it supports.

---

## Evidence vs Verification Method

Each verification method requires specific evidence.

| Verification Method | Minimum Evidence                |
| ------------------- | ------------------------------- |
| Test                | Test report + logs              |
| Analysis            | Analysis document + assumptions |
| Inspection          | Inspection checklist            |
| Simulation          | Simulation logs + configuration |

---

## Evidence Strength by Risk Class

Evidence rigor scales with **Risk Class (RC)**.

| Risk Class | Evidence Expectation                           |
| ---------- | ---------------------------------------------- |
| RC0        | Informal confirmation                          |
| RC1        | Basic test or inspection                       |
| RC2        | Formal test with documented results            |
| RC3        | Independent verification + documented analysis |
| RC4        | Not applicable (risk not acceptable)           |

---

## Evidence Content Requirements

Each evidence artifact must include:

* reference to Safety Requirement ID
* verification method used
* environment and configuration
* execution date
* responsible person or system
* pass/fail outcome

Missing information invalidates the evidence.

---

## GitHub Integration

### Evidence Representation

Evidence is referenced through:

* links to CI artifacts
* attached reports
* repository paths

Evidence links must be recorded in:

* Safety Requirement issue
* Verification issue or PR

---

### Required GitHub Fields

* `Verification Status`
* `Evidence Link`
* `Verification Date`

---

## Independence Requirements

For higher risk classes:

* RC2: peer review recommended
* RC3: independent verification required

The verifier must not be the original implementer.

---

## Evidence Retention

Evidence must be retained:

* for the lifetime of the corresponding release
* and any derived releases

Evidence may only be archived or removed following a formal review.

---

## Audit Expectations

Auditors must be able to:

* locate evidence from SR or hazard
* verify reproducibility
* confirm independence when required

Evidence gaps are treated as safety non-conformities.

---

## Relationship to Other Documents

* Traceability model → `traceability-model.md`
* Verification lifecycle → `safety-lifecycle/verification-phase.md`
* Safety requirements → `safety-requirements/`

---

## Summary

Acceptable safety evidence is:

* objective
* reproducible
* proportional to risk
* traceable
* immutable

Without evidence, there is no verified safety.
