# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below
delete from Person where Id not in (SELECT *from(select min(id) from Person group by email) as s)