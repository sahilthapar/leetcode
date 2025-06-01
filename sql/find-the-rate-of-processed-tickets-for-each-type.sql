select
type,
avg(case when processed then 1 else 0 end) as processed_rate
from facebook_complaints
group by 1;