
# @Title: 打家劫舍 II (House Robber II)
# @Author: qinxinlei
# @Date: 2018-12-14 16:38:52
# @Runtime: 36 ms
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
        if l==1:
            return nums[0]
        ans1=[0]*l
        ans2=[0]*l
        ans1[1]=nums[0]
        ans2[1]=nums[1]
        for i in range(2,l):
            ans1[i]=max(ans1[i-2]+nums[i-1],ans1[i-1])
            ans2[i]=max(ans2[i-2]+nums[i],ans2[i-1])
        return max(ans1[l-1],ans2[l-1])
