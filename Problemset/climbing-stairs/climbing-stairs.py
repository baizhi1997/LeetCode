
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: qinxinlei
# @Date: 2018-10-04 20:44:50
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        pre,ans=0,1
        for _ in range(n):
            pre,ans=ans,pre+ans
        return ans
