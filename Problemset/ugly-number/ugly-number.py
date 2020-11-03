
# @Title: 丑数 (Ugly Number)
# @Author: qinxinlei
# @Date: 2018-10-03 19:10:15
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        for i in [2,3,5]:
            while num%i==0:
                num/=i
        return num==1
