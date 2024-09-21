-- with agg_messages as(
-- select user1 as user_name, msg_count from fb_messages
-- UNION ALL
-- select user2 as user_name, msg_count from fb_messages
-- )
-- select user_name, sum(msg_count) as msg_count
-- from agg_messages
-- group by user_name
-- order by 2 desc
-- limit 10;
-- -- 0.00740 seconds


-- alternate with rank maybe? I like the simpler version above

with sq as (
select username,
sum(msg_count) as msg_count,
rank() over (order by sum(msg_count) desc)
from
(select user1 as username, msg_count from fb_messages
UNION ALL
select user2 as username, msg_count from fb_messages) a
group by 1
)
select username, msg_count from sq
where rank <= 10
order by msg_count desc

--  0.01251 seconds
