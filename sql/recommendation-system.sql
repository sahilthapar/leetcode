-- find all pages that a user's friends follows
-- remove pages that user follows already
select
    distinct f.user_id, p.page_id
from users_friends f
join users_pages p
    on f.friend_id = p.user_id
where not exists (
    select * from users_pages p2 where f.user_id = p2.user_id and p.page_id = p2.page_id
)
