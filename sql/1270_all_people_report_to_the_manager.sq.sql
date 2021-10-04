--* fastest approach: self join
SELECT e1.employee_id
FROM Employees e1
    JOIN Employees e2
    ON e1.manager_id = e2.employee_id
    JOIN Employees e3
    ON e2.manager_id = e3.employee_id
WHERE
    e3.manager_id = 1
    AND e1.employee_id != 1

-- My approach: cross join with union
(
    select
        employee_id
    from employees
    where
        manager_id = 1
        and employee_id != 1 -- boss cannot report to himself
)
union
(
    select
        a.employee_id
    from employees as a, employees as b
    where
        a.manager_id = b.employee_id
        and b.manager_id = 1
        and a.employee_id != 1 -- boss cannot report to himself
 )
 union
(
    select
        a.employee_id
    from employees as a, employees as b, employees as c
    where
        a.manager_id = b.employee_id
        and b.manager_id = c.employee_id
        and c.manager_id = 1
        and a.employee_id != 1 -- boss cannot report to himself
 )
 union
(
    select
        a.employee_id
    from employees as a, employees as b, employees as c, employees as d
    where
        a.manager_id = b.employee_id
        and b.manager_id = c.employee_id
        and c.manager_id = d.employee_id
        and d.manager_id = 1
        and a.employee_id != 1 -- boss cannot report to himself
 )