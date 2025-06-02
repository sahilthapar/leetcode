Select
cust_id,
sum(total_order_cost) as total_rev
from orders
where date_part('month', order_date) = 3 and date_part('year', order_date) = 2019
group by cust_id