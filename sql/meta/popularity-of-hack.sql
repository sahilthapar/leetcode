select
    emp.location,
    avg(hack.popularity) as avg_popularity
from facebook_hack_survey hack
inner join facebook_employees emp
    on hack.employee_id = emp.id
group by 1
