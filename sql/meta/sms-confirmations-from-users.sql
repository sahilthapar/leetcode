-- find "valid" messages
-- find responses for the valid messages
-- calculate %


with valid_messages as (
select * from fb_sms_sends
where type = 'message'
and ds = '2020-08-04'
)
select
(count(c.phone_number) / cast(count(m.*) as decimal) * 100) as pct_response
from valid_messages m
left join fb_confirmers c
on m.phone_number = c.phone_number and m.ds = c.date
