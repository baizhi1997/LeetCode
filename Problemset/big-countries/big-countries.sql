
-- @Title: 大的国家 (Big Countries)
-- @Author: qinxinlei
-- @Date: 2018-11-16 19:16:53
-- @Runtime: 1711 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT name, population, area
FROM World
WHERE area > 3000000 

UNION

SELECT name, population, area
FROM World
WHERE population > 25000000
