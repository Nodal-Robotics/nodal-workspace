# NODAL Diagram Guidelines

> **Status**: Normative
>
> **Scope**: All diagrams used in NODAL documentation (workspace and modules)
>
> **Audience**: Architects, system engineers, developers, reviewers
>
> **Goal**: Ensure all diagrams are readable, unambiguous, and architecturally consistent.

---

## 0. Core Principles

### 0.1 A Diagram Is a Contract

A diagram is not illustrative art. It is a **technical artifact**.

If a diagram can be interpreted in multiple ways, it is invalid.

---

### 0.2 Diagrams Must Match Reality

✅ No aspirational diagrams
✅ No outdated diagrams
✅ No "simplified" diagrams that lie

❌ **Bad**

> Diagram represents the intended design, not the actual one.

✅  **Good**

> Diagram represents the current system as implemented.

---

## 1. Diagram Types and Their Purpose

### 1.1 Architecture Diagrams

**Purpose**:

✅ Show module boundaries
✅ Show allowed dependencies
✅ Show responsibility split

Must include:

✅ module names
✅ dependency direction
✅ forbidden paths (if relevant)

---

### 1.2 Sequence Diagrams

**Purpose**:

✅ Show interaction order
✅ Show ownership of actions
✅ Show blocking vs non-blocking behavior

Must include:

✅ caller / callee
✅ synchronous vs asynchronous calls
✅ error paths

---

### 1.3 Timing Diagrams

**Purpose**:

✅ Show temporal constraints
✅ Show deadlines
✅ Show WCET assumptions

Must include:

✅ time axis
✅ execution windows
✅ deadlines

---

### 1.4 State Diagrams

**Purpose**:

✅ Show valid states
✅ Show transitions
✅ Show forbidden transitions

Must include:

✅ initial state
✅ terminal states (if any)
✅ error states

---

## 2. Notation Rules

### 2.1 UML Usage

✅ Use UML where applicable
✅ Do not mix UML with ad-hoc symbols

❌ **Bad**

> Custom arrows with no legend

---

### 2.2 Arrows

✅ Arrow direction = dependency or call direction
✅ Arrow meaning must be consistent

❌ **Bad**

> Same arrow meaning two different things

---

## 3. Naming in Diagrams

### 3.1 Names Must Match Code

All names used in diagrams must:

✅ match repository names
✅ match module names
✅ match API names

❌ **Bad**

> MotionEngine (code uses MotionController)

---

### 3.2 No Abbreviations

❌ **Bad**

> Ctrl, Mgr, IO

✅  **Good**

> MotionController, CoreSupervisor

---

## 4. Level of Detail

### 4.1 One Diagram = One Question

A diagram must answer **one** question.

❌ **Bad**

> Architecture + timing + state in one diagram

---

### 4.2 Layered Documentation

✅ High-level diagrams in workspace
✅ Detailed diagrams in module docs

---

## 5. Visual Rules

### 5.1 Colors

✅ Colors must have meaning
✅ Same color = same concept

Example:

✅ blue: software module
✅ red: forbidden dependency

---

### 5.2 Text

✅ Horizontal text only
✅ No overlapping labels

---

## 6. Tools

Recommended tools:

✅ PlantUML
✅ Mermaid

Rules:

✅ diagrams must be versioned as text when possible
✅ no binary-only sources without source files

---

## 7. Forbidden Diagram Patterns

The following are forbidden:

✅ diagrams without legend
✅ diagrams without title
✅ diagrams without scope
✅ screenshots of whiteboards

---

## 8. Review Checklist

✅ [ ] Diagram answers a single question
✅ [ ] Notation is consistent
✅ [ ] Names match code
✅ [ ] No ambiguity
✅ [ ] Diagram is up to date

---

## Final Rule

> If a diagram requires verbal explanation to be understood, it is incomplete.

Make diagrams self-sufficient.
