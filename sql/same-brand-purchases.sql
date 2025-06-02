with p1_users as (
    select distinct customer_id
    from online_orders o
    join online_products p
        on o.product_id = p.product_id and p.brand_name = 'Fort West'
),
p2_users as (
    select
        distinct customer_id
    from online_orders o
    join online_products p
    on o.product_id = p.product_id and p.brand_name = 'Golden'
)
select a.customer_id
from p1_users a
inner join p2_users b
on a.customer_id = b.customer_id
