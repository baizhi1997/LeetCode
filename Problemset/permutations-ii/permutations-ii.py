
# @Title: 全排列 II (Permutations II)
# @Author: qinxinlei
# @Date: 2018-10-16 15:04:43
# @Runtime: 72 ms
# @Memory: N/A

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        if len(nums)==1:
            return [nums]
        set1=set()
        for i,num in enumerate(nums):
            if num not in set1:
                set1.add(num)
                for j in self.permuteUnique(nums[:i]+nums[i+1:]):
                    ans+=[[num]+j]
        return ans
