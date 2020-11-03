
# @Title: 使用最小花费爬楼梯 (Min Cost Climbing Stairs)
# @Author: qinxinlei
# @Date: 2018-10-26 18:20:27
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        a,b=0,0
        for i in cost:
            a,b=b,min(a,b)+i
        return min(a,b)
