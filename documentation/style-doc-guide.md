# NODAL – Documentation Style Guide

## Purpose

This guide defines **how to write documentation** in the NODAL ecosystem.

It is practical, prescriptive, and intended for daily use.

---

## Language

✅ English only
✅ Technical, neutral tone
✅ No marketing language
✅ No emojis
✅ No buzzwords

Write for engineers.

---

## Document Structure

Every document should follow this structure when applicable:

1. Title
2. Purpose
3. Scope / Audience
4. Main content
5. Constraints / Assumptions

Avoid long introductions.

---

## Titles & Headings

✅ Use sentence case for headings
✅ One idea per section
✅ Avoid deep nesting (max 3 levels)

Example:

```md
## Timing Constraints
```

---

## Writing Rules

✅ Short sentences
✅ Prefer lists over paragraphs
✅ Prefer tables over prose
✅ Avoid ambiguity
✅ State non‑goals explicitly

Bad:

> This module tries to be efficient.

Good:

> This module guarantees deterministic execution under the timing budget defined in `TIMING_BUDGET.md`.

---

## Markdown Conventions

✅ Use `code blocks` for identifiers and paths
✅ Use tables for comparisons
✅ Avoid inline HTML

---

## References

✅ Prefer links over duplication
✅ Reference authoritative documents
✅ Never copy global rules locally

---

## Diagrams

✅ Diagrams must reflect reality
✅ No decorative diagrams
✅ Tools must be reproducible

(See `DIAGRAMS_GUIDELINES.md`)

---

## Examples

Examples must be:

✅ minimal
✅ correct
✅ compilable when applicable

---

## Versioning Documentation

✅ Documentation evolves with the system
✅ Breaking changes must be explicit
✅ Outdated documentation is considered incorrect

---

## Final Rule

> If a document cannot be understood without prior context, it must be rewritten.

---

This style guide is mandatory for all NODAL documentation.
