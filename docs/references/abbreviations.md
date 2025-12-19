# Abbreviations & Acronyms

## Purpose

This document lists all **standard abbreviations and acronyms** used throughout the NODAL ecosystem.

Using consistent abbreviations ensures:  

* clarity in technical communication
* reduced ambiguity in specifications
* efficient documentation
* consistent cross-references

---

## System & Architecture

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **NODAL**    | Nodular ECU-based Design for Autonomous Locomotion | Framework name |
| **ADR**      | Architecture Decision Record       | Decision documentation       |
| **API**      | Application Programming Interface  | Module interfaces            |
| **ECU**      | Electronic Control Unit            | Automotive inspiration       |
| **DAG**      | Directed Acyclic Graph             | Dependency structure         |

---

## Lifecycle & Phases

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **Analysis** | A                                  | Lifecycle phase              |
| **Dev**      | Development                        | Lifecycle phase              |
| **Verif**    | Verification                       | Lifecycle phase              |
| **Depl**     | Deployment                         | Lifecycle phase              |

---

## Safety & Risk

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **SR**       | Safety Requirement                 | Safety artifact              |
| **SR-SYS**   | System-level Safety Requirement    | Safety requirement type      |
| **SR-MOD**   | Module-level Safety Requirement    | Safety requirement type      |
| **SR-INT**   | Interface Safety Requirement       | Safety requirement type      |
| **SR-PROC**  | Procedural Safety Requirement      | Safety requirement type      |
| **RC**       | Risk Class                         | Risk classification          |
| **RC0**      | Risk Class 0 (Negligible)          | Risk level                   |
| **RC1**      | Risk Class 1 (Low)                 | Risk level                   |
| **RC2**      | Risk Class 2 (Medium)              | Risk level                   |
| **RC3**      | Risk Class 3 (High)                | Risk level                   |
| **RC4**      | Risk Class 4 (Unacceptable)        | Risk level                   |
| **S**        | Severity                           | Risk component               |
| **P**        | Probability                        | Risk component               |
| **E**        | Exposure                           | Risk component               |

---

## Timing & Real-Time

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **HRT**      | Hard Real-Time                     | Timing category              |
| **FRT**      | Firm Real-Time                     | Timing category              |
| **SRT**      | Soft Real-Time                     | Timing category              |
| **WCET**     | Worst-Case Execution Time         | Performance metric            |
| **ms**       | milliseconds                       | Time unit                    |
| **μs**       | microseconds                       | Time unit                    |

---

## Verification & Evidence

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **CI**       | Continuous Integration             | Automation                   |
| **PR**       | Pull Request                       | Code review mechanism        |

---

## Standards & Compliance

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **IEC 61508** | Functional Safety Standard         | Safety standard              |
| **ISO 26262** | Automotive Functional Safety       | Safety standard              |
| **MISRA C**  | Motor Industry Software Reliability Association C | Coding standard |
| **V-Model**  | V-shaped Development Model         | Lifecycle inspiration        |

---

## Organizational

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **SIL**      | Safety Integrity Level             | Safety assurance             |
| **FMEA**     | Failure Mode and Effects Analysis  | Hazard analysis              |
| **RMS**      | Root Mean Square                   | Statistical metric           |

---

## Module Types

| Abbreviation | Expansion                          | Context                      |
| ------------ | ---------------------------------- | ---------------------------- |
| **nodal-***  | NODAL module repositories          | Naming convention            |
| **nodal-hardware-*** | NODAL hardware reference designs | Hardware repositories        |

---

## Notation Conventions

### Safety Requirement IDs

Safety Requirements use a **hierarchical notation**:
