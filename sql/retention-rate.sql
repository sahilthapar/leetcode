-- select all users that are active in dec and also after dec
-- select all users that are active in jan and also after jan
-- divide the two

with dec_ret as (
    select distinct account_id, user_id
    from sf_events
    where date_trunc('month', date) > '2020-12-01' and user_id in (
        select distinct user_id from sf_events where date_trunc('month', date) = '2020-12-01'
    )
),
jan_ret as (
    select distinct account_id, user_id
    from sf_events
    where date_trunc('month', date) > '2021-01-01' and user_id in (
        select distinct user_id from sf_events where date_trunc('month', date) = '2021-01-01'
    )
)
select
d.account_id,
case when count(j.user_id) > 0 then count(d.user_id) / count(j.user_id) else 0 end as ret_rate
from dec_ret d
left join jan_ret j
on d.account_id = j.account_id
group by 1
