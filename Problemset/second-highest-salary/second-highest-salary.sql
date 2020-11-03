
-- @Title: 第二高的薪水 (Second Highest Salary)
-- @Author: qinxinlei
-- @Date: 2018-11-16 14:40:13
-- @Runtime: 136 ms
-- @Memory: N/A

# Write your MySQL query statement below
select max(salary) as SecondHighestSalary
from employee
where salary < (select max(salary) from employee);
