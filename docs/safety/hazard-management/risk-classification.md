---
title: Risk Classification
nav_order: 2
parent: Hazard Management
---

# Risk Classification

## Purpose

This document defines how identified hazards are **classified into risk levels** within the NODAL system. Risk classification provides a structured, repeatable, and auditable method to:

* Prioritize safety work
* Decide whether mitigation is required
* Determine the rigor of verification and validation
* Support acceptance and compliance decisions

Risk classification is a **core element of the Safety Case** and is mandatory for all hazards.

---

## Principles

Risk classification in NODAL follows these principles:

* **Systematic**: same criteria applied everywhere
* **Conservative**: uncertainty increases risk, never reduces it
* **Traceable**: every rating must be justified
* **Iterative**: classification may evolve as knowledge improves
* **Tool-supported**: implemented through GitHub Issues and Project fields

---

## Risk Model Overview

Each hazard is classified using three independent dimensions:

1. **Severity (S)** – consequence if the hazard occurs
2. **Probability (P)** – likelihood of occurrence
3. **Exposure (E)** – frequency or duration of system exposure

These dimensions are combined to derive a **Risk Class (RC)**.

> The model is inspired by functional safety standards (IEC 61508, ISO 26262) but adapted to NODAL’s modular and open architecture.

---

## Severity Levels (S)

Severity reflects the **worst credible consequence** of the hazard, assuming no mitigation.

| Level | Name         | Description                                |
| ----- | ------------ | ------------------------------------------ |
| S0    | No harm      | No safety impact; nuisance only            |
| S1    | Minor        | Reversible injury, minor property damage   |
| S2    | Major        | Serious injury, significant damage         |
| S3    | Critical     | Life-threatening injury, major system loss |
| S4    | Catastrophic | Fatality or multiple severe injuries       |

Rules:

* Always consider **credible worst-case**, not nominal behavior
* If multiple consequences exist, select the **highest severity**
* Severity is **independent of probability**

---

## Probability Levels (P)

Probability estimates the likelihood that the hazard will lead to the hazardous event.

| Level | Name       | Description                                 |
| ----- | ---------- | ------------------------------------------- |
| P0    | Incredible | Physically impossible                       |
| P1    | Rare       | Very unlikely, requires abnormal conditions |
| P2    | Occasional | Could occur during system lifetime          |
| P3    | Frequent   | Expected to occur repeatedly                |

Rules:

* Probability may be **qualitative** if data is unavailable
* Use historical data, simulations, or engineering judgment
* Uncertainty defaults to the **higher probability**

---

## Exposure Levels (E)

Exposure represents how often the system or user is exposed to the hazardous situation.

| Level | Name   | Description                     |
| ----- | ------ | ------------------------------- |
| E0    | None   | No exposure possible            |
| E1    | Low    | Rare or short exposure          |
| E2    | Medium | Regular exposure                |
| E3    | High   | Continuous or frequent exposure |

Rules:

* Exposure is context-dependent (operational profile matters)
* Changes in deployment may change exposure classification

---

## Risk Class Determination

The Risk Class (RC) is derived by combining S, P, and E using a **risk matrix** or predefined lookup table.

### Risk Classes

| RC  | Meaning      | Required Action                  |
| --- | ------------ | -------------------------------- |
| RC0 | Negligible   | No action required               |
| RC1 | Low          | Monitor, document                |
| RC2 | Medium       | Mitigation required              |
| RC3 | High         | Strong mitigation + verification |
| RC4 | Unacceptable | Design change mandatory          |

Rules:

* Any **S4** hazard is at least RC3
* Any hazard with high uncertainty cannot be RC0 or RC1
* RC4 hazards **cannot be accepted** as-is

---

## GitHub Project Mapping

Risk classification is implemented using GitHub Project fields:

### Required Fields

* **Hazard Severity** (Single select: S0–S4)
* **Hazard Probability** (Single select: P0–P3)
* **Hazard Exposure** (Single select: E0–E3)
* **Risk Class** (Single select: RC0–RC4)

### Rules

* Risk Class must be updated whenever S, P, or E changes
* Classification must be justified in the issue description or comments
* Automation may compute RC, but **human validation is mandatory**

---

## Ownership and Review

* Initial classification: **Hazard author**
* Review: **Safety reviewer or module owner**
* Approval: **Safety authority (role-based, not individual-based)**

Risk classification must be reviewed:

* At creation
* After any design change
* Before risk acceptance

---

## Evolution Over Time

Risk classification is expected to evolve:

* Early phases: conservative, assumption-heavy
* Development: refined using evidence and tests
* Verification: confirmed or escalated
* Deployment: reassessed based on operational context

All changes must remain **traceable**.

---

## Outputs

Each classified hazard produces:

* A documented Risk Class
* A mitigation requirement if RC ≥ RC2
* Input to:

  * Safety requirements
  * Lifecycle planning
  * Risk acceptance decisions

---

## Link to Next Step

Risk classification feeds directly into:

* **Risk acceptance** → `risk-acceptance.md`
* **Safety requirements definition** → `safety-requirements/`
* **Lifecycle rigor allocation** → `safety-lifecycle/`

---

> Risk classification does not reduce uncertainty — it exposes it.
> The goal is not to prove safety, but to manage risk explicitly and responsibly.
