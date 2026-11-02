# 🧭 Mentor Playbook & Review Guide

This guide is designed for the mentor to maintain high review standards, track velocity constructively without adding pressure, and nurture problem-solving independence.

---

## 🎯 Mentorship Principles

1. **Guide, Don't Hand Out Answers**:
   * If a solution has a bug, highlight the failing edge-case or suggest a test: *"What happens if the input list contains duplicate null values?"* rather than rewriting the code for her.
2. **Review for Craftsmanship, Not Just Correctness**:
   * Does the code work? (Passes tests)
   * Is it idiomatic Java 21? (Using modern constructs, streams where appropriate, not overusing loops when streams are cleaner, not overcomplicating simple loops).
   * Is the domain model expressive? (Meaningful variable/class names, proper encapsulation).
   * Are tests readable and comprehensive?
3. **Celebrate Velocity & Momentum**:
   * Acknowledge good commits, clean PR descriptions, and perseverance.
   * If an exercise had a high difficulty rating (4 or 5), schedule a quick 15-minute sync or write an explanatory diagram to reinforce the underlying intuition.

---

## 🔍 Pull Request Review Checklist

When reviewing an exercise or milestone PR, check:

- [ ] **Requirements & Acceptance Criteria**: Did the code fulfill all points in the exercise specification?
- [ ] **Idiomatic Java 21+**: Does it use modern Java features (`var` appropriately, records, pattern matching, modern streams, `Optional` properly)?
- [ ] **Clean Code & SOLID**:
  - Functions are small and have a single responsibility.
  - No magic numbers or hardcoded strings.
  - Exceptions are meaningful (no generic `catch (Exception e)` swallowing).
- [ ] **Testing Standards**:
  - Unit tests follow Arrange-Act-Assert (AAA) or Given-When-Then.
  - Edge cases covered (empty collections, invalid inputs, boundary values).
  - Clear assertion messages using AssertJ.
- [ ] **Git Hygiene**:
  - Clean commit history with conventional commit prefixes.
  - Branch named properly.

---

## ⏱️ Monitoring Velocity & Detecting Friction Points

Run `python3 tools/tracker.py` periodically to review:
1. **Cycle Time**: Days elapsed between branch creation / start date and merge.
2. **Logged Effort**: Hours reported per exercise.
3. **Difficulty Trends**:
   * If consecutive exercises are marked 4–5 in difficulty, step in for a pairing session.
   * If exercises are marked 1–2 with rapid turnaround, encourage tackling the extra credit challenges or moving directly to the milestone project.
