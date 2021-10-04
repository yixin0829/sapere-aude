--# yix's: use sum() and if() to create conditional columns first and then compute the ctr
select
    ad_id
    , ifnull(round(clicks / (views + clicks) * 100, 2), 0) as ctr
from (
    select
        ad_id
        , sum(if(action = "Clicked", 1, 0)) as clicks
        , sum(if(action = "Viewed", 1, 0)) as views
    from ads
    group by 1
) as a
order by ctr desc, ad_id asc
;

--* fastest: use avg() and case statement
select
    ad_id
    , ifnull(round(avg(case when action = 'clicked' then 1
                         when action = 'viewed' then 0
                         else null end)*100,2),0) as ctr
from ads
group by ad_id
order by ctr desc, ad_id
;