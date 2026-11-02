# 🤖 Exercises: Stage 04 (Vibe Coding & AI-Augmented Engineering)

### `EX-04-1`: Spec-Driven Prompting for Backend APIs
* **Goal**: Learn how to prompt AI like a senior software architect rather than a novice.
* **Tasks**:
  1. Write a formal technical specification for a "Currency Exchange Service" in Markdown:
     - API contract (input JSON, output JSON, error codes).
     - Data models (using Java 21 Records).
     - Cache requirement (TTL 10 minutes).
     - Concurrency requirement (thread-safe).
  2. Feed this exact spec to an LLM (Claude, Cursor, Copilot, or ChatGPT) and prompt it to generate the implementation.
  3. Compare the generated output with an un-specced one-liner prompt: *"Write currency exchange in java"*.
  4. Document the differences in code quality, edge case handling, and architecture in `spec-prompt-comparison.md`.

---

### `EX-04-2`: Catching AI Hallucinations & Security Traps
* **Goal**: Train your review radar on flawed AI-generated code.
* **Tasks**:
  1. Inspect the provided file in this folder: `UnsafeAiSnippet.java`.
  2. Identify at least 4 critical flaws planted in the code:
     - SQL Injection vulnerability.
     - Race condition in a shared mutable state.
     - Deprecated Spring Security method.
     - Memory leak caused by unclosed resources.
  3. Refactor the snippet into safe, modern Java 21 code and write tests proving the fix.

---

### `EX-04-3`: AI-Assisted Refactoring with Test Guardrails
* **Goal**: Use AI safely to refactor legacy code by building a test harness first.
* **Tasks**:
  1. Take the legacy "spaghetti" class `LegacyReportGenerator.java`.
  2. Before touching the code or asking AI, write an exhaustive unit test suite capturing current behavior (Golden Master / Characterization Tests).
  3. Use AI to assist in decomposing the class into clean, Single-Responsibility components.
  4. Run your test harness after every AI suggestion to guarantee zero behavioral regressions.
