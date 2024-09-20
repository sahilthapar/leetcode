select
    m.date,
    count(distinct m.user_id)
from
mobile_logs m
inner join web_logs w
    on m.user_id = w.user_id AND m.date = w.date
group by 1;
