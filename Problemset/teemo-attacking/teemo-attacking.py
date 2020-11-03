
# @Title: 提莫攻击 (Teemo Attacking)
# @Author: qinxinlei
# @Date: 2018-11-30 22:27:23
# @Runtime: 64 ms
# @Memory: N/A

class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        ans=0
        pre=-math.inf
        for time in timeSeries:
            if time-pre>duration:
                ans+=duration
            else:
                ans+=time-pre
            pre=time
        return ans
