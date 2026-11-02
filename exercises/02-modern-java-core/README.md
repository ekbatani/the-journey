# ☕ Exercises: Stage 02 (Modern Java Core)

### `EX-02-1`: Records, Pattern Matching & Sealed Types
* **Goal**: Master Java 17/21 language features for expressive, immutable domain models.
* **Tasks**:
  1. Define a sealed hierarchy `NotificationEvent` with permits: `EmailNotification`, `SmsNotification`, `PushNotification`.
  2. Implement each subtype as a Java `record` with appropriate fields (e.g. recipient, payload, timestamp).
  3. Write a pattern-matching `switch` function `dispatchNotification(NotificationEvent event)` that exhaustively formats and routes the message.
  4. Write unit tests verifying that all permitted types compile and route correctly.

---

### `EX-02-2`: Streams API & Functional Pipelines
* **Goal**: Replace imperative for-loops with declarative Streams.
* **Tasks**:
  1. Given a list of 1,000 transaction records:
     - Filter transactions above \$100.
     - Extract unique customer emails.
     - Group total spend by transaction category (`Collectors.groupingBy`).
     - Find the top 3 highest spending customers.
     - Partition transactions into fraudulent vs legitimate using a custom predicate.
  2. Write unit tests verifying results against known test fixtures.

---

### `EX-02-3`: Generics & Collections Deep Dive
* **Goal**: Understand generic type parameters, wildcards (`? extends T`, `? super T`), and collection performance.
* **Tasks**:
  1. Implement a generic bounded buffer `RingBuffer<T>` with a fixed capacity.
  2. Support `enqueue(T item)` and `T dequeue()`.
  3. Implement a generic utility method using Producer Extends Consumer Super (`PECS`) to copy and drain elements safely between collections.
  4. Benchmark `ArrayList` vs `LinkedList` on insertions at head, middle, and tail.

---

### `EX-02-4`: Modern Concurrency & Virtual Threads
* **Goal**: Experience Java 21 Virtual Threads and compare them with Platform Threads.
* **Tasks**:
  1. Simulate 10,000 concurrent network tasks (each sleeping for 100ms to simulate I/O).
  2. First execute using `Executors.newFixedThreadPool(200)`. Measure total elapsed time and memory footprint.
  3. Re-run using `Executors.newVirtualThreadPerTaskExecutor()`.
  4. Compare latency, throughput, and memory consumption. Document in `concurrency-report.md`.

---

### `EX-02-5`: Unit Testing with JUnit 5 & AssertJ
* **Goal**: Master professional testing conventions (AAA pattern, Parameterized tests, Mockito).
* **Tasks**:
  1. Build a `PricingEngine` class that calculates discounts, taxes, and shipping rates.
  2. Write `@ParameterizedTest` with `@CsvSource` to test 10 different coupon and country combinations.
  3. Mock an external currency conversion service using `org.mockito.Mockito`.
  4. Write fluent AssertJ assertions (`assertThat(result).isNotNull().hasFieldOrPropertyWithValue(...)`).
