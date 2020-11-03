
# @Title: 每日温度 (Daily Temperatures)
# @Author: qinxinlei
# @Date: 2018-11-23 15:22:08
# @Runtime: 292 ms
# @Memory: N/A

class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ans=[0]*len(T)
        stack=[]
        for i,t in enumerate(T):
            while stack and T[stack[-1]]<t:
                p=stack.pop()
                ans[p]=i-p
            stack.append(i)
        return ans
