
# @Title: 坏了的计算器 (Broken Calculator)
# @Author: qinxinlei
# @Date: 2019-03-05 11:52:05
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans=0
        while Y>X:
            ans+=1
            if Y&1:
                Y+=1
            else:
                Y//=2
        return ans+X-Y
