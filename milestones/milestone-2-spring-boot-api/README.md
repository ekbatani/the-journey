# 🌟 Milestone 2: Production Spring Boot 3 REST API + PostgreSQL

> **Prerequisites**: Stages 04, 05, 06  
> **Tech Stack**: Java 21, Spring Boot 3.3+, Spring Data JPA, PostgreSQL, Flyway, Testcontainers, Docker, OpenAPI / Swagger

---

## 🎯 Executive Summary
Build a production-grade backend REST API for a **Mentorship & Learning Management Platform** ("The Journey API").

This project bridges database engineering, modern Spring Boot web development, and AI-assisted workflows into a complete real-world service.

---

## 📋 Architecture & Features

### 1. Domain Entities & Schema (Managed by Flyway)
- **Mentee**: `id`, `email`, `full_name`, `bio`, `github_username`, `created_at`
- **CourseTrack**: `id`, `title`, `slug`, `description`, `total_stages`, `is_published`
- **Submission**: `id`, `mentee_id`, `exercise_id`, `github_pr_url`, `status` (`SUBMITTED`, `IN_REVIEW`, `APPROVED`, `CHANGES_REQUESTED`), `time_spent_hours`, `difficulty_score`, `created_at`
- **ReviewFeedback**: `id`, `submission_id`, `mentor_id`, `feedback_text`, `rating`, `created_at`

### 2. REST Endpoints
- `POST /api/v1/mentees` (Register mentee with validation)
- `GET /api/v1/mentees/{id}` (Retrieve profile with current stage)
- `GET /api/v1/submissions` (Filter by status, pagination via `Pageable`, sorting)
- `POST /api/v1/submissions` (Create new submission with duplicate check)
- `POST /api/v1/submissions/{id}/reviews` (Mentor submits feedback & updates status)
- `GET /api/v1/analytics/velocity/{menteeId}` (Calculates average cycle time and total hours logged)

### 3. Engineering Best Practices
- **Validation**: Strict input validation using `jakarta.validation` (`@NotNull`, `@Email`, `@Min`, `@Max`).
- **Global Error Handling**: `@RestControllerAdvice` emitting standard RFC 7807 `ProblemDetails` responses with timestamp, path, and error code.
- **DTO Layer**: Java 21 Records for all Request/Response bodies (never expose JPA entities directly to the API!).
- **Documentation**: Swagger UI accessible at `/swagger-ui.html` generated with `springdoc-openapi`.

---

## 🧪 Integration Testing with Testcontainers
- No mocks for database testing!
- Use **Testcontainers** to automatically spin up a real PostgreSQL 16 container during `./mvnw test`.
- Verify full HTTP slice tests using `MockMvc` or `WebTestClient`.

---

## 🤖 Vibe Coding / AI Log Requirement
In your PR, include a dedicated section documenting how you used AI tools (Cursor, Copilot, Antigravity):
- Which prompts were used to scaffold DTOs or Testcontainers configuration?
- What errors or hallucinations did the AI produce that you had to fix?

---

## 📦 How to Submit
1. Branch: `milestone/m02-spring-boot-api`.
2. Open PR referencing `M-02`.
