
-- @Title: 变更性别 (Swap Salary)
-- @Author: qinxinlei
-- @Date: 2018-11-16 19:36:45
-- @Runtime: 297 ms
-- @Memory: N/A

# Write your MySQL query statement below
update salary set sex = CHAR(ASCII('f') ^ ASCII('m') ^ ASCII(sex));
