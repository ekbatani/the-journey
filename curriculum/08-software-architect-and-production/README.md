# 🏗️ Stage 08: Software Architect & Production Spring Boot Systems

> **Roadmap**: [roadmap.sh/software-architect](https://roadmap.sh/software-architect)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Compare architectural topologies: Modular Monolith vs Microservices tradeoffs (CAP theorem, latency, operational cost).
- Implement enterprise caching strategies with **Redis** (Cache-Aside, Write-Through, TTL, stampede prevention).
- Build asynchronous, event-driven integrations with **Apache Kafka** (producers, consumers, partitions, idempotency, dead-letter topics).
- Build fault-tolerant distributed resilience using **Resilience4j** (Circuit Breakers, Rate Limiters, Bulkheads, Retries).
- Containerize full-stack backend systems with multi-stage **Docker** and orchestrate them via **Docker Compose**.
- Implement production observability: **Spring Boot Actuator**, **Prometheus** metrics, and **Grafana** dashboards.
- Secure production APIs using **Spring Security 6** with stateless JWT authentication and Role-Based Access Control (RBAC).

---

## 📚 Core Topics & Production Patterns

### 1. Resilient Circuit Breaker (Resilience4j)
```java
@CircuitBreaker(name = "paymentGateway", fallbackMethod = "paymentFallback")
@RateLimiter(name = "paymentGateway")
public PaymentResult chargeCard(PaymentRequest request) {
    return externalPaymentClient.charge(request);
}

// Fallback method executed when circuit is OPEN or timeout occurs
public PaymentResult paymentFallback(PaymentRequest request, Throwable throwable) {
    log.error("Payment gateway failed, queuing for async retry: {}", throwable.getMessage());
    return PaymentResult.queuedForRetry(request.orderId());
}
```

### 2. Event-Driven Messaging with Apache Kafka
- Topics, Partitions, Offsets, Consumer Groups.
- Guaranteeing message ordering within a partition key.
- Idempotent consumer design using transactional outbox or deduplication keys.

### 3. Full Production Observability Stack
```
Spring Boot 3 App (Micrometer) ---> Prometheus (Scrapes /actuator/prometheus) ---> Grafana (Visual Dashboards)
```

---

## 🧪 Assigned Exercises
Navigate to [`exercises/08-system-architecture/`](../../exercises/08-system-architecture/):
* **`EX-08-1`**: Redis Caching (Cache-Aside & Invalidation)
* **`EX-08-2`**: Event-Driven Architecture with Apache Kafka
* **`EX-08-3`**: Fault Tolerance with Resilience4j (Circuit Breakers)
* **`EX-08-4`**: Observability with Actuator, Prometheus & Grafana
* **`EX-08-5`**: Spring Security 6 with JWT & Stateless Auth

---

## 🌟 Milestone 4 Checkpoint
Upon completing this stage, proceed to **[Milestone 4: Enterprise Distributed Platform Capstone](../../milestones/milestone-4-distributed-system/README.md)**.
