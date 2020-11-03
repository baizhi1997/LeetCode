
-- @Title: 组合两个表 (Combine Two Tables)
-- @Author: qinxinlei
-- @Date: 2018-11-14 21:52:55
-- @Runtime: 203 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT Person.FirstName, Person.LastName, Address.City, Address.State from Person LEFT JOIN Address on Person.PersonId = Address.PersonId;
