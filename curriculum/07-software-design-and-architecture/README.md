# 🏛️ Stage 07: Software Design & Clean Architecture

> **Roadmap**: [roadmap.sh/software-design-architecture](https://roadmap.sh/software-design-architecture)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Apply the **SOLID** principles naturally in everyday object-oriented Java code.
- Implement essential Gang of Four (GoF) design patterns: Strategy, Factory, Builder, Observer, Decorator, Adapter.
- Understand **Hexagonal Architecture** (Ports & Adapters) and Onion/Clean Architecture.
- Apply core **Domain-Driven Design (DDD)** concepts: Ubiquitous Language, Entities, Value Objects, Aggregates, Domain Events, and Repositories.
- Enforce architecture boundaries automatically using **ArchUnit** tests in Java.

---

## 📚 Core Topics & Knowledge Map

### 1. SOLID Principles
- **S - Single Responsibility Principle**: A class should have only one reason to change.
- **O - Open/Closed Principle**: Open for extension, closed for modification (polymorphism / Strategy).
- **L - Liskov Substitution Principle**: Subtypes must be substitutable for their base types without altering correctness.
- **I - Interface Segregation Principle**: Clients should not be forced to depend on methods they do not use.
- **D - Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions.

### 2. Hexagonal Architecture (Ports and Adapters)
```
          +-----------------------------------------+
          |           INBOUND ADAPTERS              |
          |  (REST Controller, CLI, Message Queue)  |
          +--------------------+--------------------+
                               |
                               v (implements/calls)
          +--------------------+--------------------+
          |              INBOUND PORT               |
          |         (Use Case Interfaces)           |
          +--------------------+--------------------+
                               |
                               v
          +--------------------+--------------------+
          |            APPLICATION CORE             |
          |       (Domain Models, Aggregates,       |
          |          Pure Business Rules)           |
          +--------------------+--------------------+
                               |
                               v (calls)
          +--------------------+--------------------+
          |              OUTBOUND PORT              |
          |       (Repository / Gateway SPI)        |
          +--------------------+--------------------+
                               ^
                               | (implements)
          +--------------------+--------------------+
          |           OUTBOUND ADAPTERS             |
          |    (PostgreSQL JPA, Redis, Kafka)       |
          +-----------------------------------------+
```

### 3. Architecture Testing with ArchUnit
```java
@AnalyzeClasses(packages = "com.journey.domain")
class ArchitectureTest {
    @ArchTest
    static final ArchRule domain_should_not_depend_on_spring_or_persistence =
        noClasses().that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAnyPackage(
                "..org.springframework..",
                "..jakarta.persistence.."
            );
}
```

---

## 🧪 Assigned Exercises
Navigate to [`exercises/07-design-patterns-solid/`](../../exercises/07-design-patterns-solid/):
* **`EX-07-1`**: SOLID Principles Refactoring Challenge
* **`EX-07-2`**: Gang of Four Design Patterns in Modern Java
* **`EX-07-3`**: Hexagonal Architecture (Ports and Adapters)
* **`EX-07-4`**: Domain-Driven Design (DDD) Core Modeling

---

## 🌟 Milestone 3 Checkpoint
Upon completing this stage, proceed to **[Milestone 3: Hexagonal Order Fulfillment Core with ArchUnit](../../milestones/milestone-3-clean-architecture/README.md)**.
