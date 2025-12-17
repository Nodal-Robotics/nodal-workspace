# NODAL – Badge Usage Guidelines

## Purpose

This document defines the **official badge system for NODAL repositories**, based exclusively on **Shields.io** and verifiable GitHub data.

Badges are not decorative. They are **engineering signals**.

If a badge cannot be:

✅ objectively verified
✅ automatically updated
✅ consistently interpreted

➡️ **it must not exist**.

---

## Core Principles

1. **Automation first**
   Badges must update automatically (releases, CI, license, commits).

2. **Minimalism**
   Fewer badges, higher signal-to-noise ratio.

3. **Consistency across the ecosystem**
   The same badge means the same thing everywhere.

4. **No subjective claims**
   No “production ready”, “stable”, or “awesome” badges.

---

## Badge Categories

Badges are organized into **four layers**. Repositories must respect this order.

---

## 1. Identity & Scope Badges

These badges define **what the repository is**.

> Exactly **one** scope badge is allowed per repository.

### NODAL Module

```md
![NODAL Module](https://img.shields.io/badge/NODAL-Module-1f2a44)
```

### NODAL Workspace

```md
![NODAL Workspace](https://img.shields.io/badge/NODAL-Workspace-1f2a44)
```

### NODAL Hardware

```md
![NODAL Hardware](https://img.shields.io/badge/NODAL-Hardware-1f2a44)
```

---

## 2. Versioning & Activity Badges

These badges reflect **actual repository state**.

### Latest Release Version (SemVer)

Automatically updates on GitHub release/tag.

```md
![Version](https://img.shields.io/github/v/release/ORG/REPO)
```

---

### Last Commit

```md
![Last Commit](https://img.shields.io/github/last-commit/ORG/REPO)
```

---

## 3. Quality & Automation Badges

These badges reflect **objective quality gates**.

### CI / Build Status (GitHub Actions)

```md
![Build](https://github.com/ORG/REPO/actions/workflows/ci.yml/badge.svg)
```

> The workflow file **must exist**.

---

### Test Workflow (optional)

```md
![Tests](https://github.com/ORG/REPO/actions/workflows/tests.yml/badge.svg)
```

---

### Code Coverage (if enabled)

```md
![Coverage](https://img.shields.io/codecov/c/github/ORG/REPO)
```

---

## 4. Governance & Compliance Badges

### License (auto-detected)

```md
![License](https://img.shields.io/github/license/ORG/REPO)
```

Based on the repository `LICENSE` file.

---

### CLA Requirement (if applicable)

```md
![CLA](https://img.shields.io/badge/CLA-required-2f6f4e)
```

Used only if a CLA is explicitly enforced.

---

### Security Policy

```md
![Security](https://img.shields.io/badge/security-policy-green)
```

Used when `SECURITY.md` is present.

---

## Recommended Badge Sets

### NODAL Module Repository

```md
![NODAL Module](https://img.shields.io/badge/NODAL-Module-1f2a44)
![Version](https://img.shields.io/github/v/release/ORG/REPO)
![Build](https://github.com/ORG/REPO/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/github/license/ORG/REPO)
```

---

### NODAL Workspace Repository

```md
![NODAL Workspace](https://img.shields.io/badge/NODAL-Workspace-1f2a44)
![Version](https://img.shields.io/github/v/release/ORG/REPO)
![Integration](https://github.com/ORG/REPO/actions/workflows/integration.yml/badge.svg)
![License](https://img.shields.io/github/license/ORG/REPO)
```

---

### NODAL Hardware Repository

```md
![NODAL Hardware](https://img.shields.io/badge/NODAL-Hardware-1f2a44)
![License](https://img.shields.io/github/license/ORG/REPO)
```

---

## Forbidden Badges

The following badges are **explicitly forbidden**:

✅ "Production Ready"
✅ "Stable" / "Mature" (without formal criteria)
✅ "Maintained" (subjective)
✅ Vanity metrics (stars, forks)
✅ Emoji-based badges
✅ Manually edited version badges

---

## Badge Placement Rules

✅ Badges must be placed **at the very top** of the README
✅ Maximum **5 badges** per repository
✅ Identity badge must always come first

---

## Source of Truth

This document is authoritative.

Any deviation must be:

✅ explicitly justified
✅ documented
✅ approved at workspace level

---

**NODAL documentation is an interface.**
Badges are part of that interface.
