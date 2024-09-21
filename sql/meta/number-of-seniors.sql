with seniors as (
select count(1) as count_seniors
from facebook_employees
where is_senior
),
usa_workers as (
select count(1) as count_americans
from facebook_employees
where location = 'USA'
)
select
case
    when count_seniors > count_americans then 'More seniors'
    else 'More USA-based'
end
from seniors
inner join usa_workers
on 1=1