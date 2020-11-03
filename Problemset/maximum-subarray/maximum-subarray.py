
# @Title: 最大子序和 (Maximum Subarray)
# @Author: qinxinlei
# @Date: 2018-09-23 20:24:25
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        ans=nums[0]
        add=0
        for i in range(len(nums)):
            add+=nums[i]
            if add>ans:
                ans=add
            if add<=0:
                add=0
        return ans
