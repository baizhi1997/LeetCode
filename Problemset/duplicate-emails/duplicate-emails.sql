
-- @Title: 查找重复的电子邮箱 (Duplicate Emails)
-- @Author: qinxinlei
-- @Date: 2018-11-16 15:00:20
-- @Runtime: 171 ms
-- @Memory: N/A

# Write your MySQL query statement below
select Email
from Person
group by Email
having count(*) > 1;
