
# @Title: 2的幂 (Power of Two)
# @Author: qinxinlei
# @Date: 2018-10-03 17:50:18
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return False
        while n%2==0:
            n/=2
        return n==1
