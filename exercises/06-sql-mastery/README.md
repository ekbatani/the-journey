# 🗄️ Exercises: Stage 06 (Relational Databases & SQL Mastery)

### `EX-06-1`: PostgreSQL Schema Modeling (3NF & Constraints)
* **Goal**: Design a clean, normalized relational schema in PostgreSQL.
* **Tasks**:
  1. Model an e-learning platform in `01_schema.sql`:
     - `users` (id, email, password_hash, role, created_at)
     - `courses` (id, instructor_id, title, price, is_published, created_at)
     - `enrollments` (id, user_id, course_id, enrolled_at, completion_percentage)
     - `reviews` (id, course_id, user_id, rating 1-5, comment, created_at)
  2. Add foreign keys, primary keys, `NOT NULL`, and `CHECK` constraints (e.g. `rating BETWEEN 1 AND 5`).
  3. Ensure 3NF compliance (no transitive dependencies).

---

### `EX-06-2`: Advanced Joins, Aggregations & Subqueries
* **Goal**: Write complex queries combining multiple relations.
* **Tasks** in `02_queries.sql`:
  1. Find all courses with more than 10 enrollments and an average rating $\ge 4.5$.
  2. List instructors whose total revenue exceeds \$5,000, ordered from highest to lowest.
  3. Find students who enrolled in a course but never left a review (`LEFT JOIN` / `IS NULL`).
  4. Write a subquery finding the most popular course in each category.

---

### `EX-06-3`: Window Functions, CTEs & Analytics
* **Goal**: Use analytical SQL to generate reports without bringing data into Java.
* **Tasks** in `03_analytics.sql`:
  1. Use Common Table Expressions (CTEs) to calculate monthly new student signups.
  2. Use `ROW_NUMBER() OVER (PARTITION BY instructor_id ORDER BY price DESC)` to find each instructor's top 2 most expensive courses.
  3. Calculate running cumulative revenue using `SUM(price) OVER (ORDER BY enrolled_at)`.
  4. Compare each month's sales to the previous month using `LAG()`.

---

### `EX-06-4`: Indexing, EXPLAIN ANALYZE & Query Tuning
* **Goal**: Read execution plans and optimize slow queries.
* **Tasks**:
  1. Populate tables with 100,000 synthetic rows using `generate_series()`.
  2. Execute query searching by user email and course title.
  3. Run `EXPLAIN (ANALYZE, BUFFERS)` to observe the `Seq Scan`.
  4. Create targeted B-Tree indexes: `CREATE INDEX ...`.
  5. Re-run `EXPLAIN ANALYZE` and document the query execution time improvement in `indexing-report.md`.

---

### `EX-06-5`: Flyway Database Migrations in Practice
* **Goal**: Use Flyway for automated schema evolution.
* **Tasks**:
  1. Structure migration directory `src/main/resources/db/migration/`:
     - `V1__init_schema.sql`
     - `V2__add_user_phone_column.sql`
     - `V3__add_composite_index.sql`
  2. Verify migration checksums and idempotency.
