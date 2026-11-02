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
* On macOS/Linux, install [SDKMAN!](https://sdkman.io/):
  ```bash
  curl -s "https://get.sdkman.io" | bash
  source "$HOME/.sdkman/bin/sdkman-init.sh"
  sdk install java 21.0.2-tem
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
   git checkout -b exercise/00-1-terminal-git
   ```
2. Navigate to [`curriculum/00-git-and-github/README.md`](curriculum/00-git-and-github/README.md) and [`exercises/00-git-workflow/`](exercises/00-git-workflow/).
3. Complete the task in `exercises/00-git-workflow/ex-00-1/`.
4. Open your first Pull Request!
