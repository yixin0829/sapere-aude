--# self join approach: abs() function and distinct is important otherwise will miss the last seat if it's consecutive as well
select distinct
    a.seat_id
from cinema as a
    join cinema as b
    on abs(a.seat_id - b.seat_id) = 1
    and a.free = 1
    and b.free = 1
order by seat_id
;

-- *Most intuitive way: select seat that one of its neighbour seats are free as well
select seat_id
from cinema
where free = 1 and (
    seat_id - 1 in (select seat_id from cinema where free = 1)
    or
    seat_id + 1 in (select seat_id from cinema where free = 1)
);
    