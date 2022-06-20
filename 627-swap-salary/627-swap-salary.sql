# Write your MySQL query statement below
update salary set sex= char(ascii('f') + ascii('m') - ascii(sex));