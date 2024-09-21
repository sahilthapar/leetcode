-- active within last 30 days
-- at least 5 sessions
-- at least 10 listening hours

with active_status as (
select
    country,
    case
        when last_active_date >= '2024-01-01' and listening_hours >= 10 and sessions >= 5 then 1 else 0
    end as is_active
from penetration_analysis
)
select
country,
avg(is_active)
from active_status
group by 1