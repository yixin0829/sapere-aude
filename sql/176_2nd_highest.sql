-- LIMIT [offset,] row_count;
-- where the offset of the first row is 0 (default)

--* this is wrong since it returns nothing if only have one record (i.e. no 2nd highest)
SELECT
    Salary AS SecondHighestSalary
FROM Employee
ORDER BY Salary DESC
LIMIT 1,1 -- offset 1 (i.e. skip the first row)
;

-- ans1
SELECT(
    SELECT DISTINCT Salary
    FROM
        Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET 1
    ) AS SecondHighestSalary
;

-- ans2
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
