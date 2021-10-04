# Spark SQL Tips

## General
* When using aliases in VIEW  be aware that the alias will carry on to the outer query. One possible solution is to use TABLE instead

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

# MySQL Tips
* [Some good read about SQL interview (crash read)](https://towardsdatascience.com/sql-questions-summary-df90bfe4c9c)

## Window Functions
* check out [this MySQLTutorial article](https://www.mysqltutorial.org/mysql-window-functions/)
    * `DENSE_RANK()`: doesn't leave gap in between the ranking (e.g. 1,1,2,3,3,4,5...). check out [this article](https://www.mysqltutorial.org/mysql-window-functions/mysql-rank-function/)
    * `RANK()`: leaves gap in between the ranking (e.g. 1,1,3,4,4,6,7...)
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