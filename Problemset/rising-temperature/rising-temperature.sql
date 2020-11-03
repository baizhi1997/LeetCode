
-- @Title: 上升的温度 (Rising Temperature)
-- @Author: qinxinlei
-- @Date: 2018-11-16 16:11:13
-- @Runtime: 296 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT a.Id FROM Weather AS a, Weather AS b
WHERE DATEDIFF(a.RecordDate, b.RecordDate)=1 AND a.Temperature > b.Temperature
