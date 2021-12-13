# Spark SQL Tips

## General
* When using aliases in VIEW be aware that the alias will carry on to the outer query. One possible solution is to use TABLE instead
* Use `PIVOT()` function to convert rows to columns aka long to wide conversion (See [a demo blog from Databrick](https://databricks.com/blog/2018/11/01/sql-pivot-converting-rows-to-columns.html) for example)

## Limit for Groups
Limit top in groups with [window function](https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html) (e.g. dense_rank())

## Using Wildcard for Patterns
To include all the mistyped or similar ketwords, can use `lower()` or
`upper()` function with wildcard pattern in either all lower or all upper case.

```
WHERE LOWER(CAR_NAME) LIKE '%black_honda%'
```

## `CLUSTERED BY`
Something related to `MapReduce` processing technique that is applied in
Hadoop. In general makes the join faster.

## Volatile table/table/view
* Permanent table - usually used for tableau report (e.g `create table P_KAST.table_name as ...`)
* Temporary table - take up space in the cluster (`create temporary table temp_table_name as ...`)
* Volatile table (usually preferred) vs. temporary view
    * Volatile table - will store the data in the local memory space (cleared at the end the session)
    * View - an “alias” or a “function” that is “called” every time you use a temporary view

## Update and Delete Rows
* only **Delta tables** supports update/delete
* update one table and cross-table update
```sql
-- one table update
update
    table_name
set
    country = 'UK'
where
    site_id = 2;
```
* delete rows (one table and cross-table)
```sql
delete from -- rows
    table_name
where
    country = 'UK'
    user_seg = 123;
```

## SQL Optimization (Spark)
### Table Layout - Partition
* data size less than 200GB, use Partition!
* partition accelerate data locating to benefit query performance
* choose right partition column: low [cardinality](https://stackoverflow.com/questions/10621077/what-is-cardinality-in-databases) (a few unique categories) & frequent used in filter condition (WHERE)
```sql
create table sales (
    prod_id int,
    user_id int,
    dt date,
    site int
) partitioned by (dt, site);
```

### Table Layout - Bucket
* data size more than 200GB, use Bucket!
* choose right columns: high cardinality & avoid data skew
* bucket number: 500 is recommended as start
* sort is optional, recommend on frequent used column in filter condition
```sql
CREATE TABLE Items (
    item_id INT,
    seller_id INT,
    dt DATE
    ) CLUSTERED BY(item_id) INTO 1000 BUCKETS SORTED BY dt;
```

### Join 101
* Adjust the order of joins: Put small join table ahead
* Small table joins with inequality conditions can be slow (slow parallelism) -> avoid
    * General rule of thumb: don't put equality condition (e.g. a.session_start_dt < b.session_start_dt) after `ON` in joins
    * Solution: creating a bucket table with 500-1000 buckets contatining all the data that the small table has. Then join with the bucket table
* **Bucketing joins** - see this video by [query optimization using bucketing by Databricks](https://databricks.com/session/bucketing-in-spark-sql-2-3)
    * If a table satify below conditions, consider construct it as a bucketed table:
        1. Table size is **huge** (e.g. web traffic table). Over 500GB.
        2. Table used frequently in joins with **same** key.
        3. For small table, only when it used to join with huge bucket table.
        4. The sort merge join (without bucket) is **slow due to shuffle, not due to data skewing**.
    * Choise of `SORT BY` columns: date-like columns or bucket columns, or just leave it EMPTY.
    * Bucketing join: **bucketing join only works if bucket columns are subset of join keys

### Avoid Duplicated Clauses
* Use same clauses repeatly
* Join same table twice (once in view or temp table, the other could happen in the main query)


### Join Deep-dive in Spark
* [The art of joining in Spark](https://towardsdatascience.com/the-art-of-joining-in-spark-dcbd33d693c) explains the skewness existed in some joins and how to overcome it

### Common Table Expression (CTE) Optimization
* Spark SQL does not support op for CTE yet. So, manully CTE can improve performance.
* avoid using the same functions/expressions repeatedly in a `CASE` statement
    * solution: create a sub-query and inside that create aliases for commonly used expressions
* CTE: `A like X or A like Y" => "A like ANY (X, Y)`
* explicitly type cast the join key(s) to have the same data type when doing bucket join


# MySQL Tips
* [Some good read about SQL interview (crash read)](https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c)

## Window Functions
* check out [this MySQLTutorial article](https://www.mysqltutorial.org/mysql-window-functions/)
    * `DENSE_RANK()`: doesn't leave gap in between the ranking (e.g. 1,1,2,3,3,4,5...). check out [this article](https://www.mysqltutorial.org/mysql-window-functions/mysql-rank-function/)
    * `RANK()`: leaves gap in between the ranking (e.g. 1,1,3,4,4,6,7...)
    * `ROW_NUMBER()`: (e.g. 1,2,3,4...)
    * example: rank the most recent price change for each product before date '2019-08-16'
```sql
select
    product_id
    , new_price
    , change_date
    , dense_rank() over (partition by product_id order by change_date desc) as date_rank
from products
where change_date <= '2019-08-16'
;

-- general syntax
window_function_name(expression) OVER ( 
   [partition_defintion]
   [order_definition]
   [frame_definition]
)
```

### LAG() & LEAD()
* [MySQL tutorial documentation](https://www.mysqltutorial.org/mysql-window-functions/mysql-lead-function/)
* Syntax
```sql
LEAD(<expression>[,offset[, default_value]]) OVER (
    PARTITION BY (expr)
    ORDER BY (expr)
)
```

## IF Statement
This is a simplied version of CASE statement. The general syntax is `IF(condition, if_true, if_false)`. This is handy when combined with aggregation functions like `SUM()` or `COUNT()` so you can create conditional aggregation for different columns. More details [here](https://www.w3schools.com/sql/func_mysql_if.asp)

```sql
select
    product_id
    , sum(if(month=6, quantity * price, 0)) as juneCost
    , sum(if(month=7, quantity * price, 0)) as julyCost
from products
;
```

## IFNULL & COALESCE
Usually used to handle NULL field.
* `ifnull()` returns 1 if it's NULL and 0 if it's not. Can also use `col IS NULL` or `col IS NOT NULL`
* `coalesce(col1, col2, col3, ...)` returns the first non-null column

## Common Table Expression (Alternative for temp view in Leetcode)
Leetcode SQL judger does not support multiple statements (i.e. create or replace temporary view ... as (...) won't work).
We can use `WITH` clause instead to name temporary result set that exists within the scope of a single statement and that can be referred to later within that statement.

```sql
WITH
  cte1 AS (SELECT a, b FROM table1),
  cte2 AS (SELECT c, d FROM table2)
SELECT b, d FROM cte1 JOIN cte2
WHERE cte1.a = cte2.c;
```

Notice everything is done in ONE statement.
