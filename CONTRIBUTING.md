# 🛠️ Mentee Contribution & Workflow Guide

To ensure you develop real-world software engineering instincts, all work in **The Journey** follows professional Git & GitHub standards.

---

## 🌿 Branching Strategy

1. Always branch off the latest `main`:
   ```bash
   git checkout main
   git pull origin main
   ```
2. Create a meaningful branch name according to task type:
   * **For exercises**: `exercise/<id>-<short-description>`
     * Example: `git checkout -b exercise/02-1-records-and-patterns`
     * Example: `git checkout -b exercise/06-3-window-functions`
   * **For milestones**: `milestone/<milestone-id>-<name>`
     * Example: `git checkout -b milestone/m01-cli-expense-engine`
     * Example: `git checkout -b milestone/m02-spring-boot-api`

---

## ✍️ Commit Message Guidelines

Use [Conventional Commits](https://www.conventionalcommits.org/):
* `feat(ex-02-1): implement pattern matching for payment processor`
* `test(ex-02-5): add junit5 parameterized tests for calculator`
* `refactor(m-01): extract transaction parser into dedicated service`
* `docs(progress): update status for exercise 01-2`

Keep commits focused and atomic. Avoid single monolithic commits titled `"done"`.

---

## 📬 Pull Request Workflow

1. Push your branch to GitHub:
   ```bash
   git push -u origin exercise/02-1-records-and-patterns
   ```
2. Open a Pull Request against `main`.
3. GitHub will auto-populate the **Pull Request Template**. Make sure to fill in:
   * **Time Spent**: Estimate honest hours spent on this task.
   * **Difficulty (1-5)**: 1 (Walk in the park) to 5 (Had to battle through).
   * **What was learned**: Key concepts that clicked.
   * **Questions for Mentor**: Anything that felt awkward or unclear.
4. Notify your mentor or request a review.
5. If the mentor requests changes:
   * Make edits on the same branch.
   * Push your updates (`git push`).
   * Re-request review.
6. Once approved, the mentor will merge the PR.
7. Update `PROGRESS.md` with completion date, hours, and link to your PR!
