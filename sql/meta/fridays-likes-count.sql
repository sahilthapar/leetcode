select
count(1),
date_liked
from likes l
inner join user_posts up
on l.post_id = up.post_id
inner join friendships f
on (l.user_name = f.user_name1 and up.user_name = f.user_name2) or (l.user_name = f.user_name2 and up.user_name = f.user_name1)
group by 2
having EXTRACT(ISODOW FROM l.date_liked) = 5
