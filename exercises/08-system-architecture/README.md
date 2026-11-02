# 🏗️ Exercises: Stage 08 (Software Architect & Production Spring Boot Systems)

### `EX-08-1`: Redis Caching (Cache-Aside & Invalidation)
* **Goal**: Implement high-throughput caching and avoid stale data.
* **Tasks**:
  1. Set up Redis with Docker (`docker run -d -p 6379:6379 redis:7-alpine`).
  2. Implement Spring Cache with `@Cacheable(value = "products", key = "#id")`.
  3. Implement Cache-Aside with custom RedisTemplate:
     - Check cache first.
     - On cache miss, fetch from DB and populate cache with 15-minute TTL.
  4. Implement `@CacheEvict` and `@CachePut` on product update and delete operations.
  5. Demonstrate cache hit vs miss latency differences in a test benchmark.

---

### `EX-08-2`: Event-Driven Architecture with Apache Kafka
* **Goal**: Build asynchronous, decoupled event-driven services.
* **Tasks**:
  1. Run Kafka with Docker Compose (`zookeeper` or KRaft mode + `kafka` broker).
  2. Create an event topic: `order-placed-events`.
  3. Implement `OrderEventProducer` publishing strongly typed JSON events (`OrderPlacedEvent`).
  4. Implement `NotificationConsumer` and `InventoryConsumer` listening on the same topic under different consumer groups.
  5. Implement error handling with a Dead-Letter Queue (DLQ) topic for unprocessable messages.

---

### `EX-08-3`: Fault Tolerance with Resilience4j (Circuit Breakers)
* **Goal**: Prevent cascading failures in distributed systems.
* **Tasks**:
  1. Simulate an unreliable third-party payment gateway that fails 60% of the time.
  2. Configure Resilience4j `@CircuitBreaker`:
     - Failure rate threshold: 50%
     - Sliding window size: 10 calls
     - Wait duration in open state: 5 seconds
  3. Provide a graceful fallback method returning a pending status instead of throwing HTTP 500.
  4. Write an automated integration test verifying state transitions: `CLOSED` -> `OPEN` -> `HALF_OPEN` -> `CLOSED`.

---

### `EX-08-4`: Observability with Actuator, Prometheus & Grafana
* **Goal**: Monitor the health, latency, and memory of your backend in real time.
* **Tasks**:
  1. Add `spring-boot-starter-actuator` and `micrometer-registry-prometheus`.
  2. Expose `/actuator/health` and `/actuator/prometheus`.
  3. Create custom Micrometer metrics:
     - Counter: `orders.placed.total`
     - Timer: `order.processing.duration`
  4. Launch Prometheus and Grafana in Docker Compose. Configure Prometheus to scrape the Spring Boot application and visualize requests per second and memory usage on a Grafana dashboard.

---

### `EX-08-5`: Spring Security 6 with JWT & Stateless Auth
* **Goal**: Implement secure stateless authentication and authorization.
* **Tasks**:
  1. Configure `SecurityFilterChain` bean (modern Spring Security 6 lambda DSL).
  2. Disable session state (`SessionCreationPolicy.STATELESS`).
  3. Create `/api/v1/auth/login` issuing a signed JSON Web Token (JWT) with user roles.
  4. Implement `JwtAuthenticationFilter` verifying tokens on incoming requests.
  5. Protect endpoints using `@PreAuthorize("hasRole('ADMIN')")`.
