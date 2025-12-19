---

title: System Boundaries
nav_order: 6
parent: Architecture
---

# Timing Budget & Determinism Policy

## Status

Normative — Workspace level

## Purpose

This document defines the **global timing and determinism rules** applicable to all NODAL-based systems and modules.

It does **not** define concrete execution times for any specific module. Instead, it provides:

* timing assumptions
* budgeting rules
* allocation principles
* verification expectations

These rules ensure that independently developed modules can be **composed into a deterministic system**.

---

## Scope

This policy applies to:

* all software modules (`nodal-*`)
* all hardware abstraction layers
* all tooling that impacts execution, scheduling, or communication

Out of scope:

* module-specific WCET values
* hardware-specific clock configurations
* OS or RTOS implementation details

These must be defined at module level.

---

## Core Principles

### Determinism First

All NODAL systems shall be **time-deterministic by construction**.

This implies:

* bounded execution times
* bounded communication latencies
* explicit scheduling assumptions

Best-effort or unbounded timing behavior is prohibited in safety-relevant paths.

---

### Budget, Not Measurement

The workspace defines **timing budgets**, not measured values.

Measured values:

* depend on hardware
* depend on compiler
* evolve over time

Budgets:

* define contracts
* enable composition
* support early validation

---

### Hierarchical Timing Model

Timing is managed hierarchically:

1. **System-level budget** (workspace)
2. **Module-level allocation** (module repos)
3. **Function-level WCET** (implementation)

No level may violate the constraints of the level above.

---

## System-Level Timing Model

At workspace level, the system is modeled as:

* a set of periodic and aperiodic activities
* communicating via bounded interfaces
* executing on one or more processing units

The following assumptions apply:

* A global time base exists (logical or physical)
* Scheduling policy is known and documented at system integration level
* Communication paths are explicitly identified

---

## Timing Categories

Each activity shall be classified into one of the following categories:

| Category       | Description                                       |
| -------------- | ------------------------------------------------- |
| Hard real-time | Deadline must always be met                       |
| Firm real-time | Occasional misses tolerated, stale data discarded |
| Soft real-time | Latency impacts quality, not correctness          |
| Best-effort    | No guarantees                                     |

Safety-relevant functions shall be **hard or firm real-time only**.

---

## Budget Definition Rules

At workspace level, the following budget dimensions shall be defined:

* Execution time
* End-to-end latency
* Jitter
* Communication delay

Budgets shall be expressed:

* as maximum values
* with explicit margins
* independently of hardware frequency

Example (illustrative only):

> Control loop latency ≤ 10 ms (including sensing, computation, actuation)

---

## Allocation to Modules

Timing budgets shall be allocated to modules according to:

* functional responsibility
* criticality
* reuse constraints

Rules:

* Each module shall document its assumed input timing
* Each module shall declare its output timing guarantees
* Budgets shall include integration overhead

Module-level documents shall reference this policy explicitly.

---

## Interfaces and Timing Contracts

All inter-module interfaces shall define:

* triggering conditions
* expected arrival rate
* maximum acceptable latency
* timeout behavior

Undefined timing behavior at interfaces is prohibited.

---

## Verification Expectations

Each module shall provide evidence that:

* execution fits within allocated budget
* timing assumptions are stated and justified
* worst-case paths are identified

Acceptable evidence includes:

* static analysis
* measurement with margin
* analytical reasoning

---

## Tooling Impact

Build systems, middleware, and tooling shall not:

* introduce hidden buffering
* introduce unbounded retries
* obscure scheduling behavior

Tooling that impacts timing shall be documented in `tooling/`.

---

## Relation to Safety Case

Timing determinism is a **safety-enabling property**.

This document supports:

* hazard mitigation arguments
* freedom-from-interference claims
* verification completeness

Timing-related hazards shall reference this policy.

---

## References

* Lifecycle: `docs/lifecycle/verification.md`
* Safety: `docs/safety/safety-lifecycle/verification-phase.md`
* Architecture principles: `modularity-principles.md`

---

## Change Management

Changes to this document:

* require an ADR
* must assess impact on existing modules
* must preserve backward compatibility where possible

---

## Summary

This document establishes a **shared timing language** across all NODAL projects.

It enables:

* independent development
* safe composition
* predictable system behavior

Concrete timing values belong to modules and products — not the workspace.
