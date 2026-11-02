# 🌟 Milestone 3: Hexagonal Core Domain Engine with ArchUnit

> **Prerequisites**: Stage 07  
> **Tech Stack**: Java 21, Hexagonal Architecture (Ports & Adapters), DDD, ArchUnit, Spring Boot 3

---

## 🎯 Executive Summary
Take a complex, mission-critical business domain (e.g. **Subscription & Billing Life Cycle** or **Order Fulfillment Engine**) and architect it strictly following **Hexagonal Architecture (Ports and Adapters)** and **Domain-Driven Design (DDD)**.

The pure business domain must reside in a core module that has **zero dependencies** on Spring, Hibernate, or any external framework. All infrastructure concerns (HTTP controllers, JPA entities, Kafka producers) plug in through Ports and Adapters.

---

## 🏛️ Architectural Blueprint

```
                      ┌─────────────────────────────────────────┐
                      │            INBOUND ADAPTERS             │
                      │  [Web API Controller]   [CLI Runner]    │
                      └──────────────────┬──────────────────────┘
                                         │
                                         ▼ (calls)
                      ┌─────────────────────────────────────────┐
                      │             INBOUND PORTS               │
                      │  [CheckoutOrderUseCase]                 │
                      │  [CancelSubscriptionUseCase]            │
                      └──────────────────┬──────────────────────┘
                                         │
                                         ▼
                      ┌─────────────────────────────────────────┐
                      │            CORE DOMAIN LAYER            │
                      │  • Aggregate: Subscription, Invoice     │
                      │  • Entities & Value Objects: Money      │
                      │  • Domain Events: PaymentProcessedEvent │
                      │  • Pure Java (NO SPRING / NO JPA)       │
                      └──────────────────┬──────────────────────┘
                                         │
                                         ▼ (calls)
                      ┌─────────────────────────────────────────┐
                      │             OUTBOUND PORTS              │
                      │  [SubscriptionRepositoryPort]           │
                      │  [PaymentGatewayPort]                   │
                      │  [NotificationEventPort]                │
                      └──────────────────┬──────────────────────┘
                                         ▲
                                         │ (implements)
                      ┌──────────────────┴──────────────────────┐
                      │            OUTBOUND ADAPTERS            │
                      │  [PostgreSqlJpaAdapter] [StripeAdapter] │
                      │  [KafkaDomainEventPublisher]            │
                      └─────────────────────────────────────────┘
```

---

## 📋 Domain Requirements

1. **Rich Domain Aggregates**:
   - `Subscription` with states: `TRIAL`, `ACTIVE`, `PAST_DUE`, `CANCELED`.
   - Business methods enforce all invariants:
     - Cannot renew a `CANCELED` subscription.
     - Grace period transitions to `PAST_DUE` if payment fails 3 times.
2. **Value Objects**:
   - `Money` (encapsulating currency equality and round-off arithmetic).
   - `BillingCycle` (`MONTHLY`, `ANNUAL`).
3. **Domain Events**:
   - Emits `SubscriptionRenewedEvent`, `SubscriptionCanceledEvent`.

---

## 🛡️ Architecture Enforcement with ArchUnit
You must write automated architecture tests that will fail the build if someone tries to introduce framework dependencies into the domain layer:
```java
@ArchTest
static final ArchRule domain_must_be_free_of_frameworks =
    noClasses().that().resideInAPackage("..domain..")
        .should().dependOnClassesThat().resideInAnyPackage(
            "org.springframework..",
            "jakarta.persistence..",
            "org.hibernate.."
        );
```

---

## 📦 How to Submit
1. Branch: `milestone/m03-clean-architecture`.
2. Open PR referencing `M-03`.
3. Include ArchUnit test execution results.
