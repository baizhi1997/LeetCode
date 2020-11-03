
# @Title: 灯泡开关 Ⅱ (Bulb Switcher II)
# @Author: qinxinlei
# @Date: 2018-10-23 22:43:56
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m==0 or n==0:
            return 1
        if n==1:
            return 2
        if n==2:
            if m==1:
                return 3
            return 4
        if n>=3:
            if m==1:
                return 4
            if m==2:
                return 7
        return 8
