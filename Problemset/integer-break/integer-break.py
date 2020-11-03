
# @Title: 整数拆分 (Integer Break)
# @Author: qinxinlei
# @Date: 2018-11-24 14:18:20
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        if n==3:
            return 2
        x,y=divmod(n,3)
        if y==0:
            return pow(3,x)
        if y==2:
            return pow(3,x)*2
        return pow(3,x-1)*4
