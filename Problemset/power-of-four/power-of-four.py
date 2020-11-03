
# @Title: 4的幂 (Power of Four)
# @Author: qinxinlei
# @Date: 2018-10-07 16:01:41
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        tmp=1
        while tmp<num:
            tmp*=4
        return num==tmp
