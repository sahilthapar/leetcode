select
count(1)
from facebook_friendship_requests
where date_part('month', date_approved) in (1, 2)