# 🤖 Stage 04: Vibe Coding & AI-Augmented Engineering

> **Roadmap**: [roadmap.sh/vibe-coding](https://roadmap.sh/vibe-coding)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Understand modern AI coding workflows: Spec-Driven Development with AI tools (Cursor, Copilot, Claude, Gemini, Antigravity).
- Master context management: providing architectural boundaries, domain schemas, and test expectations to LLMs.
- Spot AI hallucinations, subtle security vulnerabilities (SQL injection, unsafe reflection), and deprecated APIs in generated code.
- Use unit tests and automated linters as strict guardrails against AI hallucinations and regressions.

---

## 📚 Core Topics & Knowledge Map

### 1. What is "Vibe Coding" Done Right?
"Vibe coding" without engineering discipline leads to buggy, unmaintainable code that breaks in production.
**Disciplined AI Engineering** follows this workflow:
1. **Spec First**: You write the domain types, interfaces, and acceptance criteria.
2. **Test Guardrails**: You write the test cases defining expected behavior and edge cases.
3. **AI Implementation**: You prompt the AI with the precise context (interfaces + tests).
4. **Code Review & Scrutiny**: You read every single line of generated code, verifying performance, security, and edge cases.

### 2. Prompt Engineering for Java Backend Engineers
- **Bad Prompt**: `"Write a spring boot rest controller for users"`
- **Good Prompt**:
  ```markdown
  Generate a Spring Boot 3.3 REST controller for User Registration following RFC 7807 problem details.
  - Endpoint: POST /api/v1/users
  - Request DTO: CreateUserRequest (validated with jakarta.validation: @NotBlank email, @Size(min=8) password)
  - Use constructor injection
  - Return 201 Created with Location header URI
  - Use Java 21 Records for DTOs
  ```

### 3. Catching Subtle Hallucinations in Java
- Outdated Spring Security patterns (e.g. `WebSecurityConfigurerAdapter` which was removed in Spring Security 6).
- Unsafe concurrency (sharing non-thread-safe formatters or SimpleDateFormat across virtual threads).
- Inefficient database queries ($N+1$ query problems in generated JPA entities).

---

## 🧪 Assigned Exercises
Navigate to [`exercises/04-vibe-coding-lab/`](../../exercises/04-vibe-coding-lab/):
* **`EX-04-1`**: Spec-Driven Prompting for Backend APIs
* **`EX-04-2`**: Catching AI Hallucinations & Security Traps
* **`EX-04-3`**: AI-Assisted Refactoring with Test Guardrails
