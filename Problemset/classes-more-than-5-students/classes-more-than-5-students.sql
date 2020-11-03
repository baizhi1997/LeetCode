
-- @Title: 超过5名学生的课 (Classes More Than 5 Students)
-- @Author: qinxinlei
-- @Date: 2018-11-16 19:19:23
-- @Runtime: 1577 ms
-- @Memory: N/A

# Write your MySQL query statement below
select class from courses group by class having count(distinct student) >= 5;
