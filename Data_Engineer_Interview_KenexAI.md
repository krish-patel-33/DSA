# 🚀 Data Engineer Technical Interview Preparation — KenexAI

> **Interview Date:** June 12, 2026  
> **Role:** Data Engineer  
> **Company:** KenexAI

---

## 📋 TABLE OF CONTENTS — ALL TOPICS

| #  | Topic                                      | Priority   |
|----|--------------------------------------------|------------|
| 1  | SQL — Joins, Subqueries, CTEs              | 🔴 High   |
| 2  | SQL — Window Functions                     | 🔴 High   |
| 3  | SQL — Query Optimization & Indexing        | 🔴 High   |
| 4  | SQL — Stored Procedures, Views, Triggers   | 🟡 Medium |
| 5  | Python for Data Engineering                | 🔴 High   |
| 6  | Data Warehousing Concepts                  | 🔴 High   |
| 7  | Data Modeling (Star, Snowflake, 3NF)       | 🔴 High   |
| 8  | ETL vs ELT Pipelines                       | 🔴 High   |
| 9  | Apache Spark & PySpark                     | 🔴 High   |
| 10 | Hadoop Ecosystem                           | 🟡 Medium |
| 11 | Apache Kafka & Streaming                   | 🟡 Medium |
| 12 | Apache Airflow & Orchestration             | 🔴 High   |
| 13 | Cloud Data Services (AWS/Azure/GCP)        | 🔴 High   |
| 14 | Databases — RDBMS vs NoSQL                 | 🔴 High   |
| 15 | Data Quality & Data Governance             | 🟡 Medium |
| 16 | Data Partitioning & Sharding               | 🟡 Medium |
| 17 | File Formats (Parquet, Avro, ORC, JSON)    | 🟡 Medium |
| 18 | Linux & Shell Scripting Basics             | 🟢 Low    |
| 19 | Git & Version Control                      | 🟢 Low    |
| 20 | System Design for Data Pipelines           | 🔴 High   |
| 21 | Behavioral / Scenario-Based Questions      | 🟡 Medium |

---
---

# 🔥 TOPIC 1: SQL — Joins, Subqueries, CTEs

## 📖 Concepts

### Types of Joins

| Join Type        | Description                                                     |
|------------------|-----------------------------------------------------------------|
| INNER JOIN       | Returns rows with matching values in **both** tables            |
| LEFT JOIN        | Returns **all rows from left** + matched from right (NULLs if no match) |
| RIGHT JOIN       | Returns **all rows from right** + matched from left             |
| FULL OUTER JOIN  | Returns **all rows from both** tables (NULLs where no match)    |
| CROSS JOIN       | Returns **Cartesian product** (every row × every row)           |
| SELF JOIN        | A table joined with **itself**                                  |

### Subquery Types

| Type                    | Description                                          |
|-------------------------|------------------------------------------------------|
| Scalar Subquery         | Returns a **single value**                           |
| Row Subquery            | Returns a **single row**                             |
| Table Subquery          | Returns a **table** (used in FROM clause)            |
| Correlated Subquery     | References **outer query** (executes per outer row)  |
| Non-Correlated Subquery | Independent of outer query                           |

### CTE (Common Table Expression)

- Temporary named result set defined using `WITH` clause
- Improves readability over nested subqueries
- Can be **recursive** (for hierarchical data)

## ✅ Solutions & Examples

### Q1: Find employees who earn more than the average salary of their department

```sql
-- Using Correlated Subquery
SELECT e.emp_name, e.salary, e.dept_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.dept_id = e.dept_id
);

-- Using CTE (cleaner approach)
WITH dept_avg AS (
    SELECT dept_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY dept_id
)
SELECT e.emp_name, e.salary, e.dept_id, d.avg_salary
FROM employees e
JOIN dept_avg d ON e.dept_id = d.dept_id
WHERE e.salary > d.avg_salary;
```

### Q2: Find the second highest salary

```sql
-- Method 1: Using Subquery
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Method 2: Using LIMIT/OFFSET
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Method 3: Using CTE + DENSE_RANK
WITH ranked AS (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT DISTINCT salary FROM ranked WHERE rnk = 2;
```

### Q3: Find customers who placed orders but never returned anything

```sql
SELECT c.customer_id, c.customer_name
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
LEFT JOIN returns r ON o.order_id = r.order_id
WHERE r.return_id IS NULL
GROUP BY c.customer_id, c.customer_name;
```

### Q4: Recursive CTE — Find all subordinates of a manager

```sql
WITH RECURSIVE subordinates AS (
    -- Anchor: Start with the manager
    SELECT emp_id, emp_name, manager_id, 1 AS level
    FROM employees
    WHERE emp_id = 101  -- Manager ID

    UNION ALL

    -- Recursive: Find employees under each subordinate
    SELECT e.emp_id, e.emp_name, e.manager_id, s.level + 1
    FROM employees e
    INNER JOIN subordinates s ON e.manager_id = s.emp_id
)
SELECT * FROM subordinates;
```

### Q5: Find duplicate records

```sql
SELECT email, COUNT(*) AS cnt
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Delete duplicates, keeping the one with the lowest ID
DELETE FROM users
WHERE id NOT IN (
    SELECT MIN(id)
    FROM users
    GROUP BY email
);
```

---
---

# 🔥 TOPIC 2: SQL — Window Functions

## 📖 Concepts

Window functions perform calculations across a set of rows **related to the current row** without collapsing them (unlike GROUP BY).

### Syntax

```sql
function_name() OVER (
    [PARTITION BY column]
    [ORDER BY column]
    [ROWS/RANGE BETWEEN ... AND ...]
)
```

### Types of Window Functions

| Category    | Functions                                        |
|-------------|--------------------------------------------------|
| Ranking     | `ROW_NUMBER()`, `RANK()`, `DENSE_RANK()`, `NTILE()` |
| Aggregate   | `SUM()`, `AVG()`, `COUNT()`, `MIN()`, `MAX()`   |
| Value       | `LAG()`, `LEAD()`, `FIRST_VALUE()`, `LAST_VALUE()` |
| Distribution| `PERCENT_RANK()`, `CUME_DIST()`                  |

### ROW_NUMBER vs RANK vs DENSE_RANK

| Function       | Ties       | Gaps     | Example (scores: 100, 90, 90, 80) |
|----------------|------------|----------|------------------------------------|
| ROW_NUMBER()   | No ties    | No gaps  | 1, 2, 3, 4                        |
| RANK()         | Same rank  | Has gaps | 1, 2, 2, 4                        |
| DENSE_RANK()   | Same rank  | No gaps  | 1, 2, 2, 3                        |

## ✅ Solutions & Examples

### Q1: Find the top 3 highest-paid employees per department

```sql
WITH ranked_employees AS (
    SELECT
        emp_name,
        dept_id,
        salary,
        DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk
    FROM employees
)
SELECT emp_name, dept_id, salary
FROM ranked_employees
WHERE rnk <= 3;
```

### Q2: Calculate running total of sales

```sql
SELECT
    order_date,
    sales_amount,
    SUM(sales_amount) OVER (ORDER BY order_date ROWS UNBOUNDED PRECEDING) AS running_total
FROM sales;
```

### Q3: Compare each employee's salary with the previous and next employee

```sql
SELECT
    emp_name,
    salary,
    LAG(salary, 1, 0)  OVER (ORDER BY salary) AS prev_salary,
    LEAD(salary, 1, 0) OVER (ORDER BY salary) AS next_salary,
    salary - LAG(salary, 1, 0) OVER (ORDER BY salary) AS diff_from_prev
FROM employees;
```

### Q4: Calculate Month-over-Month growth rate

```sql
SELECT
    month,
    revenue,
    LAG(revenue) OVER (ORDER BY month) AS prev_month_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY month)) * 100.0
        / NULLIF(LAG(revenue) OVER (ORDER BY month), 0), 2
    ) AS mom_growth_pct
FROM monthly_sales;
```

### Q5: Moving average (3-month window)

```sql
SELECT
    month,
    revenue,
    AVG(revenue) OVER (
        ORDER BY month
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_avg_3m
FROM monthly_sales;
```

---
---

# 🔥 TOPIC 3: SQL — Query Optimization & Indexing

## 📖 Concepts

### Index Types

