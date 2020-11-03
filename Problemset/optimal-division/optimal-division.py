
# @Title: 最优除法 (Optimal Division)
# @Author: qinxinlei
# @Date: 2018-11-23 16:10:28
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l=len(nums)
        if l==1:
            return str(nums[0])
        if l==2:
            return str(nums[0])+'/'+str(nums[1])
        ans=str(nums[0])+"/("+str(nums[1])
        for num in nums[2:]:
            ans+='/'+str(num)
        return ans+')'
