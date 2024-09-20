select
    a.entry_date,
    count(distinct a.account_id),
    count(distinct b.account_id)
from premium_accounts_by_day a
left join premium_accounts_by_day b
    on a.account_id = b.account_id and (b.entry_date - a.entry_date = 7 and b.final_price > 0)
where a.final_price > 0
group by 1
order by 1
limit 7
