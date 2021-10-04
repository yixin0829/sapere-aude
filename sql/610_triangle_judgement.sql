-- case statement and if statement is powerful when creating new column based on criterias/conditions
select
    x
    , y
    , z
    , case when (x+y > z) and (x+z > y) and (y+z > x) then 'Yes'
        else 'No' end as triangle
from triangle
;