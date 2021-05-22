# Spark SQL Basic
The official SQL Syntax doc by Apache Spark can be found in [HERE](https://spark.apache.org/docs/latest/sql-ref-syntax.html)

## Style Guide
* `;` should be placed on a new line at the end of a query for clearity
* `lower_case` for functions (e.g. `avg(col)`)
* `lower_case` for aliasing (e.g. `FIELD1 AS a1`)
* `UPPERCASE` for SQL keywords, clause (e.g. `SELECT`, `WHERE`, `CASE`, `JOIN`)
* `UPPERCASE` for SQL logical operators (e.g. `IN`, `LIKE`, `AND`)
* Use `_` as delimiter (e.g. `DATABASE_1`, `fltr_seller`)

* Name aggregation for east join later with aliasing
* Line breaks (good practice)
```sql
-- for SELECT ', ' should be on a new line (easy commenting out)
SELECT FIELD1
    , FIELD2
    ...

-- for joining
...
FROM TABLE1 a
    LEFT JOIN TABLE2 b
    ON ...
    JOIN TABLE3 c
    ON ...

-- for filtering
...
WHERE <CONDITION1>
    AND <CONDITION2>
    ...
```

## SQL Execution Precendence
1. `FROM` - choose and join tables to get base data
2. `WHERE` - filter the base data
3. `GROUP BY` - aggregates the base data
4. `HAVING` - filters the aggregated data
5. `SELECT` - select from the final processed data
6. `ORDER BY` - sorts the final data
7. `LIMIT` - limits the returned data to a row count

## Simple Template
```sql
SELECT [FIELD1], [FIELD2], AGGR[FIELD3] [alias1], ..
FROM [TABLE1] [AS] [a2]
    JOIN [TABLE2] [AS] [a3]
    ON a2.[KEY] = a3.[KEY]
WHERE [CONDITION1]
    AND [CONDITION2]
    AND [CONDITION3]
GROUP BY 1, 2
HAVING AGGR[FIELD] [<|>|LIKE|=] CONDITIONS ..
ORDER BY 1, 2
LIMIT 10
;
```

Where `AGGR()` could be any aggregation function (e.g. `AVG`, `COUNT`) and we use 

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