
# @Title: 有效的完全平方数 (Valid Perfect Square)
# @Author: qinxinlei
# @Date: 2018-10-03 21:07:15
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r=1,num
        while l<r:
            m=(l+r)/2
            if m**2<num:
                l=m+1
            else:
                r=m
        return l**2==num
