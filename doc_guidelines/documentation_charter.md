# 📘 NODAL Documentation Charter

## 1. Purpose of This Charter

This document defines the **official documentation standards** for the **NODAL framework** and the Axion Robotics ecosystem.

Its purpose is to ensure that all NODAL documentation is:

✅ clear and easy to read
✅ consistent across all repositories
✅ sustainable over the long term (5–15 years)
✅ understandable by diverse technical profiles

Within NODAL, documentation is considered **a core part of the system architecture**, just like software and hardware.

---

## 2. Fundamental Principles

### 2.1 System-Oriented Documentation

NODAL documentation describes **systems**, not just code.

Every document should implicitly answer at least one of the following questions:

✅ What is the role of this component within the global system?
✅ What are its responsibilities and boundaries?
✅ How does it interact with other modules?

### 2.2 Clarity Over Exhaustiveness

✅ A short and clear document is preferred over a long and confusing one
✅ Advanced details must be separated into dedicated files
✅ A first read should be possible in less than 5 minutes

### 2.3 Industrial Readability

Documentation must be:

✅ sober
✅ factual
✅ non-marketing

The tone is **professional, neutral, and technical**.

---

## 3. Scope

This charter applies to:

✅ all README.md files
✅ all documents under `/docs`
✅ software documentation
✅ hardware documentation
✅ diagrams and schematics

---

## 4. Documentation Hierarchy

### 4.1 Level 1 — Organization

Scope: global vision

✅ GitHub organization README
✅ NODAL framework presentation
✅ philosophy and core principles

Owner: Axion Robotics

---

### 4.2 Level 2 — Governance / Meta-Repository

Scope: global rules and architecture

Typically: `nodal-workspace`

Contains:

✅ global architecture
✅ conventions and standards
✅ documentation charter
✅ contribution rules
✅ licenses and CLA

---

### 4.3 Level 3 — Module Repositories

Scope: a single functional component

Each module repository must contain:

✅ a short and clear README
✅ optional technical documentation

A module repository must **never** document the global vision.

---

### 4.4 Level 4 — Detailed Technical Documentation

Scope: implementation details

Typical files:

✅ `/docs/architecture.md`
✅ `/docs/api.md`
✅ `/docs/interfaces.md`

These documents are optional but recommended for critical modules.

---

## 5. README Rules

### 5.1 Mandatory Structure

Every NODAL README **must** include:

1. Title and tagline
2. Overview
3. Role within the NODAL ecosystem
4. Integration
5. Versioning
6. Contributing
7. License

Unnecessary sections must not be added.

---

### 5.2 Tone and Style

✅ short sentences
✅ precise vocabulary
✅ limited use of emojis
✅ no unnecessary jargon

Terminology must be consistent across the entire ecosystem.

---

## 6. Software Documentation

### 6.1 Objectives

Software documentation must explain:

✅ the responsibilities of the module
✅ its public interfaces
✅ its constraints

It must **not** attempt to explain every line of code.

---

### 6.2 APIs and Interfaces

Every public interface must be:

✅ explicitly documented
✅ stable
✅ versioned

Interface changes must be documented in the changelog.

---

## 7. Hardware Documentation

### 7.1 Philosophy

Hardware is treated as a **system component**, at the same level as software.

Hardware documentation must cover:

✅ the role of the board
✅ its interfaces
✅ its constraints

---

### 7.2 Minimum Content

A hardware repository must include:

✅ a README
✅ a functional block diagram
✅ source files (schematics, PCB)
✅ a clear hardware license

---

## 8. Diagrams and Schematics

### 8.1 General Rules

✅ simple diagrams
✅ mandatory legends
✅ no decorative diagrams

Diagrams must explain, not impress.

---

## 9. Documentation Evolution

Any major documentation change must:

✅ be reviewed
✅ remain consistent with this charter

The charter itself is versioned.

---

## 10. Conclusion

NODAL documentation is an **engineering tool**.

It enables:

✅ knowledge transfer
✅ collaboration
✅ long-term sustainability

All contributions must respect this spirit.

---

© Axion Robotics — NODAL Framework
