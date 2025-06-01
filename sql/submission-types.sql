select user_id
from loans
where type in ('Refinance', 'InSchool')
group by user_id
having count(distinct type) = 2;
