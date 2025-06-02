-- with recent_refinance as (
--     select
--         user_id,
--         id,
--         rank() over (partition by user_id order by created_at desc) as recent_rank
--     from loans
--     where type = 'Refinance'
-- )
-- select 
--     user_id,
--     balance
-- from submissions s
-- inner join recent_refinance r
-- on s.loan_id = r.id
-- where recent_rank = 1

select 
    l.user_id,
    s.balance
from submissions s
inner join loans l on s.loan_id = l.id
where l.type = 'Refinance'
  and l.created_at = (
    select max(created_at) 
    from loans l2 
    where l2.user_id = l.user_id 
      and l2.type = 'Refinance'
  );
