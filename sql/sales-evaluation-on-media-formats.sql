-- product_type, media_type, units_sold as a percentage

with total_sales as (
select
promotions.media_type,
products.product_family,
sum(orders.units_sold * cost_in_dollars) as category_sales
from online_orders orders
left join online_sales_promotions promotions
on orders.promotion_id = promotions.promotion_id
left join online_products products
on orders.product_id = products.product_id
group by 1, 2
), category_sales as (
select
product_family,
sum(category_sales) as family_sales
from total_sales
group by 1
)
select
t.media_type,
t.product_family,
(t.category_sales / c.family_sales::float) * 100 as pct_sales
from total_sales t
left join category_sales c
on t.product_family = c.product_family

