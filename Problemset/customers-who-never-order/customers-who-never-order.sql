
-- @Title: 从不订购的客户 (Customers Who Never Order)
-- @Author: qinxinlei
-- @Date: 2018-11-16 15:08:09
-- @Runtime: 222 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT A.Name as Customers from Customers A
WHERE A.Id NOT IN (SELECT B.CustomerId from Orders B)
