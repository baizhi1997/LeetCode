
-- @Title: 超过经理收入的员工 (Employees Earning More Than Their Managers)
-- @Author: qinxinlei
-- @Date: 2018-11-16 14:58:53
-- @Runtime: 301 ms
-- @Memory: N/A

# Write your MySQL query statement below
select p1.name as Employee from Employee p1, Employee p2 where p1.ManagerId=p2.Id and p1.Salary>p2.Salary
