
# @Title: 平方数之和 (Sum of Square Numbers)
# @Author: qinxinlei
# @Date: 2018-10-04 13:27:40
# @Runtime: 68 ms
# @Memory: N/A

class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        l=0
        r=int(c**0.5)
        while l<=r:
            t=l*l+r*r
            if t==c:
                return True
            elif t<c:
                l+=1
            else:
                r-=1
        return False
