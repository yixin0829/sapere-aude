-- rank dense_rank() and join
select
    department
    , employee
    , salary
from (
    select
        dep.name as department
        , emp.name as employee
        , salary
        , dense_rank() over (partition by dep.name order by salary desc) as rnk
    from employee as emp
        join department dep
        on emp.departmentid = dep.id
) as a
where rnk = 1
;