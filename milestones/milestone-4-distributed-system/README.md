# 🌟 Milestone 4: Enterprise Distributed Platform (Capstone Project)

> **Prerequisites**: Stages 00 through 08  
> **Tech Stack**: Spring Boot 3.3+, Spring Security 6, JWT, Redis, Apache Kafka, PostgreSQL, Resilience4j, Docker Compose, Prometheus, Grafana, Testcontainers

---

## 🎯 Executive Summary
The ultimate capstone of **The Journey**. You will architect and implement an enterprise-grade, distributed backend system that incorporates every skill you have learned over the program.

This project is a resume centerpiece that proves you have the architectural vision, technical depth, and production instincts of a strong backend engineer.

---

## 📋 System Architecture

```
                                  [Client Apps / Postman]
                                             │
                                             ▼
                                  ┌────────────────────┐
                                  │   Spring Security  │ (JWT Validation & RBAC)
                                  └──────────┬─────────┘
                                             │
                       ┌─────────────────────┴─────────────────────┐
                       ▼                                           ▼
            ┌──────────────────────┐                    ┌──────────────────────┐
            │   Order & Billing    │                    │   Course Catalog     │
            │       Service        │                    │       Service        │
            └──────────┬───────────┘                    └──────────┬───────────┘
                       │                                           │
         ┌─────────────┴─────────────┐                             ▼
         ▼                           ▼                   ┌───────────────────┐
┌──────────────────┐        ┌──────────────────┐         │   Redis Cache     │
│  PostgreSQL DB   │        │   Apache Kafka   │         │ (Multi-tier cache)│
│ (ACID relational)│        │ (Event streaming)│         └───────────────────┘
└──────────────────┘        └────────┬─────────┘
                                     │
                                     ▼
                          ┌──────────────────────┐
                          │ Notification Service │
                          │ (Async consumer)     │
                          └──────────────────────┘

          ┌───────────────────────────────────────────────────────┐
          │                  Observability Stack                  │
          │ Spring Actuator ──> Prometheus ──> Grafana Dashboard │
          └───────────────────────────────────────────────────────┘
```

---

## 🛠️ Key Capabilities & Production Requirements

### 1. Resilient High-Throughput Services
- **Redis Multi-Level Caching**:
  - Hot catalog data cached with Cache-Aside pattern.
  - Automated invalidation on course updates.
- **Resilience4j Circuit Breakers & Rate Limiting**:
  - Outgoing payment provider and webhook calls protected by Circuit Breakers.
  - API rate-limited to prevent abuse (e.g. 50 requests/min per IP/user).

### 2. Asynchronous Event-Driven Messaging (Kafka)
- Decoupled event flow: When an order is placed, an `OrderPlacedEvent` is published to Kafka.
- Notification consumer sends confirmation emails asynchronously.
- Inventory consumer provisions access keys without blocking the HTTP request.
- Idempotency: Duplicate events must not result in double processing.

### 3. Stateless Security & Role-Based Access Control
- Spring Security 6 with JWT authentication.
- Roles: `ROLE_STUDENT`, `ROLE_INSTRUCTOR`, `ROLE_ADMIN`.
- Passwords hashed with BCrypt (strength 12).

### 4. Production Observability
- Spring Boot Actuator with Micrometer metrics.
- Prometheus scraping `/actuator/prometheus`.
- Pre-configured Grafana dashboard visualizing:
  - Request rate (RPS)
  - HTTP 5xx error rate
  - P95 and P99 response latency
  - JVM heap memory usage and Garbage Collection pauses

### 5. Single-Command Deployment
Everything runnable locally with one command:
```bash
docker compose up -d --build
```
Includes app container, PostgreSQL, Redis, Kafka, Prometheus, and Grafana.

---

## 📦 Deliverables & PR Evaluation
1. Complete codebase in `milestones/milestone-4-distributed-system/`.
2. Architecture Decision Records (ADRs) in `docs/adr/` explaining trade-offs.
3. Postman collection / OpenAPI export for all API flows.
4. Grafana dashboard export (`dashboard.json`).
5. Open PR referencing `M-04` for final capstone defense with your mentor!
