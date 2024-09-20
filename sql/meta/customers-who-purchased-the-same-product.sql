with aux_table as (
select
o.product_id,
p.brand_name,
o.customer_id,
count(o.customer_id) over (partition by o.product_id) as unique_cust_no
from online_orders o
left join online_products p
on o.product_id = p.product_id
where p.product_class = 'FURNITURE'
group by 1, 2, 3
order by 4 desc
)
select
*
from aux_table
