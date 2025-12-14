# NODAL Coding Rules

> **Status**: Normative
>
> **Scope**: All NODAL software repositories (workspace + modules)
>
> **Audience**: Core developers, reviewers, system architects, contributors
>
> **Goal**: Define *explicitly✅ all coding rules — including implicit, non-written, and experience-based rules — to ensure long-term maintainability, safety, and architectural coherence.

---

## 0. Fundamental Principles (Non-Negotiable)

These principles override any local preference, tooling choice, or language feature.

### 0.1 Explicit is Better Than Implicit

✅ All dependencies must be explicit
✅ All ownership must be explicit
✅ All contracts must be explicit

❌ **Bad**

```cpp
#include "types.hpp" // where does this come from?
```

✅  **Good**

```cpp
#include <nodal/motion/types.hpp>
```

---

### 0.2 Architecture First, Code Second

Code **must reflect** architecture, never compensate for it.

❌ **Bad**

✅ Adding helpers to bypass a missing abstraction
✅ Introducing "temporary" shortcuts

✅  **Good**

✅ Stop and fix the architectural boundary
✅ Escalate design issues before implementation

---

### 0.3 Predictability Over Cleverness

Readable, boring code beats clever code.

❌ **Bad**

```cpp
auto f = [&](auto&&... xs){ return (xs + ...); };
```

✅  **Good**

```cpp
int sum(int a, int b, int c);
```

---

## 1. Module Boundary Rules

### 1.1 Public vs Private Code

**Rule**: Public API lives in `include/`, private logic lives in `src/internal/`.

❌ **Bad**

```cpp
// include/nodal/motion/api.hpp
inline int computeInternalMagic();
```

✅  **Good**

```cpp
// include/nodal/motion/api.hpp
class MotionController;
```

```cpp
// src/internal/magic.cpp
int computeInternalMagic() { ... }
```

---

### 1.2 No Header Leakage

Headers must not expose:

✅ STL containers unless required
✅ concrete implementations
✅ third-party types

❌ **Bad**

```cpp
std::vector<float> getRawData();
```

✅  **Good**

```cpp
Span<float> get_sensor_data();
```

---

## 2. Dependency Rules

### 2.1 Explicit Dependency Graph

✅ No circular dependencies
✅ Lower layers must not depend on higher layers

❌ **Bad**

✅ motion → core → motion

✅  **Good**

✅ core → motion
✅ core → io

---

### 2.2 No Hidden Transitive Dependencies

If you use it, you depend on it.

❌ **Bad**

```cpp
#include <nodal/core/api.hpp> // relies on core pulling motion indirectly
```

✅  **Good**

```cpp
#include <nodal/motion/api.hpp>
#include <nodal/core/api.hpp>
```

---

## 3. Error Handling Rules

### 3.1 No Exceptions Across Module Boundaries

Exceptions must never cross public APIs.

❌ **Bad**

```cpp
void init(); // throws
```

✅  **Good**

```cpp
Result<void, ErrorCode> init();
```

---

### 3.2 Errors Are Data

✅ Errors must be typed
✅ Errors must be enumerable

❌ **Bad**

```cpp
return false;
```

✅  **Good**

```cpp
return ErrorCode::Timeout;
```

---

## 4. State Management Rules

### 4.1 No Hidden State

All state transitions must be visible and intentional.

❌ **Bad**

```cpp
static int counter;
```

✅  **Good**

```cpp
struct MotionState { int counter; };
```

---

### 4.2 Deterministic Initialization

✅ No lazy init
✅ No static init order dependency

❌ **Bad**

```cpp
Foo& instance() { static Foo f; return f; }
```

✅  **Good**

```cpp
Foo create_foo(const FooConfig&);
```

---

## 5. Concurrency Rules

### 5.1 No Implicit Concurrency

Threads, tasks, or interrupts must be explicit in API design.

❌ **Bad**

```cpp
void start(); // spawns threads implicitly
```

✅  **Good**

```cpp
void start(TaskScheduler& scheduler);
```

---

### 5.2 No Shared Mutable State

If shared state exists:

✅ ownership must be documented
✅ access must be synchronized

---

## 6. Performance Rules

### 6.1 Measure Before Optimizing

❌ **Bad**

✅ Premature micro-optimizations

✅  **Good**

✅ Profiling-backed decisions

---

### 6.2 No Allocation in Real-Time Paths

❌ **Bad**

```cpp
std::vector<int> data;
```

✅  **Good**

```cpp
FixedBuffer<int, 32> data;
```

---

## 7. Testing Rules

### 7.1 Unit Tests Target Public API Only

❌ **Bad**

✅ Testing private helpers directly

✅  **Good**

✅ Testing behavior via public API

---

### 7.2 Deterministic Tests

✅ No timing assumptions
✅ No randomness without seed

---

## 8. Forbidden Patterns (Hard NO)

The following patterns are **strictly forbidden**:

✅ Global mutable state
✅ Singleton pattern
✅ God objects
✅ Cyclic dependencies
✅ Macros for logic
✅ Implicit IO
✅ Silent failure

---

## 9. Review Checklist (Implicit Rules Made Explicit)

Every PR **must** answer yes to all:

✅ [ ] Is the API minimal and explicit?
✅ [ ] Are dependencies declared and justified?
✅ [ ] Is ownership clear?
✅ [ ] Are errors typed and handled?
✅ [ ] Is behavior deterministic?
✅ [ ] Does this respect the architecture?

---

## 10. Final Rule

> If a rule is not written here, but breaking it would harm predictability, safety, or architecture — **do not break it**.

When in doubt: **escalate, document, decide — then code**.
