with dec_2019_ranks as (
select
    u.country,
    dense_rank() over (order by sum(number_of_comments) desc) as rnk
from fb_comments_count c
join fb_active_users u
    on c.user_id = u.user_id
where created_at between '2019-12-01' and '2019-12-31'
group by 1
),
jan_2020_ranks as (
select
    u.country,
    dense_rank() over (order by sum(number_of_comments) desc) as rnk
from fb_comments_count c
join fb_active_users u
    on c.user_id = u.user_id
where created_at between '2020-01-01' and '2020-01-31'
group by 1
)
select
    j.country
from dec_2019_ranks d
full outer join jan_2020_ranks j
    on d.country = j.country
where j.rnk < d.rnk
    or (d.rnk is null and j.rnk is not null)
