select
    p.product_id,
    p.brand_name
from online_products p
join online_orders o
on p.product_id = o.product_id
group by 1, 2
having count(units_sold) > 1 and avg(cost_in_dollars) >= 3
