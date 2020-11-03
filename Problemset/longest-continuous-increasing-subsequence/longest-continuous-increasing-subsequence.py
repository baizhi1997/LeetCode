
# @Title: 最长连续递增序列 (Longest Continuous Increasing Subsequence)
# @Author: qinxinlei
# @Date: 2018-11-17 16:17:12
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        tmp=0
        pre=math.inf
        nums.append(-math.inf)
        for num in nums:
            if num>pre:
                tmp+=1
            else:
                ans=max(ans,tmp)
                tmp=1
            pre=num
        return ans
