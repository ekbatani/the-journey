# 🌟 Milestone 1: CLI Analytics & Expense Engine

> **Prerequisites**: Stages 00, 01, 02, 03  
> **Tech Stack**: Pure Java 21 LTS, Collections, Streams, File I/O, JUnit 5, AssertJ, Maven

---

## 🎯 Executive Summary
Build a standalone, high-performance financial transaction analytics engine from scratch in pure Java 21 without any web frameworks.

This project proves you have mastered:
- Object-Oriented Design & Clean Code
- Modern Java 21 features (Records, Pattern Matching, Sealed Interfaces)
- Streams API and complex aggregations
- Algorithmic efficiency and custom data structures
- Comprehensive Unit Testing & Git collaboration

---

## 📋 Business Requirements & User Stories

### Story 1: Data Ingestion & Validation
The engine must parse CSV and JSON financial transactions:
```csv
id,timestamp,category,merchant,amount,currency,payment_type
tx-001,2026-10-01T14:32:00Z,GROCERIES,Whole Foods,84.50,USD,CREDIT_CARD
tx-002,2026-10-01T18:10:00Z,TECH,Apple Store,1299.00,USD,DEBIT_CARD
```
- Validate all fields: non-empty IDs, positive amounts, valid ISO-8601 timestamps.
- Malformed rows must be routed to an `ErrorLog` with specific rejection reasons without crashing the ingestion process.

### Story 2: Transaction Analytics Engine
Implement query capabilities via an interactive or scriptable CLI:
1. **Total Spend by Category**: Group and sum amounts by category (e.g. `GROCERIES: $450.00`, `TECH: $1,299.00`).
2. **Monthly Expense Breakdown**: Pivot spend by Year-Month.
3. **Outlier / Anomaly Detection**: Algorithmic detection of suspicious transactions (transactions exceeding $2.5 \times$ the standard deviation of that category's average).
4. **Top N Merchants**: Find top $N$ merchants by total transaction volume using a `PriorityQueue` (Min-Heap) for $O(K \log N)$ efficiency.

### Story 3: Clean Architecture & Extensibility
- Store parsed records in an in-memory repository with custom indexing for fast lookup by category and date range.
- Produce formatted reports in Markdown, CSV, and Console Table formats using the Strategy pattern.

---

## 🧪 Testing & Quality Gates
- **100% Test Coverage** on domain models and calculation logic.
- Use `@ParameterizedTest` with edge cases:
  - Empty files, corrupted timestamps, negative amounts, large datasets ($100,000+$ rows).
- Benchmarking report: Measure ingestion and query latency for 100k transactions.

---

## 📦 How to Submit
1. Work in branch `milestone/m01-cli-expense-engine`.
2. Build the project under `milestones/milestone-1-cli-task-engine/`.
3. Open a Pull Request referencing `M-01`.
4. Include test coverage reports and execution screenshots in the PR description.
