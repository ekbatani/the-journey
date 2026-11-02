# 🏛️ Exercises: Stage 07 (Software Design, SOLID & Architecture)

### `EX-07-1`: SOLID Principles Refactoring Challenge
* **Goal**: Take a monolithic, coupled class and apply all 5 SOLID principles.
* **Tasks**:
  1. Inspect `GodOrderService.java` (in this folder), which handles cart calculation, database persistence, payment gateway calls, and email sending all in one class.
  2. Refactor into:
     - **SRP**: Separate services for pricing, payment, persistence, and notifications.
     - **OCP**: Add new payment methods without modifying the payment dispatcher.
     - **LSP**: Ensure all payment gateway implementations behave consistently without runtime type checks.
     - **ISP**: Split fat interfaces into fine-grained client-specific interfaces.
     - **DIP**: Inject abstractions (interfaces) rather than concrete implementations.
  3. Verify with unit tests.

---

### `EX-07-2`: Gang of Four Design Patterns in Modern Java
* **Goal**: Implement essential GoF patterns using modern Java 21 idioms.
* **Tasks**:
  1. **Strategy Pattern**: Build a dynamic fee calculation engine with strategies for `StandardFee`, `HolidayFee`, and `VipFee`.
  2. **Factory Method / Abstract Factory**: Create notification factories for multi-channel messaging.
  3. **Builder Pattern**: Implement a fluent builder with compile-time mandatory step validation (Step Builder pattern) for `HttpRequestConfig`.
  4. **Decorator Pattern**: Wrap an `OrderService` with caching and logging decorators.

---

### `EX-07-3`: Hexagonal Architecture (Ports and Adapters)
* **Goal**: Separate pure domain logic from frameworks and infrastructure.
* **Tasks**:
  1. Create package structure:
     - `domain.model` (Order, Money, OrderStatus - zero dependencies on Spring or Hibernate)
     - `domain.port.in` (CreateOrderUseCase, CancelOrderUseCase)
     - `domain.port.out` (OrderRepositoryPort, PaymentGatewayPort)
     - `adapter.in.web` (OrderRestController)
     - `adapter.out.persistence` (JpaOrderRepositoryAdapter)
  2. Implement the use case and demonstrate that domain logic can be tested with 100% unit tests without booting Spring.

---

### `EX-07-4`: Domain-Driven Design (DDD) Core Modeling
* **Goal**: Model rich domain models rather than anemic data bags with getters and setters.
* **Tasks**:
  1. Create an `AggregateRoot`: `Account`.
  2. Protect business invariants inside methods: `account.withdraw(Money amount)` throws `InsufficientFundsException` if balance is too low.
  3. Use Value Objects (`Money`, `EmailAddress`, `Currency`) that are immutable and self-validating.
  4. Publish a `DomainEvent`: `MoneyWithdrawnEvent`.
