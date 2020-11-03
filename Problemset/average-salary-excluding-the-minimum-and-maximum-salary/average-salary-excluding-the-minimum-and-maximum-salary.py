
# @Title: 去掉最低工资和最高工资后的工资平均值 (Average Salary Excluding the Minimum and Maximum Salary)
# @Author: qinxinlei
# @Date: 2020-07-31 13:31:30
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def average(self, salary: List[int]) -> float:
        return (sum(salary)-max(salary)-min(salary))/(len(salary)-2)
