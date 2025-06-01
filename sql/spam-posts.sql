-- find all viewed posts
-- find which of the viewed posts have the keyword spam in it
-- calculate percentage


with viewed_posts as (
select *
from facebook_posts p
inner join facebook_post_views v
on p.post_id = v.post_id
)
select
post_date,
(sum(case when post_keywords ilike '%spam%' then 1 else 0 end) / cast(count(1) as decimal) * 100) as count_spam_posts
from viewed_posts
group by 1
