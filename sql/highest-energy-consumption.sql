with total_consumption as
(
select coalesce(eu.date,na.date,asia.date) as date,  sum(coalesce(eu.consumption, 0) + coalesce(asia.consumption, 0) + coalesce(na.consumption, 0)) as total_consumption
from fb_eu_energy eu
full outer join fb_asia_energy asia
on eu.date = asia.date
full outer join fb_na_energy na
on eu.date = na.date
group by 1
)
select
date,
total_consumption
from total_consumption t
where t.total_consumption = (select max(total_consumption) from total_consumption)
order by 1