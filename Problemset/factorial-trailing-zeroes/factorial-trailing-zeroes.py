
# @Title: 阶乘后的零 (Factorial Trailing Zeroes)
# @Author: qinxinlei
# @Date: 2018-10-03 15:39:38
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n:
            n/=5
            ans+=n
        return ans
    
