select
    distinct(fp.*)
from facebook_reactions fr
inner join facebook_posts fp
    on fr.post_id = fp.post_id
where LOWER(fr.reaction) = 'heart';