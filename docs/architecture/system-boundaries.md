---

title: System Boundaries
nav_order: 1
parent: Architecture
permalink: /architecture/system-boundaries/
---

# System Boundaries

## 1. Purpose

This document defines the **boundaries of the NODAL system**.

It clarifies:

* what is considered part of the system
* what is explicitly outside the system
* where responsibilities start and end

Clear system boundaries are essential for:

* architectural consistency
* safety scope definition
* hazard responsibility allocation
* certification and liability analysis

This document is **normative**.

---

## 2. Definition of the System

The **NODAL system** is defined as:

> A modular robotics system framework composed of independent functional modules, orchestrated and governed by the NODAL workspace.

The system includes:

* the NODAL workspace (architecture, lifecycle, governance)
* all NODAL-compliant software modules
* reference hardware interfaces when explicitly specified
* tooling required to build, test, and integrate the system

---

## 3. In-Scope Elements

The following elements are considered **inside the system boundary**.

### 3.1 Software

* NODAL software modules
* inter-module interfaces and contracts
* configuration and integration mechanisms
* build and verification tooling defined by the workspace

### 3.2 System Configuration

* module composition and activation
* version compatibility rules
* system-level parameters affecting behavior

### 3.3 Safety-Relevant Artifacts

* hazards identified at system level
* safety requirements derived from those hazards
* verification evidence produced within the defined lifecycle

---

## 4. Out-of-Scope Elements

The following elements are **explicitly outside the system boundary**.

### 4.1 Physical Environment

* the operational environment in which the robot is deployed
* external actors (humans, other machines)
* site-specific safety measures not controlled by NODAL

### 4.2 External Systems

* third-party hardware not specified as reference
* external software systems interacting via defined interfaces
* cloud or infrastructure services unless explicitly included

### 4.3 Usage and Operational Procedures

* end-user operational procedures
* installation-specific configurations
* local safety policies beyond system assumptions

---

## 5. Boundary Interfaces

All interactions across the system boundary must:

* occur through explicit interfaces
* be documented and versioned
* define assumptions and limitations

Undocumented or implicit boundary crossings are **not permitted**.

---

## 6. Responsibility Allocation

Responsibilities are allocated as follows:

* **NODAL system**: behavior and safety within defined boundaries
* **Integrators**: correct configuration and deployment
* **Operators**: safe operation within documented assumptions

This allocation is used for safety and compliance reasoning.

---

## 7. Impact on Safety Scope

The system boundary directly defines:

* the scope of hazard identification
* the applicability of safety requirements
* the limits of safety claims

Hazards originating outside the boundary may be considered only
in terms of their **interaction with the system**.

---

## 8. Boundary Changes

Changes to system boundaries:

* are exceptional
* require an ADR
* must assess impact on safety, lifecycle, and compliance

Boundary changes may invalidate existing safety assumptions
and require re-evaluation.

---

## 9. Related Documents

* Architectural overview: `overview.md`
* Architectural assumptions: `assumptions.md`
* Safety scope and assumptions: `../safety/safety-scope-and-assumptions.md`
* Architecture Decision Records: `../governance/adr/`

---

> System boundaries define responsibility.
> Responsibility defines safety.
