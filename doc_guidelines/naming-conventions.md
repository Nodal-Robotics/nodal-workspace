# NODAL Naming Convention

> **Status**: Normative
>
> **Scope**: All NODAL repositories (workspace + modules)
>
> **Audience**: Developers, reviewers, architects
>
> **Goal**: Define a single, explicit, and enforceable naming system across the entire NODAL ecosystem.

---

## 0. Core Principles

### 0.1 Names Are Part of the Architecture

A name is not cosmetic. A name encodes:

✅ responsibility
✅ ownership
✅ abstraction level
✅ lifetime

If a name is wrong, the architecture is already damaged.

---

### 0.2 Explicit > Short

❌ **Bad**

```cpp
ctx, mgr, util, data
```

✅  **Good**

```cpp
motion_context
scheduler
sensor_data
```

---

### 0.3 One Concept = One Name

Never use multiple names for the same concept.

❌ **Bad**

✅ controller / manager / handler (same role)

✅  **Good**

✅ controller (and only controller)

---

## 1. Repository Naming

### 1.1 Workspace

```
nodal-workspace
```

✅ singular
✅ lowercase
✅ hyphen-separated

---

### 1.2 Module Repositories

```
nodal-core
nodal-motion
nodal-io
```

Rules:

✅ prefix `nodal-` mandatory
✅ one responsibility only
✅ no version in repo name

❌ **Bad**

```
nodal-motion-v2
motion-module
```

---

## 2. Directory Naming

### 2.1 Standard Directories

| Directory     | Rule                       |
| ------------- | -------------------------- |
| include/      | public headers only        |
| src/          | implementation only        |
| src/internal/ | strictly private logic     |
| tests/unit/   | unit tests                 |
| docs/         | module-local documentation |

❌ **Bad**

```
src/public/
```

---

## 3. File Naming

### 3.1 General Rules

✅ lowercase
✅ snake_case
✅ descriptive

❌ **Bad**

```
API.hpp
motionApi.h
```

✅  **Good**

```
api.hpp
types.hpp
config.hpp
```

---

### 3.2 Source Files

Implementation mirrors API intent.

❌ **Bad**

```
magic.cpp
helpers.cpp
```

✅  **Good**

```
api.cpp
trajectory_generator.cpp
```

---

## 4. Namespace Naming

### 4.1 Global Namespace

```cpp
namespace nodal::motion
```

Rules:

✅ always start with `nodal`
✅ module name as second level

❌ **Bad**

```cpp
namespace motion
```

---

### 4.2 Internal Namespaces

```cpp
namespace nodal::motion::internal
```

✅ never exposed in headers
✅ never used outside module

---

## 5. Type Naming

### 5.1 Classes & Structs

```cpp
class MotionController;
struct MotionState;
```

Rules:

✅ PascalCase
✅ nouns for data
✅ controller/engine/manager only if justified

❌ **Bad**

```cpp
class DoStuff;
class Utils;
```

---

### 5.2 Enums

```cpp
enum class ErrorCode {
  ok,
  timeout,
  invalid_config
};
```

Rules:

✅ enum class only
✅ lowercase values
✅ semantic meaning

---

## 6. Function Naming

### 6.1 Public API

```cpp
Result<void, ErrorCode> start();
MotionState get_state() const;
```

Rules:

✅ snake_case
✅ verbs for actions
✅ no abbreviations

❌ **Bad**

```cpp
initSys();
getSt();
```

---

### 6.2 Internal Functions

Same rules, less restrictive — but still explicit.

---

## 7. Variable Naming

### 7.1 General

```cpp
int retry_count;
float target_velocity;
```

❌ **Bad**

```cpp
int i;
float v;
```

(loop indices excepted)

---

### 7.2 Constants

```cpp
constexpr int max_retry_count = 3;
```

✅ lowercase
✅ descriptive

---

## 8. Error & Result Naming

```cpp
Result<T, ErrorCode>
```

✅ ErrorCode mandatory
✅ no bool-based APIs

❌ **Bad**

```cpp
bool init();
```

---

## 9. Test Naming

### 9.1 Test Files

```
motion_controller_test.cpp
```

### 9.2 Test Cases

```cpp
TEST(MotionController, FailsOnInvalidConfig)
```

---

## 10. Forbidden Names (Hard NO)

The following are forbidden everywhere:

✅ util
✅ helper
✅ misc
✅ data
✅ stuff
✅ tmp

If you need them, your abstraction is wrong.

---

## 11. Review Checklist

✅ [ ] Names reflect responsibility
✅ [ ] No abbreviations
✅ [ ] No generic names
✅ [ ] Consistent with existing modules
✅ [ ] Clear for a new engineer

---

## Final Rule

> If you hesitate when naming something, **you have not understood its responsibility yet**.

Stop. Clarify. Then name.
