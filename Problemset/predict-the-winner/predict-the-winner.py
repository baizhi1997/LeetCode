
# @Title: 预测赢家 (Predict the Winner)
# @Author: qinxinlei
# @Date: 2018-10-26 17:17:29
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp=[]
        for r in range(len(nums)):
            dp.append(nums[r])
            for l in range(r)[::-1]:
                dp[l]=max(nums[r]-dp[l],nums[l]-dp[l+1])
        return dp[0]>=0
[l],nums[l]-dp[l+1])
        return dp[0]>=0
