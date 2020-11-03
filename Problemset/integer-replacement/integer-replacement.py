
# @Title: 整数替换 (Integer Replacement)
# @Author: qinxinlei
# @Date: 2018-11-27 21:45:21
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans=0
        while n>1:
            if n%2==0:
                n//=2
            elif n%4==1 or n==3:
                n-=1
            else:
                n+=1
            ans+=1
        return ans
