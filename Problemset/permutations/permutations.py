
# @Title: 全排列 (Permutations)
# @Author: qinxinlei
# @Date: 2018-10-16 14:49:12
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        if len(nums)==1:
            return [nums]
        for i,num in enumerate(nums):
            for j in self.permute(nums[:i]+nums[i+1:]):
                ans+=[[num]+j]
        return ans
