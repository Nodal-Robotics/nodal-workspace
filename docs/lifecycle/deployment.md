# Deployment Phase

## Status

Normative — Workspace level

## Purpose

The Deployment phase defines **how verified artifacts are released, configured, and accepted for operational use**.

Deployment answers the question:

> *Is the verified system ready to be used in its intended context?*

This phase closes the lifecycle loop and establishes a clear boundary between **engineering work** and **operational use**.

---

## Scope

The Deployment phase applies to:

* software releases
* hardware revisions
* system configurations
* safety acceptance decisions
* delivery artifacts

Out of scope:

* feature development
* requirement changes
* exploratory testing

---

## Core Principles

### Verification Is a Prerequisite

Only **verified artifacts** may be deployed.

Deployment shall not:

* compensate for missing verification
* bypass unresolved verification findings
* introduce unverified changes

If verification is incomplete, deployment is prohibited.

---

### Configuration Is Part of the Product

A deployed system is not only code or hardware.

Deployment includes:

* configuration parameters
* build options
* hardware variants
* enabled / disabled features

All deployed configurations shall be:

* versioned
* documented
* reproducible

---

### Explicit Acceptance

Deployment implies an **explicit acceptance decision**.

Acceptance shall:

* reference verification evidence
* identify residual risks
* state known limitations

Implicit or informal acceptance is not allowed.

---

## Deployment Activities

### 1. Release Preparation

Before deployment:

* all verification activities shall be complete
* release scope shall be frozen
* version identifiers shall be assigned

Release notes shall summarize:

* included changes
* addressed issues
* known limitations
  n---

### 2. Configuration Definition

Deployment configurations shall specify:

* target environment
* enabled modules
* safety-relevant parameters

Configuration changes after deployment require controlled updates.

---

### 3. Acceptance Review

An acceptance review shall confirm:

* verification completeness
* safety requirements satisfaction
* traceability closure

Acceptance decisions shall be recorded.

---

### 4. Delivery

Delivered artifacts may include:

* binaries or firmware
* hardware documentation
* configuration files
* user or integrator documentation

---

## Artifacts

The Deployment phase produces:

| Artifact          | Description            |
| ----------------- | ---------------------- |
| Release package   | Deployable system      |
| Configuration set | Operational parameters |
| Release notes     | Scope and limitations  |
| Acceptance record | Deployment decision    |

---

## Relation to GitHub Projects

In GitHub Projects, Deployment work is represented by:

* lifecycle = Deployment
* type = release / acceptance
* linked releases or tags

A Deployment item is not complete until acceptance is recorded.

---

## Exit Criteria

The Deployment phase is complete when:

* release artifacts are published
* configuration is documented
* acceptance decision is recorded
* deployment scope is traceable

---

## Feedback to Lifecycle

Deployment may reveal:

* operational constraints
* unexpected behavior
* improvement opportunities

Such feedback shall generate new Analysis items.

---

## Relation to Other Phases

* Follows: [`verification.md`](./verification.md)
* Informs: [`analysis.md`](./analysis.md)

---

## Summary

The Deployment phase transforms **verified artifacts** into **accepted operational systems**.

It provides a clear, auditable boundary between engineering and use, enabling controlled evolution and safety accountability.
