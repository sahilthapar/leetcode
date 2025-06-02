-- each promotion
-- find the products that sold the most

-- promotion_id, product_id, total_sales for the product_id

-- group by 1, 2
-- window function to find rank between products


with ranked_product_sales as (
select
    promotion_id,
    product_id,
    sum(units_sold) as total_sales,
    rank() over (partition by promotion_id order by sum(units_sold) desc) as sales_rank
from online_orders
group by 1, 2
)
select
    promotion_id,
    product_id,
    total_sales
from ranked_product_sales
where sales_rank = 1
