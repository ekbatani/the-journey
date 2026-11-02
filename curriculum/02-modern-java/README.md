# ☕ Stage 02: Modern Java (Java 21 LTS)

> **Roadmap**: [roadmap.sh/java](https://roadmap.sh/java)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Master modern Java (Java 17/21 LTS): `records`, `sealed interfaces`, pattern matching for switch.
- Write functional, declarative data pipelines using Java Streams and Lambda expressions.
- Thoroughly understand the Collections Framework (`List`, `Set`, `Map`, `Queue`) and generics.
- Understand modern concurrency: Platform Threads vs Virtual Threads (`Project Loom`).
- Write professional test suites with **JUnit 5**, **AssertJ**, and **Mockito**.

---

## 📚 Core Topics & Knowledge Map

### 1. Modern Java Idioms (Java 17 & 21)
```java
// Records: Immutable data carriers with auto equals/hashCode/toString
public record OrderItem(String productId, int quantity, BigDecimal unitPrice) {}

// Sealed Interfaces: Explicitly permit permitted subtypes
public sealed interface PaymentMethod permits CreditCard, BankTransfer, Crypto {}
public record CreditCard(String cardNumber, String cvv) implements PaymentMethod {}
public record BankTransfer(String iban) implements PaymentMethod {}
public record Crypto(String walletAddress) implements PaymentMethod {}

// Pattern Matching for Switch
public String processPayment(PaymentMethod payment) {
    return switch (payment) {
        case CreditCard cc   -> "Charging card " + cc.cardNumber();
        case BankTransfer bt -> "Transferring to IBAN " + bt.iban();
        case Crypto c        -> "Sending to " + c.walletAddress();
    };
}
```

### 2. Streams API & Functional Pipelines
- Intermediate operations: `filter()`, `map()`, `flatMap()`, `distinct()`, `sorted()`.
- Terminal operations: `collect()`, `reduce()`, `count()`, `anyMatch()`.
- Advanced collectors: `Collectors.groupingBy()`, `Collectors.partitioningBy()`, `Collectors.toMap()`.

### 3. Concurrency in Java 21 (Virtual Threads)
```java
// Traditional pool: Expensive OS threads
ExecutorService platformPool = Executors.newFixedThreadPool(100);

// Modern Java 21: Lightweight Virtual Threads (millions can run concurrently!)
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> fetchRemoteData());
}
```

### 4. Unit Testing with AssertJ & JUnit 5
```java
@Test
void shouldCalculateTotalPriceForItems() {
    // Given
    var cart = new ShoppingCart();
    cart.add(new OrderItem("p1", 2, new BigDecimal("10.00")));

    // When
    BigDecimal total = cart.calculateTotal();

    // Then
    assertThat(total).isEqualByComparingTo("20.00");
}
```

---

## 🧪 Assigned Exercises
Navigate to [`exercises/02-modern-java-core/`](../../exercises/02-modern-java-core/):
* **`EX-02-1`**: Records, Pattern Matching & Sealed Types
* **`EX-02-2`**: Streams API & Functional Pipelines
* **`EX-02-3`**: Generics & Collections Deep Dive
* **`EX-02-4`**: Modern Concurrency & Virtual Threads
* **`EX-02-5`**: Unit Testing with JUnit 5 & AssertJ
