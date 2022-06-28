# Write your MySQL query statement below
SELECT user_id,max(time_stamp) as last_stamp
from Logins where time_stamp between '2020-01-01' and '2021-01-01'
group by user_id
order by time_stamp DESC;