with matched_messages as (
    select s.message_id as sender_msg_id, r.message_id as receiver_msg_id from facebook_messages_sent s
    left join facebook_messages_received r
    on s.message_id = r.message_id
) Select count(receiver_msg_id) / cast(count(sender_msg_id) as decimal) as success_ratio
from matched_messages;