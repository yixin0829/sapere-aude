select distinct num as ConsecutiveNums
from (
    select
        num
        , lead(num, 1) over () as nextnum -- use lead() window function to get the num from next row
        , lead(num, 2) over () as nextnextnum
    from logs
) as a
where num = nextnum and nextnum = nextnextnum
;