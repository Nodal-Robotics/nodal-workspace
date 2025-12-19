# Build Tooling

This document defines the requirements for build systems used in all NODAL repositories.

---

## 🎯 Objectives

Build tooling must guarantee:

- reproducibility
- traceability of artifacts
- deterministic outputs
- alignment between local and CI builds

---

## 🔒 Mandatory Rules

- Builds must be fully automated
- No manual build steps are allowed for release artifacts
- Build configuration must be version-controlled
- Toolchain versions must be explicit

---

## 🧠 Determinism

A build is considered deterministic if:

- same inputs → same outputs
- independent of host machine state
- independent of execution order

Non-deterministic builds are **forbidden** for safety-related artifacts.

---

## 🛡️ Safety Impact

Build tooling is safety-relevant when it affects:

- compiler flags
- code generation
- optimization levels
- feature toggles
- hardware abstraction

Any change to build tooling **requires impact analysis**.

---

## 📌 Evidence

Build logs and artifacts are considered valid evidence if:

- versioned
- traceable to a commit
- reproducible