| Index Type          | Description                                              |
|---------------------|----------------------------------------------------------|
| B-Tree Index        | Default; good for `=`, `<`, `>`, `BETWEEN`, `ORDER BY`  |
| Hash Index          | Good for exact `=` lookups only                          |
| Bitmap Index        | Good for low-cardinality columns (e.g., gender, status)  |
| Composite Index     | Index on multiple columns; follows **leftmost prefix** rule |
| Covering Index      | Index contains all columns needed by the query           |
| Clustered Index     | Reorders the physical data; only **one per table**       |
| Non-Clustered Index | Separate structure pointing to data; **multiple allowed** |

### EXPLAIN / Execution Plan

```sql
EXPLAIN ANALYZE SELECT * FROM orders WHERE customer_id = 100;
```

- **Seq Scan** → Full table scan (slow for large tables)
- **Index Scan** → Uses an index (fast)
- **Index Only Scan** → Fully answered from index (fastest)
- **Nested Loop / Hash Join / Merge Join** → Join strategies

### Key Optimization Techniques

1. **Use indexes** on columns in `WHERE`, `JOIN`, `ORDER BY`
2. **Avoid `SELECT *`** — select only needed columns
3. **Avoid functions on indexed columns** — `WHERE YEAR(date_col) = 2025` ❌ → `WHERE date_col >= '2025-01-01'` ✅
4. **Use EXISTS instead of IN** for correlated subqueries
5. **Partition large tables** (by date, region, etc.)
6. **Use LIMIT** to reduce result set when possible
7. **Avoid DISTINCT unnecessarily** — fix the root cause (bad join)
8. **Batch INSERT/UPDATE** instead of row-by-row
9. **Denormalize for read-heavy** workloads
10. **Use materialized views** for expensive aggregations

## ✅ Solutions & Examples

### Q1: Why is this query slow? How to fix it?

```sql
-- SLOW ❌
SELECT * FROM orders WHERE YEAR(created_at) = 2025;

-- FAST ✅ (sargable — uses index)
SELECT order_id, customer_id, total
FROM orders
WHERE created_at >= '2025-01-01' AND created_at < '2026-01-01';

-- Create an index
CREATE INDEX idx_orders_created_at ON orders(created_at);
```

### Q2: EXISTS vs IN performance

```sql
-- IN (loads entire subquery result into memory)
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);

-- EXISTS (stops at first match — better for large subqueries)
SELECT * FROM customers c
WHERE EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);
```

### Q3: Composite Index — Leftmost Prefix Rule

```sql
-- Index on (dept_id, salary, hire_date)
CREATE INDEX idx_dept_sal_date ON employees(dept_id, salary, hire_date);

-- ✅ Uses index (leftmost prefix)
SELECT * FROM employees WHERE dept_id = 10;
SELECT * FROM employees WHERE dept_id = 10 AND salary > 50000;
SELECT * FROM employees WHERE dept_id = 10 AND salary > 50000 AND hire_date > '2023-01-01';

-- ❌ Does NOT use index (skips dept_id)
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM employees WHERE hire_date > '2023-01-01';
```

---
---

# 🔥 TOPIC 4: SQL — Stored Procedures, Views, Triggers

## 📖 Concepts

| Feature             | Description                                                        |
|---------------------|--------------------------------------------------------------------|
| **View**            | Virtual table based on a query; no data stored                     |
| **Materialized View** | Pre-computed, stored results; needs manual refresh              |
| **Stored Procedure** | Reusable SQL program; can accept parameters, use control flow    |
| **Function (UDF)**  | Returns a value; can be used in SELECT/WHERE                       |
| **Trigger**         | Auto-executes on INSERT/UPDATE/DELETE events                       |
| **Cursor**          | Row-by-row processing (generally avoid — use set-based ops)        |

## ✅ Solutions & Examples

### View vs Materialized View

```sql
-- Regular View (always runs the underlying query)
CREATE VIEW active_customers AS
SELECT customer_id, name, email
FROM customers
WHERE status = 'active';

-- Materialized View (stores results; faster reads)
CREATE MATERIALIZED VIEW monthly_sales_summary AS
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY DATE_TRUNC('month', order_date);

-- Refresh when data changes
REFRESH MATERIALIZED VIEW monthly_sales_summary;
```

### Stored Procedure Example

```sql
CREATE PROCEDURE update_salary(
    IN emp_id INT,
    IN increase_pct DECIMAL
)
BEGIN
    UPDATE employees
    SET salary = salary * (1 + increase_pct / 100)
    WHERE id = emp_id;
END;

-- Call
CALL update_salary(101, 10);
```

### Trigger Example

```sql
CREATE TRIGGER log_salary_change
AFTER UPDATE ON employees
FOR EACH ROW
BEGIN
    IF OLD.salary <> NEW.salary THEN
        INSERT INTO salary_audit(emp_id, old_salary, new_salary, changed_at)
        VALUES (OLD.id, OLD.salary, NEW.salary, NOW());
    END IF;
END;
```

---
---

# 🔥 TOPIC 5: Python for Data Engineering

## 📖 Concepts

### Key Libraries

| Library        | Purpose                                          |
|----------------|--------------------------------------------------|
| `pandas`       | Data manipulation & analysis (DataFrames)        |
| `numpy`        | Numerical computing                              |
| `pyspark`      | Distributed data processing                      |
| `sqlalchemy`   | Database ORM & connection management             |
| `boto3`        | AWS SDK for Python                               |
| `requests`     | HTTP requests (API integration)                  |
| `json`         | JSON parsing & generation                        |
| `logging`      | Application logging                              |
| `unittest`     | Unit testing framework                           |
| `datetime`     | Date/time manipulation                           |

### Core Python Concepts for DE

- **List Comprehensions** — concise data transformations
- **Generators** — memory-efficient iteration for large datasets
- **Decorators** — add functionality (logging, retry logic)
- **Context Managers** — safe resource handling (`with` statement)
- **Exception Handling** — robust error management in pipelines
- **OOP** — reusable pipeline components

## ✅ Solutions & Examples

### Q1: Read CSV, clean, and write to database

```python
import pandas as pd
from sqlalchemy import create_engine

# Read
df = pd.read_csv('sales_data.csv')

# Clean
df.dropna(subset=['customer_id', 'amount'], inplace=True)
df['amount'] = df['amount'].astype(float)
df['order_date'] = pd.to_datetime(df['order_date'])
df.drop_duplicates(subset=['order_id'], inplace=True)

# Load to DB
engine = create_engine('postgresql://user:pass@localhost:5432/mydb')
df.to_sql('clean_sales', engine, if_exists='replace', index=False)
```

### Q2: Generator for processing large files (memory-efficient)

```python
def read_large_file(filepath, chunk_size=10000):
    """Yield chunks of rows from a large CSV."""
    for chunk in pd.read_csv(filepath, chunksize=chunk_size):
        # Process each chunk
        chunk = chunk[chunk['status'] == 'completed']
        yield chunk

# Usage — never loads full file into memory
for chunk in read_large_file('huge_file.csv'):
    chunk.to_sql('processed_data', engine, if_exists='append', index=False)
```

### Q3: Decorator for retry logic in API calls

```python
import time
import functools

def retry(max_retries=3, delay=2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_retries:
                        raise
                    time.sleep(delay * attempt)  # Exponential backoff
        return wrapper
    return decorator

@retry(max_retries=3, delay=2)
def fetch_api_data(url):
    import requests
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
```

### Q4: Context Manager for database connections

```python
from contextlib import contextmanager
import psycopg2

@contextmanager
def db_connection(db_config):
    conn = None
    try:
        conn = psycopg2.connect(**db_config)
        yield conn
        conn.commit()
    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if conn:
            conn.close()

# Usage
with db_connection({'host': 'localhost', 'dbname': 'mydb'}) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT 10")
    rows = cursor.fetchall()
```

### Q5: Dictionary & List Comprehensions for data transformation

```python
# Flatten nested JSON
raw_data = [
    {"id": 1, "info": {"name": "Alice", "age": 30}},
    {"id": 2, "info": {"name": "Bob", "age": 25}},
]

flat_data = [
    {"id": d["id"], "name": d["info"]["name"], "age": d["info"]["age"]}
    for d in raw_data
]

# Group by key
from collections import defaultdict

orders = [
    {"customer": "A", "amount": 100},
    {"customer": "B", "amount": 200},
    {"customer": "A", "amount": 150},
]

grouped = defaultdict(list)
for order in orders:
    grouped[order["customer"]].append(order["amount"])

# {'A': [100, 150], 'B': [200]}
totals = {k: sum(v) for k, v in grouped.items()}
# {'A': 250, 'B': 200}
```

