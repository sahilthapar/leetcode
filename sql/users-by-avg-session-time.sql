-- find users start time
-- find users end time
-- find the difference

with starts as
(select user_id, date(timestamp) as date_ts, max(timestamp) as timestamp from facebook_web_log where action = 'page_load' group by 1, 2),
ends as
(select user_id, date(timestamp) as date_ts, min(timestamp) as timestamp from facebook_web_log where action = 'page_exit' group by 1, 2)
select starts.user_id, avg(ends.timestamp-starts.timestamp) as session_duration
from starts
inner join ends
on starts.user_id = ends.user_id
and date(starts.timestamp) = date (ends.timestamp)
group by 1;