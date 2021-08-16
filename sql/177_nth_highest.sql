-- approach 1: using limit offset
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M=N-1; -- This is the offset will be used in LIMIT later
  RETURN (
      # Write your MySQL query statement below.
      -- Select all distinct Salary first and order from DESC (biggest at the top)
      -- LIMIT offset, row count 
      SELECT DISTINCT Salary FROM Employee ORDER BY Salary DESC LIMIT M, 1
  );
END

-- approach2: use window function ie. rank()
-- (spark sql) https://databricks.com/blog/2015/07/15/introducing-window-functions-in-spark-sql.html
-- (dense_rank vs. row_number vs. rank) https://www.sqlshack.com/overview-of-sql-rank-functions/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
          select q1.salary
          from (
                select dense_rank() over (order by salary desc) as rank_nbr
                      ,salary
                from employee
          ) as q1
          where rank_nbr = N
          group by 1
  );
END