---
---

# 🔥 TOPIC 6: Data Warehousing Concepts

## 📖 Concepts

### What is a Data Warehouse?

A centralized repository for **structured, historical data** optimized for **analytical queries** (OLAP).

### OLTP vs OLAP

| Feature        | OLTP                        | OLAP                            |
|----------------|-----------------------------|---------------------------------|
| Purpose        | Day-to-day transactions     | Analytical reporting            |
| Queries        | Simple, short               | Complex, aggregations           |
| Data           | Current, real-time          | Historical, consolidated        |
| Normalization  | Highly normalized (3NF)     | Denormalized (Star/Snowflake)   |
| Users          | Thousands (app users)       | Fewer (analysts, managers)      |
| Examples       | MySQL, PostgreSQL           | Redshift, BigQuery, Snowflake   |

### Data Warehouse Architecture

```
Source Systems → ETL/ELT → Staging → Data Warehouse → Data Marts → BI Tools
                                          ↓
                                    (Fact + Dimension Tables)
```

### Key Terms

| Term               | Definition                                                          |
|--------------------|---------------------------------------------------------------------|
| **Fact Table**      | Stores measurable events/metrics (e.g., sales_amount, quantity)    |
| **Dimension Table** | Stores descriptive attributes (e.g., customer_name, product_type) |
| **Grain**           | The lowest level of detail in a fact table                         |
| **Data Mart**       | Subset of warehouse for a specific department                      |
| **Data Lake**       | Raw, unstructured/semi-structured data storage                     |
| **Data Lakehouse**  | Combines lake + warehouse (Delta Lake, Iceberg)                    |
| **Slowly Changing Dimensions (SCD)** | How dimension data changes over time           |

### SCD Types

| Type   | Strategy                                                            | Example                    |
|--------|---------------------------------------------------------------------|----------------------------|
| Type 0 | No changes allowed                                                  | Original value preserved   |
| Type 1 | Overwrite old value                                                 | Update in place            |
| Type 2 | Add new row with version/date range (most common)                  | History preserved          |
| Type 3 | Add new column for old value                                        | Limited history            |

## ✅ Solutions & Examples

### SCD Type 2 Implementation

```sql
-- Dimension table with SCD Type 2
CREATE TABLE dim_customer (
    customer_sk    INT PRIMARY KEY,     -- Surrogate Key
    customer_id    INT,                 -- Natural/Business Key
    customer_name  VARCHAR(100),
    city           VARCHAR(50),
    is_current     BOOLEAN DEFAULT TRUE,
    effective_date DATE,
    expiry_date    DATE DEFAULT '9999-12-31'
);

-- When a customer moves to a new city:
-- Step 1: Expire the old record
UPDATE dim_customer
SET is_current = FALSE, expiry_date = CURRENT_DATE - 1
WHERE customer_id = 1001 AND is_current = TRUE;

-- Step 2: Insert the new record
INSERT INTO dim_customer (customer_sk, customer_id, customer_name, city, is_current, effective_date)
VALUES (NEXT_SK, 1001, 'Alice', 'New York', TRUE, CURRENT_DATE);
```

### Data Lake vs Data Warehouse vs Data Lakehouse

```
┌─────────────────┬──────────────────┬─────────────────┬─────────────────────┐
│ Feature         │ Data Lake        │ Data Warehouse  │ Data Lakehouse      │
├─────────────────┼──────────────────┼─────────────────┼─────────────────────┤
│ Data Format     │ Raw (any format) │ Structured only │ Both                │
│ Schema          │ Schema-on-read   │ Schema-on-write │ Both                │
│ Processing      │ ELT              │ ETL             │ Both                │
│ Cost            │ Low storage      │ High            │ Medium              │
│ ACID            │ Limited          │ Full            │ Supported           │
│ Examples        │ S3, ADLS, GCS    │ Redshift, BQ    │ Delta Lake, Iceberg │
└─────────────────┴──────────────────┴─────────────────┴─────────────────────┘
```

---
---

# 🔥 TOPIC 7: Data Modeling (Star, Snowflake, 3NF)

## 📖 Concepts

### Normalization Forms

| Form | Rule                                                     | Example                         |
|------|----------------------------------------------------------|---------------------------------|
| 1NF  | No repeating groups; atomic values                       | Split multi-value cells         |
| 2NF  | 1NF + no partial dependencies                           | Remove columns dependent on part of a composite key |
| 3NF  | 2NF + no transitive dependencies                        | Remove columns dependent on non-key columns         |
| BCNF | Every determinant is a candidate key                     | Stricter 3NF                    |

### Star Schema vs Snowflake Schema

| Feature         | Star Schema                    | Snowflake Schema                  |
|-----------------|--------------------------------|-----------------------------------|
| Structure       | Fact table + denormalized dims | Fact table + normalized dims      |
| Query Speed     | Faster (fewer joins)           | Slower (more joins)               |
| Storage         | More (redundancy)              | Less (no redundancy)              |
| Complexity      | Simple                         | Complex                           |
| Maintenance     | Easier                         | Harder                            |
| Best For        | BI/reporting                   | Complex hierarchical data         |

## ✅ Solutions & Examples

### Star Schema Design — E-Commerce

```sql
-- FACT TABLE
CREATE TABLE fact_sales (
    sale_id         INT PRIMARY KEY,
    date_key        INT REFERENCES dim_date(date_key),
    product_key     INT REFERENCES dim_product(product_key),
    customer_key    INT REFERENCES dim_customer(customer_key),
    store_key       INT REFERENCES dim_store(store_key),
    quantity_sold   INT,
    unit_price      DECIMAL(10,2),
    total_amount    DECIMAL(12,2),
    discount_amount DECIMAL(10,2)
);

-- DIMENSION: Date
CREATE TABLE dim_date (
    date_key     INT PRIMARY KEY,
    full_date    DATE,
    day_of_week  VARCHAR(10),
    month_name   VARCHAR(15),
    quarter      INT,
    year         INT,
    is_weekend   BOOLEAN,
    is_holiday   BOOLEAN
);

-- DIMENSION: Product
CREATE TABLE dim_product (
    product_key    INT PRIMARY KEY,
    product_name   VARCHAR(100),
    category       VARCHAR(50),
    sub_category   VARCHAR(50),
    brand          VARCHAR(50),
    unit_cost      DECIMAL(10,2)
);

-- DIMENSION: Customer
CREATE TABLE dim_customer (
    customer_key   INT PRIMARY KEY,
    customer_name  VARCHAR(100),
    email          VARCHAR(100),
    city           VARCHAR(50),
    state          VARCHAR(50),
    country        VARCHAR(50),
    segment        VARCHAR(30)  -- 'Consumer', 'Corporate', etc.
);
```

### Sample Analytical Query on Star Schema

```sql
-- Monthly revenue by product category for 2025
SELECT
    d.month_name,
    p.category,
    SUM(f.total_amount) AS total_revenue,
    COUNT(f.sale_id) AS num_transactions,
    AVG(f.total_amount) AS avg_order_value
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
JOIN dim_product p ON f.product_key = p.product_key
WHERE d.year = 2025
GROUP BY d.month_name, p.category
ORDER BY total_revenue DESC;
```

---
---

# 🔥 TOPIC 8: ETL vs ELT Pipelines

## 📖 Concepts

### ETL vs ELT

| Feature        | ETL (Extract-Transform-Load)         | ELT (Extract-Load-Transform)           |
|----------------|--------------------------------------|----------------------------------------|
| Transform      | Before loading (on ETL server)       | After loading (in the target system)   |
| Best For       | On-prem data warehouses              | Cloud data warehouses                  |
| Speed          | Slower (separate transform step)     | Faster (leverage warehouse compute)    |
| Data Volume    | Small to Medium                      | Large to Very Large                    |
| Tools          | Informatica, Talend, SSIS            | dbt, Snowflake, BigQuery               |
| Flexibility    | Transform logic fixed before load    | Can re-transform raw data anytime      |

### ETL Pipeline Steps

```
1. EXTRACT: Pull data from sources (APIs, DBs, files, streams)
2. TRANSFORM: Clean, validate, aggregate, enrich, conform
3. LOAD: Write to target (data warehouse, data mart)
```

