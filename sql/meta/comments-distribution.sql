-- need to remove cases where the comment date is earlier than user join date
-- need to group by no of comments
-- and find the distinct users who commented that many times
with valid_comments as (
select
    f.id,
    count(*) as comment_count
from fb_users f
join fb_comments c
on f.id = c.user_id
where joined_at < created_at
and created_at between '2020-01-01' and '2020-01-31'
and joined_at between '2018-01-01' and '2020-01-31'
group by 1
)
select
comment_count,
count(id)
from valid_comments
group by 1
order by 1