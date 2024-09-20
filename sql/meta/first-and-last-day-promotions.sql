with orders_by_date as (
select
    promotion_id,
    date,
    count(1) as day_order_count,
    sum(count(1)) over (partition by promotion_id) as promotion_order_count
from online_orders
group by 1,2
)
select
p.promotion_id,
sum(case when p.start_date = o.date then (day_order_count / promotion_order_count::float) * 100 else 0 end) as start_date_pct,
sum(case when p.end_date = o.date then (day_order_count / promotion_order_count::float) * 100 else 0 end) as end_date_pct
from online_sales_promotions p
left join orders_by_date o
on p.promotion_id = o.promotion_id
and (o.date = p.start_date) or (o.date = p.end_date)
group by 1