### Common Transformations

- **Data Cleaning** — handle NULLs, duplicates, outliers
- **Type Casting** — convert data types
- **Deduplication** — remove duplicate records
- **Joining/Enriching** — combine data from multiple sources
- **Aggregation** — summarize data (SUM, AVG, COUNT)
- **Filtering** — remove irrelevant records
- **Conforming** — standardize formats (dates, currencies)

## ✅ Solutions & Examples

### Python ETL Pipeline Example

```python
import pandas as pd
from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SalesETLPipeline:
    def __init__(self, source_path, target_db_url):
        self.source_path = source_path
        self.engine = create_engine(target_db_url)

    def extract(self):
        """Extract data from CSV source."""
        logger.info("Extracting data...")
        df = pd.read_csv(self.source_path)
        logger.info(f"Extracted {len(df)} rows")
        return df

    def transform(self, df):
        """Clean and transform the data."""
        logger.info("Transforming data...")

        # Remove duplicates
        df = df.drop_duplicates(subset=['order_id'])

        # Handle nulls
        df['customer_name'] = df['customer_name'].fillna('Unknown')
        df = df.dropna(subset=['amount'])

        # Type casting
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['amount'] = df['amount'].astype(float)

        # Derived columns
        df['order_month'] = df['order_date'].dt.to_period('M')
        df['amount_category'] = pd.cut(
            df['amount'],
            bins=[0, 100, 500, float('inf')],
            labels=['Small', 'Medium', 'Large']
        )

        logger.info(f"Transformed to {len(df)} rows")
        return df

    def load(self, df):
        """Load to target database."""
        logger.info("Loading data...")
        df.to_sql('fact_sales', self.engine, if_exists='append', index=False)
        logger.info(f"Loaded {len(df)} rows to fact_sales")

    def run(self):
        """Execute full ETL pipeline."""
        try:
            raw_data = self.extract()
            clean_data = self.transform(raw_data)
            self.load(clean_data)
            logger.info("ETL pipeline completed successfully!")
        except Exception as e:
            logger.error(f"ETL pipeline failed: {e}")
            raise

# Execute
pipeline = SalesETLPipeline('sales.csv', 'postgresql://user:pass@localhost/warehouse')
pipeline.run()
```

### dbt (Data Build Tool) — ELT Transform Example

```sql
-- models/staging/stg_orders.sql
WITH source AS (
    SELECT * FROM {{ source('raw', 'orders') }}
),
cleaned AS (
    SELECT
        order_id,
        customer_id,
        CAST(order_date AS DATE) AS order_date,
        CAST(amount AS DECIMAL(10,2)) AS amount,
        LOWER(TRIM(status)) AS status
    FROM source
    WHERE order_id IS NOT NULL
)
SELECT * FROM cleaned
```

---
---

# 🔥 TOPIC 9: Apache Spark & PySpark

## 📖 Concepts

### What is Apache Spark?

- **Distributed computing engine** for big data processing
- **100x faster** than Hadoop MapReduce (in-memory processing)
- Supports **batch** and **stream** processing
- APIs: Scala, Python (PySpark), Java, R, SQL

### Spark Architecture

```
Driver Program
    ↓
SparkContext / SparkSession
    ↓
Cluster Manager (YARN / Mesos / K8s / Standalone)
    ↓
Worker Nodes → Executors → Tasks
```

### Key Concepts

| Concept              | Description                                                     |
|----------------------|-----------------------------------------------------------------|
| **RDD**              | Resilient Distributed Dataset — immutable, partitioned collection |
| **DataFrame**        | Distributed table with named columns (like pandas)              |
| **Dataset**          | Typed DataFrame (Scala/Java only)                               |
| **Transformation**   | Lazy operation (map, filter, groupBy) — builds a DAG            |
| **Action**           | Triggers execution (count, collect, show, write)                |
| **Partition**        | Unit of parallelism; data split across workers                  |
| **Shuffle**          | Data redistribution across partitions (expensive)               |
| **Catalyst Optimizer** | Query optimization engine for Spark SQL                       |
| **Tungsten**         | Memory management & code generation engine                      |

### Transformations vs Actions

| Transformations (Lazy)           | Actions (Triggers Execution)     |
|----------------------------------|----------------------------------|
| `select()`, `filter()`, `where()`| `show()`, `collect()`            |
| `groupBy()`, `agg()`            | `count()`, `first()`             |
| `join()`, `union()`             | `write()`, `save()`              |
| `withColumn()`, `drop()`        | `take(n)`, `toPandas()`          |

## ✅ Solutions & Examples

### Q1: Basic PySpark DataFrame operations

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, count, when, lit, year

# Initialize Spark
spark = SparkSession.builder \
    .appName("DataEngineerInterview") \
    .config("spark.sql.adaptive.enabled", "true") \
    .getOrCreate()

# Read data
df = spark.read.csv("s3://bucket/sales_data.csv", header=True, inferSchema=True)

# Basic operations
df.printSchema()
df.show(5)

# Filter
active_orders = df.filter(
    (col("status") == "completed") & (col("amount") > 100)
)

# Add columns
df_enriched = df.withColumn(
    "order_year", year(col("order_date"))
).withColumn(
    "size_category",
    when(col("amount") > 1000, "Large")
    .when(col("amount") > 100, "Medium")
    .otherwise("Small")
)

# Aggregation
summary = df.groupBy("product_category").agg(
    count("*").alias("total_orders"),
    sum("amount").alias("total_revenue"),
    avg("amount").alias("avg_order_value")
).orderBy(col("total_revenue").desc())

summary.show()
```

### Q2: PySpark — Joins and handling skew

```python
# Regular join
result = orders_df.join(
    customers_df,
    orders_df.customer_id == customers_df.customer_id,
    "left"
).select(
    orders_df["order_id"],
    customers_df["customer_name"],
    orders_df["amount"]
)

# Broadcast join (for small dimension tables)
from pyspark.sql.functions import broadcast

result = orders_df.join(
    broadcast(dim_product_df),  # Broadcasts small table to all nodes
    "product_id"
)

# Handling data skew with salting
from pyspark.sql.functions import rand, floor, concat

# Add salt to the skewed key
salted_orders = orders_df.withColumn(
    "salt", floor(rand() * 10).cast("int")
).withColumn(
    "salted_key", concat(col("customer_id"), lit("_"), col("salt"))
)
```

### Q3: PySpark — Window functions

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, dense_rank, lag

# Define window
window_spec = Window.partitionBy("department").orderBy(col("salary").desc())

# Add ranking
df_ranked = df.withColumn("rank", dense_rank().over(window_spec))

# Top 3 per department
top_3 = df_ranked.filter(col("rank") <= 3)

# Running total
running_window = Window.partitionBy("department").orderBy("hire_date").rowsBetween(
    Window.unboundedPreceding, Window.currentRow
)
df_running = df.withColumn("running_salary_total", sum("salary").over(running_window))
```

### Q4: Write data with partitioning

```python
# Write as Parquet with partitioning
df.write \
    .mode("overwrite") \
    .partitionBy("year", "month") \
    .parquet("s3://bucket/processed/sales/")

# Write to Delta table
df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("warehouse.fact_sales")
```

### Spark Optimization Tips

| Technique                 | When to Use                              |
|---------------------------|------------------------------------------|
| `broadcast()` join        | One table < 10MB                         |
| `repartition(n)`         | Before wide transformations              |
| `coalesce(n)`            | Reduce partitions before writing         |
| `cache()` / `persist()`  | Reused DataFrames                        |
| Avoid UDFs               | Use built-in functions (Catalyst-optimized) |
| Adaptive Query Execution | Enable `spark.sql.adaptive.enabled=true` |
| Predicate pushdown       | Filter early in the pipeline             |

---
---

# 🔥 TOPIC 10: Hadoop Ecosystem

## 📖 Concepts

### Core Components

| Component      | Purpose                                              |
|----------------|------------------------------------------------------|
| **HDFS**       | Distributed file system (stores data across nodes)   |
| **MapReduce**  | Batch processing framework (largely replaced by Spark) |
| **YARN**       | Resource management & job scheduling                 |
| **Hive**       | SQL interface on top of Hadoop                       |
| **HBase**      | NoSQL columnar database on HDFS                      |
| **Pig**        | Data flow scripting language                         |
| **Sqoop**      | Data transfer between Hadoop and RDBMS               |
| **Flume**      | Log data ingestion                                   |
| **Oozie**      | Workflow scheduler for Hadoop jobs                   |
| **Zookeeper**  | Coordination service                                 |

