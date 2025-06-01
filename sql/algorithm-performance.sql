
--

with rated_search as (
select
    search_id,
    search_term,
    clicked,
    search_results_position,
    case
        -- not clicked, rating = 1
        when clicked = 0  then 1
        when clicked = 1 and search_results_position > 3 then 2
        when clicked = 1 and search_results_position <= 3 then 3
    end as rating
from fb_search_events
)
select
    search_id,
    max(rating)
from rated_search
group by 1