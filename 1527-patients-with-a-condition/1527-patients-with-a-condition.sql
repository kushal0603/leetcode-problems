# Write your MySQL query statement below
select * from Patients where conditions REGEXP " DIAB1" or conditions LIKE "DIAB1%";