### HDFS Architecture

```
NameNode (Master)
  ├── Manages metadata (file names, block locations, permissions)
  ├── Single point of contact for clients
  └── High Availability via Standby NameNode

DataNodes (Workers)
  ├── Store actual data blocks
  ├── Default block size: 128 MB
  └── Replication factor: 3 (configurable)
```

### MapReduce Flow

```
Input → Split → Map (parallel) → Shuffle & Sort → Reduce → Output
```

### Hive vs Traditional RDBMS

| Feature        | Hive                           | RDBMS                     |
|----------------|--------------------------------|---------------------------|
| Data size      | Petabytes                      | Terabytes                 |
| Schema         | Schema-on-read                 | Schema-on-write           |
| Latency        | High (batch)                   | Low (real-time)           |
| Updates        | Limited (append-mostly)        | Full CRUD                 |
| Best for       | Data warehousing on Hadoop     | OLTP transactions         |

---
---

# 🔥 TOPIC 11: Apache Kafka & Streaming

## 📖 Concepts

### What is Kafka?

A **distributed event streaming platform** for real-time data pipelines and stream processing.

### Kafka Architecture

```
Producers → Topics (Partitions) → Brokers (Cluster) → Consumers (Consumer Groups)
```

| Component          | Description                                           |
|--------------------|-------------------------------------------------------|
| **Producer**       | Publishes messages to topics                          |
| **Consumer**       | Reads messages from topics                            |
| **Topic**          | Category/channel for messages                         |
| **Partition**      | Ordered, immutable log within a topic                 |
| **Broker**         | Kafka server that stores partitions                   |
| **Consumer Group** | Multiple consumers sharing load of a topic            |
| **Offset**         | Position of a message within a partition              |
| **Zookeeper**      | Manages broker metadata (being replaced by KRaft)     |

### Key Guarantees

| Guarantee       | Description                                              |
|-----------------|----------------------------------------------------------|
| At-most-once    | Messages may be lost, never duplicated                   |
| At-least-once   | Messages never lost, may be duplicated                   |
| Exactly-once    | Messages delivered exactly once (Kafka Transactions)     |

### Batch vs Stream Processing

| Feature       | Batch                          | Stream                        |
|---------------|--------------------------------|-------------------------------|
| Data          | Bounded (finite)               | Unbounded (infinite)          |
| Latency       | Minutes to hours               | Milliseconds to seconds       |
| Processing    | Entire dataset at once         | Event-by-event or micro-batch |
| Tools         | Spark Batch, Hive              | Kafka Streams, Flink, Spark Structured Streaming |

## ✅ Solutions & Examples

### Kafka Producer (Python)

```python
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send messages
for i in range(100):
    message = {"order_id": i, "amount": round(i * 10.5, 2), "status": "new"}
    producer.send('orders_topic', value=message)

producer.flush()
producer.close()
```

### Kafka Consumer (Python)

```python
from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'orders_topic',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    group_id='order_processing_group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

for message in consumer:
    order = message.value
    print(f"Partition: {message.partition}, Offset: {message.offset}, Order: {order}")
    # Process the order...
```

### Spark Structured Streaming + Kafka

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("KafkaStream").getOrCreate()

schema = StructType() \
    .add("order_id", StringType()) \
    .add("amount", DoubleType()) \
    .add("status", StringType())

# Read from Kafka
stream_df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "orders_topic") \
    .load()

# Parse JSON
parsed_df = stream_df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Write to console (or sink)
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
```

---
---

# 🔥 TOPIC 12: Apache Airflow & Orchestration

## 📖 Concepts

### What is Airflow?

- **Workflow orchestration platform** to author, schedule, and monitor data pipelines
- Pipelines defined as **DAGs** (Directed Acyclic Graphs) in Python
- Created by **Airbnb**, now Apache project

### Key Concepts

| Concept          | Description                                             |
|------------------|---------------------------------------------------------|
| **DAG**          | Collection of tasks with dependencies                   |
| **Task**         | Single unit of work (an operator instance)              |
| **Operator**     | Template for a task (PythonOperator, BashOperator, etc.)|
| **Sensor**       | Waits for a condition to be met (FileSensor, etc.)      |
| **XCom**         | Cross-communication between tasks                       |
| **Hook**         | Interface to external systems (DB, S3, etc.)            |
| **Connection**   | Stored credentials for external systems                 |
| **Variable**     | Global config values accessible in DAGs                 |
| **Executor**     | How tasks are run (Local, Celery, Kubernetes)            |
| **Schedule**     | Cron expression defining when DAG runs                  |
| **Backfill**     | Re-run historical DAG runs                              |

### Common Operators

| Operator                | Purpose                              |
|-------------------------|--------------------------------------|
| `PythonOperator`        | Run Python functions                 |
| `BashOperator`          | Run bash commands                    |
| `PostgresOperator`      | Execute SQL on PostgreSQL            |
| `S3ToRedshiftOperator`  | Load S3 data to Redshift             |
| `EmailOperator`         | Send emails                          |
| `DummyOperator`         | No-op placeholder for branching      |
| `BranchPythonOperator`  | Conditional branching                |

## ✅ Solutions & Examples

### Complete Airflow DAG — Daily ETL Pipeline

```python
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta

default_args = {
    'owner': 'data_engineering',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'email_on_failure': True,
    'email': ['de-team@company.com'],
}

dag = DAG(
    'daily_sales_etl',
    default_args=default_args,
    description='Daily ETL for sales data',
    schedule_interval='0 6 * * *',  # Daily at 6 AM
    catchup=False,
    tags=['production', 'etl', 'sales'],
)

def extract_data(**context):
    # Extract logic
    import pandas as pd
    df = pd.read_csv('/data/raw/sales.csv')
    context['ti'].xcom_push(key='row_count', value=len(df))
    return '/data/staging/sales_extracted.csv'

def transform_data(**context):
    row_count = context['ti'].xcom_pull(key='row_count', task_ids='extract')
    # Transform logic
    print(f"Transforming {row_count} rows...")

def check_data_quality(**context):
    # Data quality checks
    pass

# Define tasks
wait_for_file = FileSensor(
    task_id='wait_for_file',
    filepath='/data/raw/sales.csv',
    poke_interval=300,
    timeout=3600,
    dag=dag,
)

extract = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag,
)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag,
)

quality_check = PythonOperator(
    task_id='quality_check',
    python_callable=check_data_quality,
    dag=dag,
)

load = PostgresOperator(
    task_id='load_to_warehouse',
    postgres_conn_id='warehouse_conn',
    sql='sql/load_sales.sql',
    dag=dag,
)

