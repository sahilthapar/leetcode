with ranked_types as (
select
    media_type,
    sum(cost) as total_cost,
    dense_rank() over (order by sum(cost) desc) as spend_rank
from online_sales_promotions
group by 1
)
select
    media_type,
    total_cost
from ranked_types
where spend_rank = 1 or spend_rank = 2