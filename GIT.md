# NODAL Git Rules & Workflow

> **Status**: Normative
>
> **Scope**: All NODAL repositories (workspace, modules, tooling)
>
> **Audience**: All contributors
>
> **Goal**: Define a strict, predictable, and auditable Git workflow for NODAL.

---

## 0. Core Principles

### 0.1 Git Is a System Interface

Git history is not a log of activity.
It is a **technical artifact** used to:

✅ understand intent
✅ review changes
✅ debug regressions
✅ audit decisions

---

### 0.2 Predictability Over Flexibility

A boring Git workflow is a good Git workflow.

---

## 1. Repository Roles

### 1.1 nodal-workspace

✅ System-level repository
✅ Integration, E2E tests, specs
✅ Source of truth for standards

### 1.2 nodal-<module>

✅ Single responsibility
✅ No cross-module history coupling

---

## 2. Branching Model

### 2.1 Main Branches

```
main
```

Rules:

✅ always releasable
✅ protected
✅ no direct commits

---

### 2.2 Feature Branches

```
feature/<short-description>
```

❌ **Bad**

```
fix
new-stuff
```

✅  **Good**

```
feature/motion-timeout-handling
```

---

### 2.3 Bugfix Branches

```
fix/<short-description>
```

---

## 3. Commit Rules

### 3.1 Atomic Commits

Each commit must:

✅ compile
✅ pass tests
✅ represent a single logical change

❌ **Bad**

> WIP

---

### 3.2 Commit Message Format

```
<type>: <short summary>

<optional body>

Why:
<explanation>

What:
<what was changed>

Impact:
<impact on the system, safety, or certification>

Safety:
- SIL target: <SIL1|SIL2|SIL3|N/A>
- Affected functions: <list or none>
- Hazard impact: <none|low|medium|high>

BREAKING CHANGE:
<if applicable>


Types:

feat

fix

refactor

docs

test

chore

safety

build

ci

revert
```

### 3.3 Gitmoji

All commits must use Gitmoji to indicate the type of change. This improves clarity, traceability, and consistency across all commits.

| Emoji    | Type | Description |
| -------------------------- | -------- | ------------
| 🎉 (:sparkles:)            | feat     | New feature
| 🐛 (:bug:)	             | fix	    | Bug fix
| 🔧 (:recycle:)	         | refactor | Code refactor, no change in feature
| 📝 (:memo:)                | docs	    | Documentation changes
| 🦺  (:safety_vest:)         | safety	 | Safety-related changes
| ✅  (:white_check_mark:)    | test     | Add, update or pass test
| 🧪  (:test_tube:)	          | test     | Add a failing test
| 👷 (:construction_worker:) | build	| Changes to the build system
| 🚀 (:rocket:)	             | chore	| Maintenance tasks
| ⏪️  (:rewind:)             | revert	| Reverts a previous commit

**Example:**
```
🎉 feat(architecture): add initial system overview

Why:
Document the system architecture for future review.

What:
Added system overview, hardware profile, timing budget.

Impact:
No impact on runtime behavior.

Safety:
- SIL target: N/A
- Affected functions: none
- Hazard impact: none
```

---

## 4. Pull Requests

### 4.1 Mandatory PRs

✅ No direct push to main
✅ All changes via PR and review

PR must pass automated checks (e.g., linters, tests)

Safety checks on all commits are mandatory
---

### 4.2 PR Content

PRs must include:

✅ Motivation behind the change
✅ Summary of the changes
✅ Impact analysis (including safety impact if relevant)
✅ Documentation impact (if relevant)
---

## 5. Versioning & Releases

### 5.1 Semantic Versioning

✅ MAJOR: breaking change
✅ MINOR: backward-compatible feature
✅ PATCH: bug fix

Tags:

```
vX.Y.Z
```

---

## 6. Forbidden Git Patterns

✅ Force push on main
✅ Squash without review
✅ History rewriting after release
✅ Mixing refactor and feature commits

---

## Final Rule

> If a change cannot be explained clearly in Git history, it does not belong in NODAL.

> Safety-related commits must follow the structure defined in the commit message format, and the section Safety: must always be populated, even if SIL is N/A. This ensures clarity and traceability for all safety-related decisions, which is crucial for compliance with standards like IEC 61508.