# Define dependencies
wait_for_file >> extract >> transform >> quality_check >> load
```

---
---

# 🔥 TOPIC 13: Cloud Data Services (AWS / Azure / GCP)

## 📖 Concepts

### AWS Data Services

| Service            | Purpose                                      |
|--------------------|----------------------------------------------|
| **S3**             | Object storage (data lake foundation)        |
| **Redshift**       | Cloud data warehouse                         |
| **Glue**           | Serverless ETL + Data Catalog                |
| **Athena**         | Serverless SQL on S3                         |
| **Kinesis**        | Real-time data streaming                     |
| **EMR**            | Managed Hadoop/Spark clusters                |
| **RDS**            | Managed relational databases                 |
| **DynamoDB**       | Managed NoSQL database                       |
| **Lambda**         | Serverless compute (event-driven processing) |
| **Step Functions** | Workflow orchestration                       |

### Azure Data Services

| Service                 | Purpose                                |
|-------------------------|----------------------------------------|
| **Azure Data Lake (ADLS)** | Data lake storage                   |
| **Azure Synapse**       | Data warehouse + analytics platform    |
| **Azure Data Factory**  | ETL / data integration                 |
| **Azure Databricks**    | Managed Spark platform                 |
| **Azure Event Hubs**    | Real-time event streaming              |
| **Cosmos DB**           | Multi-model NoSQL database             |
| **Azure SQL Database**  | Managed SQL Server                     |

### GCP Data Services

| Service            | Purpose                                      |
|--------------------|----------------------------------------------|
| **BigQuery**       | Serverless data warehouse                    |
| **Cloud Storage**  | Object storage                               |
| **Dataflow**       | Stream & batch processing (Apache Beam)      |
| **Dataproc**       | Managed Hadoop/Spark                         |
| **Pub/Sub**        | Real-time messaging                          |
| **Cloud Composer** | Managed Apache Airflow                       |
| **Firestore**      | NoSQL document database                      |

### AWS vs Azure vs GCP — Equivalent Services

| Category        | AWS              | Azure                | GCP              |
|-----------------|------------------|----------------------|------------------|
| Object Storage  | S3               | ADLS / Blob Storage  | Cloud Storage    |
| Data Warehouse  | Redshift         | Synapse              | BigQuery         |
| ETL             | Glue             | Data Factory         | Dataflow         |
| Spark           | EMR              | Databricks / HDInsight | Dataproc       |
| Streaming       | Kinesis          | Event Hubs           | Pub/Sub          |
| Serverless SQL  | Athena           | Synapse Serverless   | BigQuery         |
| NoSQL           | DynamoDB         | Cosmos DB            | Firestore/Bigtable |
| Orchestration   | Step Functions   | Data Factory         | Cloud Composer   |

---
---

# 🔥 TOPIC 14: Databases — RDBMS vs NoSQL

## 📖 Concepts

### RDBMS (Relational)

| Feature        | Description                                         |
|----------------|-----------------------------------------------------|
| Structure      | Tables with rows and columns                        |
| Schema         | Fixed, predefined schema                            |
| ACID           | Full ACID compliance                                |
| Query Language | SQL                                                 |
| Scaling        | Vertical (scale up)                                 |
| Best For       | Structured data, complex queries, transactions      |
| Examples       | PostgreSQL, MySQL, SQL Server, Oracle               |

### NoSQL Types

| Type           | Structure                | Examples                | Best For                        |
|----------------|--------------------------|-------------------------|---------------------------------|
| Document       | JSON-like documents      | MongoDB, Couchbase      | Semi-structured, flexible schema |
| Key-Value      | Simple key→value pairs   | Redis, DynamoDB         | Caching, sessions, fast lookups  |
| Column-Family  | Column-oriented storage  | Cassandra, HBase        | Time-series, IoT, write-heavy   |
| Graph          | Nodes & edges            | Neo4j, Amazon Neptune   | Social networks, recommendations |

### ACID vs BASE

| Property  | ACID (RDBMS)                     | BASE (NoSQL)                      |
|-----------|----------------------------------|-----------------------------------|
| A         | Atomicity                        | Basically Available               |
| C         | Consistency                      | Soft state                        |
| I/E       | Isolation                        | Eventually consistent             |
| D         | Durability                       |                                   |

### CAP Theorem

> A distributed system can only guarantee **two of three** properties:

| Property      | Description                              |
|---------------|------------------------------------------|
| Consistency   | All nodes see the same data              |
| Availability  | Every request gets a response            |
| Partition Tolerance | System works despite network failures |

```
       Consistency
         /     \
        /       \
      CP         CA
     (HBase)    (RDBMS - not distributed)
      /           \
Partition    Availability
Tolerance       /
     \         /
       \      /
         AP
     (Cassandra, DynamoDB)
```

## ✅ Solutions & Examples

### When to use what?

| Scenario                              | Choose              | Why?                              |
|---------------------------------------|---------------------|-----------------------------------|
| Banking transactions                  | RDBMS (PostgreSQL)  | ACID compliance critical          |
| User session storage                  | Redis (Key-Value)   | Fast, simple lookups              |
| Product catalog (varying attributes)  | MongoDB (Document)  | Flexible schema                   |
| Social network connections            | Neo4j (Graph)       | Relationship-heavy queries        |
| IoT sensor data (billions of writes)  | Cassandra (Column)  | High write throughput             |
| E-commerce data warehouse             | RDBMS + Star Schema | Complex analytics queries         |

---
---

# 🔥 TOPIC 15: Data Quality & Data Governance

## 📖 Concepts

### Data Quality Dimensions

| Dimension      | Description                                        | Example Check                    |
|----------------|----------------------------------------------------|----------------------------------|
| Completeness   | No missing critical data                           | `WHERE column IS NOT NULL`       |
| Accuracy       | Data reflects real-world values                    | Age between 0-120                |
| Consistency    | Same data across systems                           | Customer name matches in all DBs |
| Timeliness     | Data is current and up-to-date                     | Latest refresh < 24 hours ago    |
| Uniqueness     | No duplicate records                               | Unique constraint on primary key |
| Validity       | Data conforms to rules/formats                     | Email matches regex pattern      |

### Data Governance Pillars

| Pillar             | Description                                       |
|--------------------|---------------------------------------------------|
| Data Catalog       | Metadata management (what data exists, where)     |
| Data Lineage       | Track data origin → transformations → consumption |
| Data Classification | Label data sensitivity (PII, confidential, public)|
| Access Control     | Who can read/write what data                      |
| Data Retention     | How long to keep data, archival policies          |
| Compliance         | GDPR, HIPAA, SOC2 adherence                       |

### Data Quality Tools

| Tool                     | Type                    |
|--------------------------|-------------------------|
| Great Expectations       | Python-based DQ testing |
| dbt Tests                | SQL-based assertions    |
| Apache Griffin           | Open-source DQ platform |
| AWS Deequ                | Spark-based DQ library  |
| Monte Carlo / Soda       | Data observability      |

## ✅ Solutions & Examples

### Data Quality Checks in SQL

```sql
-- 1. Completeness: Check for NULLs
SELECT
    COUNT(*) AS total_rows,
    COUNT(customer_id) AS non_null_customer_id,
    COUNT(*) - COUNT(customer_id) AS null_count,
    ROUND(COUNT(customer_id) * 100.0 / COUNT(*), 2) AS completeness_pct
FROM orders;

-- 2. Uniqueness: Find duplicates
SELECT order_id, COUNT(*)
FROM orders
GROUP BY order_id
HAVING COUNT(*) > 1;

-- 3. Validity: Check data ranges
SELECT COUNT(*)
FROM employees
WHERE age < 0 OR age > 120;

-- 4. Freshness: Check latest data timestamp
SELECT MAX(updated_at) AS last_update,
       CURRENT_TIMESTAMP - MAX(updated_at) AS staleness
FROM fact_sales;

-- 5. Referential integrity
SELECT o.customer_id
FROM orders o
LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
```

### Great Expectations Example (Python)

```python
import great_expectations as gx

context = gx.get_context()

# Define expectations
validator = context.sources.pandas_default.read_csv("sales.csv")

validator.expect_column_values_to_not_be_null("customer_id")
validator.expect_column_values_to_be_between("amount", min_value=0, max_value=1000000)
validator.expect_column_values_to_be_unique("order_id")
validator.expect_column_values_to_match_regex("email", r"^[\w.+-]+@[\w-]+\.[\w.]+$")

results = validator.validate()
print(f"Success: {results.success}")
```

---
---

# 🔥 TOPIC 16: Data Partitioning & Sharding

## 📖 Concepts

### Partitioning (within a single database)

| Type                | Description                                          | Example                     |
|---------------------|------------------------------------------------------|-----------------------------|
| **Range Partitioning**  | Rows split by value range                        | By date: Jan, Feb, Mar...   |
| **List Partitioning**   | Rows split by discrete values                    | By region: US, EU, APAC     |
| **Hash Partitioning**   | Rows distributed by hash function                | hash(user_id) % num_parts   |

### Sharding (across multiple databases/servers)

- **Horizontal Sharding**: Split rows across servers
- **Vertical Sharding**: Split columns across servers

### Partitioning vs Sharding

| Feature         | Partitioning                     | Sharding                          |
|-----------------|----------------------------------|-----------------------------------|
| Scope           | Single database                  | Multiple databases/servers        |
| Purpose         | Query performance                | Horizontal scalability            |
| Complexity      | Lower                           | Higher                            |
| Consistency     | Easier (single DB)              | Harder (distributed)              |

### Why Partition?

- **Partition pruning**: Queries only scan relevant partitions
- **Faster queries**: Less data to read
- **Easier maintenance**: Drop old partitions instead of DELETE
- **Parallel processing**: Different partitions processed in parallel

## ✅ Solutions & Examples

### PostgreSQL Range Partitioning

```sql
-- Create partitioned table
CREATE TABLE sales (
    sale_id    SERIAL,
    sale_date  DATE NOT NULL,
    amount     DECIMAL(10,2),
    region     VARCHAR(50)
) PARTITION BY RANGE (sale_date);

