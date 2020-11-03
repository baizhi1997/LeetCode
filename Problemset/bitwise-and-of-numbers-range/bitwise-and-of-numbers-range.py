
# @Title: 数字范围按位与 (Bitwise AND of Numbers Range)
# @Author: qinxinlei
# @Date: 2019-01-19 14:23:04
# @Runtime: 520 ms
# @Memory: N/A

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i=0
        while m!=n:
            m>>=1
            n>>=1
            i+=1
        return m<<i
