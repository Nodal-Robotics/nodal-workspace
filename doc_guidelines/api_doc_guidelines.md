# NODAL – API Documentation Guidelines

## Purpose

This document defines **how public APIs must be documented** across the NODAL ecosystem.

An API without precise documentation is considered **incomplete**.

This guide applies to:

✅ C++ public headers (`include/`)
✅ future Rust public APIs
✅ any interface exposed outside a module

---

## Scope of API Documentation

Only **public interfaces** are documented here:

✅ public classes
✅ public functions
✅ public types
✅ configuration parameters

Internal implementation details are explicitly excluded.

---

## API Boundary Rule

> If a symbol is accessible from outside the module, it **must** be documented.

Conversely:

✅ internal helpers
✅ private classes
✅ implementation details

must not appear in API documentation.

---

## Required Information per API Element

Each public API element must document:

1. **Purpose**
   What this element does.

2. **Inputs**
   Parameters, units, valid ranges.

3. **Outputs**
   Return values or effects.

4. **Constraints**
   Timing, determinism, threading assumptions.

5. **Error Handling**
   Possible failures and how they are reported.

6. **Ownership & Lifetime** (if applicable)

---

## Function Documentation Template

```cpp
/// @brief Short, explicit description.
///
/// @param[in]  input   Description, units, constraints
/// @param[out] output  Description
///
/// @return Description of return value
///
/// @note Timing, determinism, or threading assumptions
```

---

## Class Documentation Rules

A public class documentation must state:

✅ responsibility
✅ lifecycle
✅ thread-safety guarantees
✅ ownership model

Avoid describing implementation strategy.

---

## Error Semantics

Errors must be:

✅ explicit
✅ deterministic
✅ documented

Document whether errors are:

✅ returned
✅ thrown
✅ reported asynchronously

Silence is not acceptable.

---

## Configuration Parameters

Public configuration options must specify:

✅ default value
✅ valid range
✅ effect on behavior
✅ whether change is allowed at runtime

---

## Examples

Examples must be:

✅ minimal
✅ correct
✅ aligned with the public API

Examples must not expose internal details.

---

## Forbidden Practices

✅ Documenting internal headers
✅ Explaining implementation algorithms
✅ Copying global architectural rules
✅ Ambiguous wording

---

## Final Rule

> API documentation defines the contract.

Breaking the contract without updating documentation is a breaking change.

---

This document is mandatory for all NODAL modules exposing a public API.
