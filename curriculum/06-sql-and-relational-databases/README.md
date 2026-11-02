# 🗄️ Stage 06: Relational Databases & SQL Mastery

> **Roadmap**: [roadmap.sh/sql](https://roadmap.sh/sql)

---

## 🎯 Learning Objectives
By the end of this stage, you should:
- Design normalized relational schemas (1NF, 2NF, 3NF) with PostgreSQL.
- Master complex SQL queries: Multi-table JOINs, Aggregations with `GROUP BY` / `HAVING`, CTEs (Common Table Expressions), and Window Functions (`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `LEAD`, `LAG`).
- Understand B-Tree indexing, execution plans (`EXPLAIN (ANALYZE, BUFFERS)`), and how to eliminate sequential table scans.
- Understand ACID transactions and isolation levels (`READ COMMITTED`, `REPEATABLE READ`, `SERIALIZABLE`).
- Manage schema evolutions using automated migration tools (**Flyway**).

---

## 📚 Core Topics & Knowledge Map

### 1. Schema Modeling & Constraints
```sql
CREATE TABLE customers (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id UUID NOT NULL REFERENCES customers(id) ON DELETE RESTRICT,
    total_amount NUMERIC(12, 2) NOT NULL CHECK (total_amount >= 0),
    status VARCHAR(30) NOT NULL DEFAULT 'PENDING',
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_orders_customer_created ON orders (customer_id, created_at DESC);
```

### 2. Window Functions & Analytics
```sql
-- Rank customers by monthly spend using Window Functions
SELECT 
    customer_id,
    DATE_TRUNC('month', created_at) AS order_month,
    SUM(total_amount) AS monthly_spend,
    RANK() OVER (
        PARTITION BY DATE_TRUNC('month', created_at) 
        ORDER BY SUM(total_amount) DESC
    ) AS monthly_rank
FROM orders
WHERE status = 'COMPLETED'
GROUP BY customer_id, DATE_TRUNC('month', created_at);
```

### 3. Query Profiling & Optimization
```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM orders WHERE customer_id = 'c123' ORDER BY created_at DESC LIMIT 10;
```
* Look out for: `Seq Scan` on massive tables vs `Index Scan` / `Bitmap Index Scan`.

---

## 🧪 Assigned Exercises
Navigate to [`exercises/06-sql-mastery/`](../../exercises/06-sql-mastery/):
* **`EX-06-1`**: PostgreSQL Schema Modeling (3NF & Constraints)
* **`EX-06-2`**: Advanced Joins, Aggregations & Subqueries
* **`EX-06-3`**: Window Functions, CTEs & Analytics
* **`EX-06-4`**: Indexing, EXPLAIN ANALYZE & Query Tuning
* **`EX-06-5`**: Flyway Database Migrations in Practice

---

## 🌟 Milestone 2 Checkpoint
Upon completing this stage, proceed to **[Milestone 2: Production Spring Boot 3 REST API + PostgreSQL](../../milestones/milestone-2-spring-boot-api/README.md)**.
