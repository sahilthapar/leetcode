with brand_customers as
(
    select
        brand_name,
        customer_id,
        count(customer_id) over (partition by brand_name) as brand_cust_count
    from online_orders o
    left join online_products p
    on o.product_id = p.product_id
    where p.product_family = 'CONSUMABLE'
    group by 1, 2
)
select

brand_name,
(brand_cust_count / (select count(distinct customer_id) from online_orders)::float) * 100 as pct
from brand_customers
group by 1, 2
