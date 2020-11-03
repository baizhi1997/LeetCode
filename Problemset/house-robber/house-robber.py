
# @Title: 打家劫舍 (House Robber)
# @Author: qinxinlei
# @Date: 2018-10-22 21:07:40
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l=len(nums)
        ans=[0]*(l+1)
        ans[1]=nums[0]
        for i in range(2,l+1):
            ans[i]=max(ans[i-2]+nums[i-1],ans[i-1])
        return ans[l]
