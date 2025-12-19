---
title: System Architecture Overview
nav_order: 1
parent: Governance
---

# Safety Requirement Allocation Rules

## Purpose

This document defines how **Safety Requirements (SR)** are allocated across the  NODAL system architecture.

Allocation ensures that each safety requirement:

* is implemented at the correct architectural level
* has a clear owner
* avoids duplication or ambiguity
* remains traceable from system to module level

---

## Core Principles

1. **Allocate as high as possible, as low as necessary**
   Safety requirements should be allocated at the highest level capable of enforcing them.

2. **One owner per requirement**
   Every SR has exactly one implementation owner.

3. **Derivation is explicit**
   Module-level SRs derived from system SRs must reference their parent.

4. **No silent duplication**
   A safety requirement shall not be re-stated without justification.

5. **Allocation follows architecture, not convenience**
   Allocation decisions must reflect real control and responsibility boundaries.

---

## Allocation Levels

Safety requirements may be allocated to one of the following levels:

| Level              | Description                            |
| ------------------ | -------------------------------------- |
| System (Workspace) | Cross-module or global safety behavior |
| Module             | Local functional safety behavior       |
| Interface          | Interaction between modules            |
| Hardware           | Physical or electrical constraints     |
| Process            | Operational or procedural constraints  |

---

## System-Level Allocation (SR-SYS)

A Safety Requirement **shall** be allocated at system level if:

* it involves multiple modules
* it defines global safety states or transitions
* it concerns system startup, shutdown, or emergency behavior
* it governs fault handling coordination

**Examples:**

* Emergency stop propagation
* Global safe-state definition
* System-wide watchdog behavior

---

## Module-Level Allocation (SR-MOD)

A Safety Requirement **shall** be allocated at module level if:

* the module has full control over the behavior
* failure impact is localized
* mitigation does not require coordination

Module SRs may be:

* directly originating from a hazard
* derived from a system-level SR

---

## Derived Requirements

When a system-level SR cannot be implemented directly, it shall be **decomposed** into derived requirements.

Derived SRs must:

* reference the parent SR ID
* preserve the safety intent
* fully cover the parent requirement

**Example:**

* SR-SYS-CTRL-001 → SR-MOD-MOTION-012 + SR-MOD-COMM-007

---

## Interface Allocation (SR-INT)

Interface safety requirements apply when:

* safety depends on interaction correctness
* timing or data integrity is critical
* ownership is shared

SR-INTs must specify:

* participating modules
* interface assumptions
* failure handling behavior

---

## Hardware Allocation (SR-HW)

Hardware safety requirements apply when:

* mitigation depends on physical properties
* electrical or mechanical limits are involved
* software-only solutions are insufficient

Examples:

* power cutoff latency
* current limiting
* physical interlocks

---

## Process Allocation (SR-PROC)

Process safety requirements apply when:

* risk mitigation relies on procedures
* operational constraints are required
* human interaction is unavoidable

Examples:

* maintenance procedures
* calibration requirements
* deployment constraints

---

## Allocation Documentation

Each Safety Requirement must explicitly document:

* allocation level
* owner (role or team)
* derived-from (if applicable)

Allocation decisions must be recorded and traceable.

---

## GitHub Integration

Allocation is represented using:

* `Allocation Level` (single select)
* `Owner` (user or team)
* `Derived From` (issue reference)

GitHub Projects views must allow filtering by allocation level.

---

## Review and Change

Allocation must be reviewed when:

* architecture changes
* module responsibilities change
* a derived SR cannot fully satisfy the parent

Re-allocation requires re-verification.

---

## Relationship to Other Documents

* Safety requirement format → `requirement-format.md`
* Change management → `change-management.md`
* Architecture overview → `architecture/overview.md`

---

## Summary

Correct allocation ensures that safety requirements are:

* implementable
* enforceable
* traceable
* maintainable

Incorrect allocation is a safety risk in itself.
