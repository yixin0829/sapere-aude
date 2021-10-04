# Write your MySQL query statement below

# 1. compute the expense for each (customer_id, name) in June and July 2020
# 2. filter for >$100 in both month

select
    customer_id
    , name
from (
    select
        customer_id
        , name
        , mth
        , sum(cost) as monthlyCost
    from (
        select
            orders.customer_id
            , customers.name
            , order_id
            , order_date
            , (price * quantity) as cost
            , month(order_date) as mth
        from orders
            join product
                on orders.product_id = product.product_id
            join customers
                on orders.customer_id = customers.customer_id
    ) as a
    where
        mth in (6, 7)  
    group by 1,2,3
) as b
where monthlyCost >= 100
group by 1
having count(1) = 2
;

--# fastest method using case statement or if statement
SELECT 
    customer_id,
    name
FROM Customers 
JOIN Orders USING(customer_id) 
JOIN Product USING(product_id)
GROUP BY customer_id
HAVING 
    SUM(
        IF(MONTH(order_date) = 6, quantity, 0) * price
    ) >= 100 AND 
    SUM(
        IF(MONTH(order_date) = 7, quantity, 0) * price
    ) >= 100;