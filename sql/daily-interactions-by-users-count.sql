with num_people as (
select a.day, count(distinct a.user) as num_people from (
select day, user1 as user from facebook_user_interactions
union all
select day, user2 as user from facebook_user_interactions
) a
group by a.day
), num_interactions as (
select day, count(1) as num_interactions from facebook_user_interactions group by day
)
select
p.day,
num_people,
num_interactions
from num_people p
left join num_interactions i
on p.day = i.day