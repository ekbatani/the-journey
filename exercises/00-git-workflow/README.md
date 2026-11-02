# 🌿 Exercises: Stage 00 (Git & GitHub)

### `EX-00-1`: Terminal Git & SSH Setup
* **Goal**: Configure local git environment without any GUI tools.
* **Tasks**:
  1. Set up SSH key and test connection to GitHub (`ssh -T git@github.com`).
  2. Configure `git config --global core.editor` and alias commands (e.g. `git config --global alias.lg "log --graph --oneline --all"`).
  3. Create a test commit in a personal test branch, demonstrating atomic commits with conventional commit message prefixes (`feat:`, `chore:`).
* **Deliverable**: Open PR updating `PROGRESS.md` for `EX-00-1` with your experience.

---

### `EX-00-2`: Branching & Conflict Resolution
* **Goal**: Understand git merge conflicts and resolve them systematically.
* **Tasks**:
  1. Create two branches from `main`: `feature/feature-a` and `feature/feature-b`.
  2. Modify the same file `exercises/00-git-workflow/sandbox.txt` on different branches with conflicting text.
  3. Commit on both branches.
  4. Attempt to merge `feature/feature-b` into `feature/feature-a`.
  5. Inspect the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
  6. Resolve the conflict cleanly, stage, and complete the merge.
* **Deliverable**: Submit a PR showing the clean merge resolution commit history.

---

### `EX-00-3`: Pull Request & Code Review Workflow
* **Goal**: Learn the end-to-end PR cycle used by top engineering teams.
* **Tasks**:
  1. Create branch `exercise/00-3-pr-workflow`.
  2. Introduce a new utility note in `exercises/00-git-workflow/my-git-cheatsheet.md`.
  3. Fill out the full `.github/PULL_REQUEST_TEMPLATE.md` with honest difficulty and time tracking.
  4. Request mentor review and address at least one suggested revision.