-- Create partitions
CREATE TABLE sales_2024 PARTITION OF sales
    FOR VALUES FROM ('2024-01-01') TO ('2025-01-01');

CREATE TABLE sales_2025 PARTITION OF sales
    FOR VALUES FROM ('2025-01-01') TO ('2026-01-01');

CREATE TABLE sales_2026 PARTITION OF sales
    FOR VALUES FROM ('2026-01-01') TO ('2027-01-01');

-- Query automatically uses partition pruning
SELECT * FROM sales WHERE sale_date = '2025-06-15';
-- ↑ Only scans sales_2025 partition
```

### Spark Partitioning

```python
# Write with partitioning
df.write \
    .partitionBy("year", "month") \
    .parquet("s3://datalake/sales/")

# Results in directory structure:
# s3://datalake/sales/year=2025/month=01/
# s3://datalake/sales/year=2025/month=02/
# ...

# Read with predicate pushdown (only reads needed partitions)
df = spark.read.parquet("s3://datalake/sales/") \
    .filter(col("year") == 2025)
```

---
---

# 🔥 TOPIC 17: File Formats (Parquet, Avro, ORC, JSON, CSV)

## 📖 Concepts

### Comparison

| Format    | Type         | Schema   | Compression | Splittable | Best For                     |
|-----------|--------------|----------|-------------|------------|------------------------------|
| **CSV**   | Row-based    | No       | Poor        | Yes        | Simple data exchange         |
| **JSON**  | Row-based    | No       | Poor        | Yes*       | APIs, semi-structured data   |
| **Avro**  | Row-based    | Yes      | Good        | Yes        | Streaming, schema evolution  |
| **Parquet**| Columnar    | Yes      | Excellent   | Yes        | Analytics, data warehousing  |
| **ORC**   | Columnar     | Yes      | Excellent   | Yes        | Hive-optimized analytics     |

### Row-Based vs Columnar

```
ROW-BASED (CSV, Avro):                 COLUMNAR (Parquet, ORC):
┌────┬───────┬─────┐                    ┌────┬────┬────┬────┐
│ ID │ Name  │ Age │                    │ 1  │ 2  │ 3  │ 4  │  ← IDs
├────┼───────┼─────┤                    ├────┴────┴────┴────┤
│ 1  │ Alice │ 30  │                    │Alice│Bob │Carl│Dan│  ← Names
│ 2  │ Bob   │ 25  │                    ├────┬────┬────┬────┤
│ 3  │ Carl  │ 35  │                    │ 30 │ 25 │ 35 │ 28 │  ← Ages
│ 4  │ Dan   │ 28  │                    └────┴────┴────┴────┘
└────┴───────┴─────┘
                                        ✅ Better for: SELECT AVG(age) FROM...
✅ Better for: SELECT * WHERE id=2      ✅ Better compression (similar values together)
✅ Better for INSERT/UPDATE             ✅ Column pruning (read only needed columns)
```

### When to Use What?

| Use Case                        | Recommended Format |
|---------------------------------|--------------------|
| Data warehouse / analytics      | **Parquet**        |
| Hive-based processing           | **ORC**            |
| Kafka / streaming               | **Avro**           |
| API response / config           | **JSON**           |
| Simple data exchange            | **CSV**            |
| Schema evolution needed         | **Avro** or **Parquet** |
| Machine learning features       | **Parquet**        |

---
---

# 🔥 TOPIC 18: Linux & Shell Scripting Basics

## 📖 Concepts & Commands

### Essential Commands for Data Engineers

```bash
# File operations
ls -la                    # List files with details
cat file.txt              # Print file contents
head -n 20 file.csv       # First 20 lines
tail -f logfile.log       # Follow log in real-time
wc -l file.csv            # Count lines
du -sh /data/             # Disk usage summary

# Text processing
grep "ERROR" app.log                    # Search for pattern
grep -c "ERROR" app.log                 # Count matches
awk -F',' '{print $1, $3}' data.csv     # Print columns 1 and 3
sed 's/old/new/g' file.txt              # Find & replace
sort -t',' -k3 -n data.csv             # Sort by 3rd column numerically
cut -d',' -f1,3 data.csv               # Extract columns 1 and 3
uniq -c                                 # Count unique lines

# Piping and Redirection
cat file.csv | grep "2025" | wc -l     # Count 2025 entries
command > output.txt                    # Redirect stdout
command 2> error.txt                    # Redirect stderr
command >> output.txt                   # Append output

# Process management
ps aux | grep python                    # Find Python processes
nohup python etl.py &                   # Run in background
crontab -e                              # Edit cron jobs

# Compression
gzip file.csv                           # Compress
gunzip file.csv.gz                      # Decompress
tar -czf archive.tar.gz /data/          # Create tar archive
tar -xzf archive.tar.gz                 # Extract tar archive

# Network
curl -X GET https://api.example.com/data   # HTTP request
scp file.csv user@server:/path/            # Secure copy
```

### Cron Expression Format

```
* * * * * command
│ │ │ │ │
│ │ │ │ └─ Day of week (0-7, 0 or 7 = Sunday)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)

# Examples:
0 6 * * *     → Daily at 6:00 AM
*/15 * * * *  → Every 15 minutes
0 0 1 * *     → First day of every month at midnight
```

### Shell Script Example — Data Pipeline

```bash
#!/bin/bash
set -euo pipefail  # Exit on error, undefined vars, pipe failures

DATE=$(date +%Y-%m-%d)
LOG_FILE="/var/log/etl_${DATE}.log"
DATA_DIR="/data/raw/${DATE}"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "Starting daily ETL pipeline"

# Step 1: Download data
log "Downloading data..."
mkdir -p "$DATA_DIR"
curl -s "https://api.example.com/data?date=${DATE}" -o "${DATA_DIR}/raw.json"

# Step 2: Validate
ROW_COUNT=$(cat "${DATA_DIR}/raw.json" | python3 -c "import sys,json; print(len(json.load(sys.stdin)))")
if [ "$ROW_COUNT" -lt 100 ]; then
    log "ERROR: Only ${ROW_COUNT} rows. Expected >= 100"
    exit 1
fi

# Step 3: Process
log "Processing ${ROW_COUNT} rows..."
python3 /scripts/process_data.py --input "${DATA_DIR}/raw.json" --output "${DATA_DIR}/processed.parquet"

# Step 4: Upload
log "Uploading to S3..."
aws s3 cp "${DATA_DIR}/processed.parquet" "s3://datalake/processed/${DATE}/"

log "ETL pipeline completed successfully"
```

---
---

# 🔥 TOPIC 19: Git & Version Control

## 📖 Key Commands

```bash
# Basic workflow
git init                                # Initialize repo
git clone <url>                         # Clone remote repo
git add .                               # Stage all changes
git commit -m "feat: add sales ETL"     # Commit with message
git push origin main                    # Push to remote
git pull origin main                    # Pull latest changes

# Branching
git branch feature/new-pipeline         # Create branch
git checkout feature/new-pipeline       # Switch to branch
git checkout -b feature/new-pipeline    # Create + switch (shortcut)
git merge feature/new-pipeline          # Merge into current branch
git rebase main                         # Rebase current branch on main

# Inspection
git log --oneline -10                   # Last 10 commits (compact)
git diff                                # Show unstaged changes
git status                              # Check current state
git blame file.py                       # Who changed each line

# Undo
git stash                               # Save changes temporarily
git stash pop                           # Restore stashed changes
git reset --soft HEAD~1                 # Undo last commit (keep changes)
git reset --hard HEAD~1                 # Undo last commit (discard changes)
git revert <commit-hash>               # Create a new commit that undoes changes
```

### Git Workflow for Data Engineering Teams

```
main ──────────────────────────────────────────────
  │                           ↑ (merge via PR)
  └── feature/sales-pipeline ──────────────────
                                (develop, test, review)
