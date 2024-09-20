select
    (sum(case when p.promotion_id is not null then 1 else 0 end) / cast (count(*) as decimal) ) * 100 as pct
from online_orders o
left join online_promotions p
    on o.promotion_id = p.promotion_id
