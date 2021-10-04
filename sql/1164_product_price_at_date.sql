select
    a.product_id
    , coalesce(price, 10) as price
from (
    (
        select distinct
            product_id
        from products
    ) as a
    left join
    (
        select
            product_id
            , new_price as price
        from (
            select
                product_id
                , new_price
                , change_date
                , dense_rank() over (partition by product_id order by change_date desc) as date_rank
            from products
            where change_date <= '2019-08-16'
        ) as b
        where date_rank = 1
    ) as c
    on a.product_id = c.product_id
);