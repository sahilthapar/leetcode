with sent_requests as (
select
    user_id_sender as sender,
    user_id_receiver as receiver,
    date
from fb_friend_requests
where action = 'sent'
), accepted_requests as (
select
    user_id_sender as sender,
    user_id_receiver as receiver,
    date
from fb_friend_requests
where action = 'accepted'
)
select
sr.date,
(count(ar.sender) / cast(count(sr.sender) as decimal)) as acceptance_rate
from sent_requests sr
left join accepted_requests ar
on sr.sender = ar.sender
and sr.receiver = ar.receiver
group by 1
order by 1
