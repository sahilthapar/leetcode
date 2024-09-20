with ranked_products as
(
    select
        p.product_class,
        count(o.product_id) as count_sales,
        rank() over (order by count(o.product_id) desc) as sale_rank
    from online_products p
    join online_orders o
    on p.product_id = o.product_id
    group by 1
)
select product_class from ranked_products
order by sale_rank
limit 3
