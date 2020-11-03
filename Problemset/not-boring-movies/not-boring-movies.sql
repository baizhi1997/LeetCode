
-- @Title: 有趣的电影 (Not Boring Movies)
-- @Author: qinxinlei
-- @Date: 2018-11-16 19:27:20
-- @Runtime: 142 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT * FROM cinema WHERE (id % 2 = 1) AND (description <> 'boring') ORDER BY rating DESC
