# 🌟 Mentee Onboarding: Your First Day

Welcome to **The Journey**! Before diving into code, let's configure your local developer workstation so you have an identical setup to professional backend developers.

---

## 🛠️ Step 1: Install Core Developer Tools

### 1. Git & GitHub CLI
* **Install Git**: [git-scm.com](https://git-scm.com/)
* Configure your name and email:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  ```
* Set up SSH keys with GitHub: [GitHub SSH Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### 2. Java 21 LTS SDK (via SDKMAN! or Temurin)
Modern backend Java currently standards on **Java 21 LTS**.
* **Windows**: install Eclipse Temurin 21 with `winget` (in PowerShell or Terminal), then open a **new** terminal window:
  ```powershell
  winget install EclipseAdoptium.Temurin.21.JDK
  ```
  *(Or download the `.msi` from [adoptium.net](https://adoptium.net/) and tick "Set JAVA_HOME" during install.)*
* **macOS/Linux**: install [SDKMAN!](https://sdkman.io/), then pick the newest `21.x.x-tem` from `sdk list java`:
  ```bash
  curl -s "https://get.sdkman.io" | bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  sdk list java
  sdk install java 21.0.x-tem   # replace x with the newest 21 version listed
  ```
* Verify installation:
  ```bash
  java -version
  ```
  *(Ensure it outputs version 21.x.x)*

### 3. Integrated Development Environment (IDE)
* **IntelliJ IDEA Community or Ultimate** (Recommended standard for Java): [JetBrains IntelliJ](https://www.jetbrains.com/idea/)
* Recommended plugins:
  * Rainbow Brackets
  * GitToolBox
  * Key Promoter X

### 4. Docker Desktop / OrbStack
Required later for running PostgreSQL, Redis, Kafka, and Testcontainers.
* Install Docker: [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/)

---

## 🚀 Step 2: Clone The Repository

```bash
git clone https://github.com/ekbatani/the-journey.git
cd the-journey
```

---

## 🎯 Step 3: Your Very First Mission (Exercise 00-1)

To test your Git setup and the PR workflow:
1. Create a branch:
   ```bash
   git checkout -b exercise/00-1-git-setup
   ```
   *(Branch names follow the `exercise/<id>-<short-description>` convention from [CONTRIBUTING.md](CONTRIBUTING.md).)*
2. Read [`curriculum/00-git-and-github/README.md`](curriculum/00-git-and-github/README.md).
3. Complete the `EX-00-1` tasks described in [`exercises/00-git-workflow/README.md`](exercises/00-git-workflow/README.md). Put any files you create directly in `exercises/00-git-workflow/` (e.g. `ex-00-1-test.txt`).
4. Push your branch and open your first Pull Request — never upload files straight to `main` through the GitHub website; every change goes through a PR so it can be reviewed.
