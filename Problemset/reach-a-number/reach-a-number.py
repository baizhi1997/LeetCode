
# @Title: 到达终点数字 (Reach a Number)
# @Author: qinxinlei
# @Date: 2018-10-15 10:42:26
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target=abs(target)
        x=math.ceil((2*target+0.25)**0.5-0.5)
        return x if (x*(x+1)/2-target)%2==0 else x+1+x%2
