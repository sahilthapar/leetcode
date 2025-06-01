select
(
    select
        count(distinct user_id)
    from fb_active_users
    where status = 'open' and country = 'USA'
) / count(*)::float as active_share
from fb_active_users
where country = 'USA'
