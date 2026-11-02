# 🌿 Stage 00: Git & GitHub Mastery

> **Roadmap**: [roadmap.sh/git-github](https://roadmap.sh/git-github)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Understand the Git data model (blobs, trees, commits, references).
- Master terminal Git commands without relying on GUI shortcuts.
- Resolve tricky merge conflicts with confidence using rebase or merge.
- Follow professional branching workflows, conventional commit messages, and Pull Request etiquette.

---

## 📚 Core Topics & Knowledge Map

### 1. The Three Trees of Git
- **Working Directory**: Your local sandbox of files.
- **Staging Area (Index)**: The snapshot ready to be committed (`git add`).
- **Repository (.git directory)**: The immutable history of commits (`git commit`).

### 2. Essential Commands
```bash
git status                     # Check state of working dir and index
git add <file>                 # Stage specific file
git commit -m "feat: message"  # Commit staged changes
git log --oneline --graph --all# Visualize commit history tree
git diff                       # Inspect unstaged changes
git diff --staged              # Inspect staged changes
```

### 3. Branching & Conflict Resolution
```bash
git checkout -b feature/name   # Create and switch to new branch
git switch -c feature/name     # Modern alternative
git merge <branch>             # Merge branch into current
git rebase <branch>            # Rebase current branch on top of target
```

---

## 🧪 Assigned Exercises
Navigate to [`exercises/00-git-workflow/`](../../exercises/00-git-workflow/):
* **`EX-00-1`**: Terminal Git & SSH Setup
* **`EX-00-2`**: Branching & Conflict Resolution
* **`EX-00-3`**: Pull Request & Code Review Workflow
