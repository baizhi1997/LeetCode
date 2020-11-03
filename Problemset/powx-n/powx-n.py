
# @Title: Pow(x, n) (Pow(x, n))
# @Author: qinxinlei
# @Date: 2018-10-16 12:37:18
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        ans=1
        if n<0:
            n=-1*n
            x=1/x
        while n:
            if n%2:
                ans*=x
            x*=x
            n//=2
        return ans
