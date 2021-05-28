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
