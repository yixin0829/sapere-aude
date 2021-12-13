-- youtube link: https://www.youtube.com/watch?v=XOJk0AKIqv8


-----------------------------  Part2: SQL ------------------------------ 
-- Messages table: user_id, user_name, date, message_sent, message_received
-- Q1: for each day, return the name of the user who received the highest message_sent to message_received ratio
select
    date
    , user_name
    , row_number() over (partition by date order by sent_to_received_ratio desc) as rank -- ensure only returns one for each date
from (
    select
        user_id
        , case when message_received = 0 then inf -- handle divided by zero (either NULL or large number)
            else message_sent / message_received end as sent_to_received_ratio
    from Messages
) as a
where 1=1
    and rank = 1
;


-- Q2: for each user, return the first date when the user received 0 message
select
    user_id
    , user_name
    , date
    , row_number() over (partition by user_id order by date asc, zero_msg desc) as rank
from (
    select
        user_id
        , user_name
        , date
        , case when message_received = 0 then 1
            else 0 end as zero_msg -- boolean column
    from Messages
) as a
where 1=1
    and rank = 1
;

-- Q2 (better approach)
select user_name, min(date) as date
from Messages
where message_received = 0

group by user_name;


-----------------------------  Part3: Case ------------------------------ 
-- 1) how do you determine if a user is an influencer on Instagram?

goal: match advertiser to influencers
definition: # of follwers; # of overall views of their post; paid ads