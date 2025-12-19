---
title: Evidence Expectations
nav_order: 2
parent: Traceability
---

# Evidence Expectations

This document defines what constitutes **acceptable safety evidence** within the  NODAL ecosystem.

Safety evidence is a **core engineering artifact**.  
It substantiates safety requirements, justifies safety claims, and enables objective audits.

---

## 🎯 Purpose

The objectives of this document are to:

- define what is considered valid safety evidence
- ensure consistency across repositories and modules
- prevent weak, subjective, or unverifiable claims
- support long-term auditability and certification readiness

---

## 🧩 Scope

This document applies to:

- all safety requirements
- all verification activities
- all tools producing safety-relevant outputs

It applies across:
- software modules
- hardware components
- tooling and processes

---

## 🧠 Core Principle

> **Evidence is not a document.  
> Evidence is a reproducible result produced by a controlled process.**

A PDF, screenshot, or statement **is not evidence by itself**.

---

## 🔗 Position in the Safety Chain

Evidence occupies a fixed position in the safety traceability chain:

- Hazard
- Safety Requirement
- Design / ADR
- Implementation
- Verification
- Evidence
- Safety Claim

If evidence is missing, the safety claim is invalid.

---

## ✅ General Validity Criteria

An artifact is considered **valid safety evidence** only if **all** of the following conditions are met:

1. **Traceable**  
   - Linked to a specific safety requirement
   - Linked to a specific commit or version

2. **Reproducible**  
   - Can be regenerated using the documented process
   - Independent of developer machine state

3. **Objective**  
   - Does not rely on subjective interpretation
   - Has a clear pass/fail or measurable outcome

4. **Tool-Generated or Justified**  
   - Produced by a documented tool  
   - OR manually produced with explicit justification

5. **Preserved**  
   - Stored or referenced in a durable location
   - Accessible for future audit

If **any** criterion is not met, the artifact is **not acceptable** as safety evidence.

---

## 🛠️ Tool Classification and Evidence Acceptance

### Class A — Safety-Critical Tools

**Examples:**
- compiler
- code generator
- blocking static analysis
- hardware synthesis tools

**Evidence Types:**
- build logs
- analysis reports
- generated artifacts hashes

**Requirements:**
- tool version explicitly documented
- deterministic execution
- changes subject to impact analysis
- evidence must be reproducible

---

### Class B — Safety-Support Tools

**Examples:**
- unit / integration test frameworks
- simulators
- coverage tools

**Evidence Types:**
- test reports
- simulation outputs
- coverage metrics

**Requirements:**
- assumptions documented
- limitations stated
- results reproducible
- scope clearly defined

Simulation results are acceptable **only** within the documented model limits.

---

### Class C — Informational Tools

**Examples:**
- formatters
- linters (non-blocking)
- dashboards

**Evidence Types:**
- informational only

❌ **Not acceptable as direct safety evidence**

---

## 🧪 Accepted Evidence Types

### 1. Automated Test Results

**Examples:**
- unit test reports
- integration test reports
- HIL/SIL test outputs

**Acceptance Conditions:**
- automated execution
- version-controlled test code
- clear pass/fail criteria
- linked to safety requirement

---

### 2. Static Analysis Reports

**Examples:**
- MISRA compliance reports
- rule violation summaries

**Acceptance Conditions:**
- rule set defined
- scope clearly stated
- justification for deviations documented

---

### 3. Build Artifacts

**Examples:**
- binary hashes
- compilation logs
- linker maps

**Acceptance Conditions:**
- deterministic build
- toolchain documented
- artifact traceable to commit

---

### 4. Simulation Results

**Examples:**
- timing simulations
- fault injection results

**Acceptance Conditions:**
- model assumptions documented
- limitations explicitly stated
- reproducibility demonstrated

Simulation **does not replace verification** unless explicitly justified.

---

### 5. Manual Analysis (Exceptional)

**Examples:**
- formal reasoning
- expert review
- architectural argumentation

**Acceptance Conditions:**
- explicit justification
- documented methodology
- peer review
- traceable to requirement

Manual evidence is **never the default**.

---

## ❌ Non-Acceptable Evidence

The following are explicitly rejected as safety evidence:

- screenshots
- unversioned documents
- verbal statements
- undocumented test runs
- “it works on my machine”
- logs without context or traceability

---

## 🔁 Evidence Evolution and Change

When any of the following changes:

- safety requirement
- implementation
- verification method
- tooling version

→ existing evidence must be **re-evaluated**.

Outdated evidence is considered **invalid**.

---

## 🔗 Integration with GitHub

Evidence must be linked using:

- Issue references
- Pull Requests
- CI run identifiers
- Artifact storage links

GitHub is used as a **traceability carrier**, not as the evidence itself.

---

## 🛡️ Audit Readiness

For any safety claim, it must be possible to:

1. identify the safety requirement
2. identify the verification method
3. retrieve the evidence
4. reproduce the result
5. justify the conclusion

Failure at any step invalidates the claim.

---

## 📌 References

- Traceability Model
- Safety Requirements
- Tooling and Safety Evidence
- Safety Lifecycle