```

### Conventional Commits

```
feat: add new sales ETL pipeline
fix: handle null values in customer data
refactor: optimize Spark join logic
docs: update pipeline documentation
test: add unit tests for transform step
ci: add GitHub Actions workflow
```

---
---

# 🔥 TOPIC 20: System Design for Data Pipelines

## 📖 Concepts

### Design Principles

1. **Idempotency** — Re-running a pipeline produces the same result
2. **Fault Tolerance** — Handle failures gracefully (retries, checkpoints)
3. **Scalability** — Handle 10x data growth without redesign
4. **Observability** — Logging, monitoring, alerting
5. **Data Quality** — Validate at every stage
6. **Modularity** — Reusable, composable components
7. **Security** — Encryption, access control, PII handling

### Common Design Question: "Design a real-time analytics pipeline"

```
┌──────────┐    ┌─────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────┐
│ Sources  │───→│  Kafka  │───→│ Spark        │───→│ Data         │───→│ BI Tools │
│ (Apps,   │    │ (Buffer │    │ Structured   │    │ Warehouse    │    │(Looker,  │
│  APIs,   │    │  & Log) │    │ Streaming    │    │(Redshift/BQ) │    │ Tableau) │
│  IoT)    │    │         │    │              │    │              │    │          │
└──────────┘    └─────────┘    └──────┬───────┘    └──────────────┘    └──────────┘
                                      │
                                      ↓
                               ┌──────────────┐
                               │ Data Lake    │
                               │ (S3/ADLS)   │
                               │ Raw + Processed│
                               └──────────────┘
```

### Design Question: "Design a batch data warehouse pipeline"

```
                    ┌──────────────────────────────────────────────────────┐
                    │                   ORCHESTRATION                      │
                    │              (Apache Airflow DAG)                    │
                    │                                                      │
  ┌─────────┐      │   ┌─────────┐   ┌───────────┐   ┌───────────────┐  │   ┌──────────┐
  │ Sources │──────┼──→│ Extract │──→│ Transform │──→│     Load      │──┼──→│ Serve    │
  │         │      │   │ (Ingest │   │ (Clean,   │   │ (Write to DW) │  │   │ (BI/SQL) │
  │ - APIs  │      │   │  to S3) │   │  Conform, │   │               │  │   │          │
  │ - DBs   │      │   │         │   │  Enrich)  │   │               │  │   │          │
  │ - Files │      │   └─────────┘   └───────────┘   └───────────────┘  │   └──────────┘
  └─────────┘      │        ↓              ↓               ↓             │
                    │   ┌─────────────────────────────────────────────┐  │
                    │   │     DATA QUALITY CHECKS (every stage)      │  │
                    │   │   Freshness | Completeness | Accuracy      │  │
                    │   └─────────────────────────────────────────────┘  │
                    │        ↓              ↓               ↓             │
                    │   ┌─────────────────────────────────────────────┐  │
                    │   │        MONITORING & ALERTING               │  │
                    │   │   Logs → CloudWatch/Prometheus → PagerDuty │  │
                    │   └─────────────────────────────────────────────┘  │
                    └──────────────────────────────────────────────────────┘
```

### How to Answer System Design Questions

1. **Clarify Requirements**: Volume, velocity, variety of data? SLA? Users?
2. **High-Level Architecture**: Draw the components and data flow
3. **Deep Dive**: Choose technologies for each component; justify choices
4. **Data Model**: Design fact/dimension tables or document structures
5. **Scalability**: How to handle 10x/100x growth?
6. **Failure Handling**: Retries, dead-letter queues, idempotency
7. **Monitoring**: What metrics to track? How to alert?
8. **Trade-offs**: Cost vs performance vs complexity

---
---

# 🔥 TOPIC 21: Behavioral / Scenario-Based Questions

## Common Questions & How to Answer (STAR Method)

### Q1: "Tell me about a data pipeline failure you handled."

**Framework**: Situation → Task → Action → Result

> *"In my previous role, our daily sales ETL failed at 3 AM due to a schema change in the source API. I was paged, identified the root cause using Airflow logs, implemented a schema validation step as a pre-check, added alerting for schema drift, and built a retry mechanism with exponential backoff. This reduced pipeline failures by 80%."*

### Q2: "How do you handle late-arriving data?"

> - Use **event time** instead of processing time
> - Implement **watermarks** (in Spark Structured Streaming)
> - Design pipelines to be **reprocessable** (idempotent)
> - Use **SCD Type 2** for slowly changing dimensions
> - Keep raw data in data lake for **backfill**

### Q3: "How do you ensure data quality?"

> - Define **data contracts** between producers and consumers
> - Implement **automated checks** at each pipeline stage (Great Expectations, dbt tests)
> - Monitor **data freshness** with alerting (e.g., data not updated in 24h → alert)
> - Track **data lineage** (where data came from, what transformed it)
> - Regular **reconciliation** between source and target systems

### Q4: "How do you handle PII data?"

> - **Classify** data (PII, confidential, public)
> - **Encrypt** at rest and in transit
> - Use **column-level masking** or **tokenization**
> - Implement **role-based access control (RBAC)**
> - Follow **GDPR/CCPA** — right to erasure, data retention policies
> - Use **separate secure environments** for PII processing

### Q5: "Describe your experience with CI/CD for data pipelines."

> - **Version control** all pipeline code (Git)
> - **Automated testing**: unit tests for transformations, integration tests for end-to-end
> - **CI pipeline**: lint → test → build → deploy to staging
> - **CD pipeline**: Deploy to production after staging validation
> - **dbt slim CI**: Only test/build changed models
> - **Infrastructure as Code**: Terraform/CloudFormation for resources

---
---

# 🎯 QUICK REVISION — KEY FORMULAS & CHEAT SHEET

## SQL Must-Know Patterns

```sql
-- Find Nth highest salary
SELECT DISTINCT salary
FROM (
    SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
    FROM employees
) ranked
WHERE rnk = N;

-- Year-over-Year growth
SELECT
    year,
    revenue,
    LAG(revenue) OVER (ORDER BY year) AS prev_year,
    ROUND((revenue - LAG(revenue) OVER (ORDER BY year)) * 100.0
          / LAG(revenue) OVER (ORDER BY year), 2) AS yoy_growth
FROM yearly_revenue;

-- Pivot (rows to columns)
SELECT
    product,
    SUM(CASE WHEN quarter = 'Q1' THEN sales END) AS Q1,
    SUM(CASE WHEN quarter = 'Q2' THEN sales END) AS Q2,
    SUM(CASE WHEN quarter = 'Q3' THEN sales END) AS Q3,
    SUM(CASE WHEN quarter = 'Q4' THEN sales END) AS Q4
FROM quarterly_sales
GROUP BY product;

-- Consecutive days problem (gaps and islands)
WITH numbered AS (
    SELECT login_date,
           login_date - ROW_NUMBER() OVER (ORDER BY login_date) * INTERVAL '1 day' AS grp
    FROM logins
)
SELECT MIN(login_date), MAX(login_date), COUNT(*) AS consecutive_days
FROM numbered
GROUP BY grp
HAVING COUNT(*) >= 3;
```

## PySpark Must-Know Patterns

```python
# Read → Transform → Write
df = spark.read.parquet("s3://input/")
df_clean = df.filter(col("status") == "active") \
             .withColumn("total", col("price") * col("qty")) \
             .dropDuplicates(["order_id"])
df_clean.write.partitionBy("date").parquet("s3://output/")

# Broadcast join
result = big_df.join(broadcast(small_df), "key")

# Unpivot / Melt
from pyspark.sql.functions import expr
df.selectExpr("id", "stack(3, 'Q1', Q1, 'Q2', Q2, 'Q3', Q3) as (quarter, sales)")
```

## Key Numbers to Remember

| Metric                     | Value                    |
|----------------------------|--------------------------|
| Parquet row group size     | 128 MB (default)         |
| HDFS block size            | 128 MB (default)         |
| Spark partition target     | 128 MB per partition     |
| Kafka message max size     | 1 MB (default)           |
| Broadcast join threshold   | 10 MB (default Spark)    |
| Spark executor memory      | 4-8 GB typical           |
| Redshift max columns       | 1,600                    |
| BigQuery max query size    | 1 TB (free tier monthly) |

---

# 🏆 FINAL TIPS FOR THE INTERVIEW

1. **Think out loud** — Explain your reasoning process
2. **Clarify before coding** — Ask questions about edge cases
3. **Start with brute force** — Then optimize
4. **Mention trade-offs** — There's no perfect solution
5. **Be honest** — If you don't know something, say so and explain how you'd find out
6. **Show passion** — Talk about data engineering challenges you've solved
7. **Ask good questions** — About their tech stack, team, data volumes, challenges

> **Good luck at your KenexAI interview! 🚀**

---
*Prepared on June 11, 2026*
