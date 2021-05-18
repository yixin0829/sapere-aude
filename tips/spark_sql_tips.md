# Spark SQL Tips

## General
* When using aliases in VIEW  be aware that the alias will carry on to the outer query. One possible solution is to use TABLE instead

## Limit for Groups
Limit top in groups with [window function](https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html) (e.g. dense_rank())

