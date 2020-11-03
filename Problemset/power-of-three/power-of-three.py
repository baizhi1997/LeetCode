
# @Title: 3的幂 (Power of Three)
# @Author: qinxinlei
# @Date: 2018-10-03 20:34:15
# @Runtime: 140 ms
# @Memory: N/A

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and 1162261467%n==0
