
-- @Title: 换座位 (Exchange Seats)
-- @Author: qinxinlei
-- @Date: 2020-06-17 22:04:23
-- @Runtime: 209 ms
-- @Memory: 0 B

# Write your MySQL query statement below
select 
    if(id%2=0,
        id-1,
        if(id=(select count(distinct id) from seat),
            id,
            id+1)) 
    as id,student 
from seat 
order by id;

