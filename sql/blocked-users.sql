select
    block_reason,
    count(distinct user_id) as count_users
from fb_blocked_users
where
    (extract(MONTH from block_date) = 12 and extract(YEAR from block_date) = 2021) -- if block date is from DEC 2021
    OR
    (block_date < '2021-12-01' and block_duration is null) -- if user was blocked before DEC 2021 and banned permanently
    OR
    (block_date < '2021-12-01' and (block_date + cast(block_duration as int) >= '2021-12-01')) -- if block_date + block_duration is greater than Dec 2021
GROUP BY 1
