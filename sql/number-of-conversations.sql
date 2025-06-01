with all_convos as (
    select message_sender_id as u1, message_receiver_id as u2 from whatsapp_messages
    UNION
    select message_receiver_id as u1, message_sender_id as u2 from whatsapp_messages
)
select count(*) from all_convos
where u1 < u2
