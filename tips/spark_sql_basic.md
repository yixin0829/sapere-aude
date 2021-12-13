# Spark SQL Basic
The official SQL Syntax doc by Apache Spark can be found in [HERE](https://spark.apache.org/docs/latest/sql-ref-syntax.html)

## SQL Execution Precendence
1. `FROM` - choose and join tables to get base data
2. `WHERE` - filter the base data
3. `GROUP BY` - aggregates the base data
4. `HAVING` - filters the aggregated data
5. `SELECT` - select from the final processed data
6. `ORDER BY` - sorts the final data
7. `LIMIT` - limits the returned data to a row count

## Functions & Syntax
* `MONTH(DATE)` - returns the month of the date
* `ISNULL(FIELD)` - returns true if it's NULL

### `CASE` Clause
[Spark SQL CASE clause official doc](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-case.html)

Useful when used to replace `NULL` with 0, convert boolean to int type, and creating one-hot encoded columns.
```sql
CASE [ expression ] { WHEN boolean_expression THEN then_expression } [ ... ]
    [ ELSE else_expression ]
END
```

### Wildcard
A [wildcard](https://www.w3schools.com/sql/sql_wildcards.asp) character is used to substitute one or more characters in a string.

Wildcard characters are used with the `LIKE` operator. The `LIKE` operator is used in a `WHERE` clause to search for a specified pattern in a column.

### `BETWEEN` Operator
```sql
WHERE FIELD BETWEEN VALUE1 AND VALUE2
```
Usually used in date selection when you want to select an interval of date.

### `coalesce` Function
[coalesce](https://spark.apache.org/docs/latest/api/sql/index.html#coalesce) returns the first non-null argument if exists
otherwise null. Useful to replace `NULL` with 0 in practice. `select coalesce(CTR, 0) from table1` if null then go for 0.


# Spark SQL Style Guide

## Table of Contents
- [Spark SQL Style Guide](#fast-spark-sql-style-guide)
  * [Motivation](#motivation)
  * [General](#general)
  * [`SELECT`](#select)
    + [Window Functions](#window)
  * [`FROM` and `JOIN`](#from-and-join)
  * [`WHERE` and `HAVING`](#where-and-having)
  * [`GROUP/ORDER BY`](#group-order-by)
  * [Temporary Views/Tables](#temp-views-tables)
  * [Common Table Expressions (CTEs)](#cte)

## Motivation <a name="motivation"></a>
Following a consistent coding style allows better reproducibility and clarity which facilitate collabration when conduct code reviewing & knowledge transistion. A team following a style guide helps everyone write code in a consistent way, and consistent code is easier to read and faster to update. Consistent code is easier to read and understand making it faster to revise or add new metrics.

This style guide referenced [Fred Benenson's Kick Starter SQL Style Guide](https://gist.github.com/fredbenenson/7bb92718e19138c20591). Thank you Fred.

## General <a name="general"></a>
* Use tabs (4 spaces) for indenting
* No trailing whitespace
* Always CAPITALIZE SQL keywords (e.g. `SELECT` or `AS`)
* Always CAPITALIZE SQL functions (e.g. `COUNT()`)
* Variable names should be underscore delimited
* Avoid "deep" nested sub-queries (nested level > 2). Use Common Table Expressions (CTEs), temporary tables/views to break down your query.
* Always put ending `;` on a new line for easy editinga (unless the query is short)
* (Optional) insert a new line between dimensions and metrics in `SELECT` clause

## `SELECT` <a name="select"></a>
* Align all columns to the first column on their own line starting with `, ` (i.e. `SELECT` goes on its own line)
* Always rename aggregates and function-wrapped columns:
* Always include `AS` when renaming columns

```sql
SELECT
    user_id
    , user_email
    , CASE
        WHEN user_country = 'CA' then 'Canada'
        WHEN user_country = 'US' then 'United States'
        ELSE 'Other' END
        AS case_country -- CASE: indent WHEN and ELSE

    , COUNT(session.session_id) AS sessions
FROM ...
```

### Window Functions <a name="window"></a>
Long Window functions should be split across multiple lines: one for the PARTITION, ORDER and frame clauses.

```sql
SELECT
    ...
    , SUM(1) OVER (PARTITION BY categ_id, year
                   ORDER BY month DESC
                   ROWS UNBOUNDED PRECEDING) AS category_year
    ...
```

## `FROM` and `JOIN` <a name="from-and-join"></a>
* Only one table be in the same line with `FROM`
* Each join should be placed on a separate line followed by a new indented line of joined keys (i.e. `ON`) for easy reviewing
* Begin with `INNER JOIN` and then list `LEFT JOIN`, order them semantically, and do not intermingle `LEFT JOIN` with `INNER JOIN` unless necessary

```sql
SELECT
    projects.name AS project_name,

    COUNT(backings.id) AS backings_count
FROM ksr.projects AS projects
    INNER JOIN ksr.backings AS backings
        ON backings.project_id = projects.id
        AND backings.year = projects.year -- additional filter condition(s) 
    LEFT JOIN ...
        ON ...
```

## `WHERE` and `HAVING` <a name="where-and-having"></a>
* Always start the `WHERE` clause with `1=1` for [easy dynamic query structuring](https://stackoverflow.com/questions/1264681/what-is-the-purpose-of-using-where-1-1-in-sql-statements#:~:text=People%20use%20it%20because%20they,t%20have%20to%20figure%20out.).

```sql
SELECT
    name
    , goal
FROM random_table AS projects
WHERE 1=1
    AND country = 'CA' -- actual conditions go to 2nd line and below
    AND start_date >= '2021-08-29'
```
* Aggregation conditions for `HAVING` should be started on a new line

```sql
HAVING
    count(user_id) > 1000
    AND avg(listings) > 10
...
```

## `GROUP/ORDER BY` <a name="group-order-by"></a>
* Simplifying `GROUP/ORDER BY` by using column position in `SELECT` clause instead of whole column names

```sql
...
GROUP BY 1,2,3,4
ORDER BY 1 DESC, 2,3,4 -- sort column1 (descending) first, and then by column2/3/4 in ascending order
;  
```

## Temporary Views/Tables <a name="temp-views-tables"></a>
* Always indent the query by one tab and enclosed it with parentheses.

```sql
DROP TABLE IF EXISTS temp_table; -- include drop statement for error handling
CREATE TEMPORARY TABLE temp_table AS (
    SELECT -- indent the actual query
        *
    FROM random_table AS rnd
    WHERE 1=1
        AND country = 'CA'
        AND start_date >= '2021-08-29'
); -- enclosed with ); on a new line
```

## Common Table Expressions (CTEs) <a name="cte"></a>
* [Spark official documentation on CTEs](https://spark.apache.org/docs/latest/sql-ref-syntax-qry-select-cte.html)
* The body of a CTE must be one indent further than the WITH keyword. Open them at the end of a line and close them on a new line:

```sql
-- Multiple CTEs should be formatted accordingly
-- CTE with multiple column aliases
WITH backings_per_category (a1, a2) AS (
    SELECT
        column1
        , column2
        ...
), backers AS (
    SELECT
        ...
), backers_and_creators AS (
    ...
)
SELECT * FROM backers;
```