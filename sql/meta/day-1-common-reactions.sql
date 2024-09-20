-- find totals by reaction type
-- rank to find the highest

with reaction_totals as (
select reaction, count(1) as reaction_count,
rank() over (order by count(1) desc) as n
from facebook_reactions
where date_day = 1
group by 1
)
select
reaction,
reaction_count
from reaction_totals
where n = 1