-- use a sub_query to find out like facebook_reactions and then find all relevant posts

select count(*) from (
select distinct p.post_id from facebook_posts p
inner join facebook_reactions r
on p.post_id = r.post_id
and r.reaction = 'like'
) a