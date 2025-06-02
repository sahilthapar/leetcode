with max_steps as (
select feature_id, user_id, max(step_reached) as step_reached
from facebook_product_features_realizations
group by 1, 2
), completion as (
    select
    f.feature_id,
    coalesce(s.step_reached, 0) / cast(f.n_steps as decimal) * 100 as pct_completion
    from facebook_product_features f
    left join max_steps s
    on f.feature_id = s.feature_id
)
select feature_id, avg(pct_completion) from completion group by 1;