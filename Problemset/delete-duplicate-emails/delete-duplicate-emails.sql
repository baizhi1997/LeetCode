
-- @Title: 删除重复的电子邮箱 (Delete Duplicate Emails)
-- @Author: qinxinlei
-- @Date: 2018-11-16 15:52:11
-- @Runtime: 516 ms
-- @Memory: N/A

# Write your MySQL query statement below
delete from Person
where Id not in 
(
    select id from
    (
        select min(Id) as id
        from Person
        group by Email
    )a
)
