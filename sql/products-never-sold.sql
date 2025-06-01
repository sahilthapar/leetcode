-- find total categories
-- find categories that never sold
with aux_table as (

select
    c.category_name,
    coalesce(sum(units_sold), 0) as units_sold
from online_product_categories c
left join online_products p
    on p.product_category = c.category_id
left join online_orders o
    on p.product_id = o.product_id
group by 1
)
select
100 * ((
    select count(*) from aux_table where units_sold = 0) / count(*)::float
) as pct_unsold
from aux_table
