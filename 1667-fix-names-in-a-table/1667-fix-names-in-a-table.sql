# Write your MySQL query statement below
SELECT user_id,CONCAT(UPPER(LEFT(name,1)),SUBSTR(LOWER(name),2,LENGTH(name))) AS name FROM Users
ORDER BY user_id;