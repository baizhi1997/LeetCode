
# @Title: 子集 (Subsets)
# @Author: qinxinlei
# @Date: 2018-09-28 15:21:44
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        for i in range(len(nums)+1):
            ans+=itertools.combinations(nums,i)
        return ans
     return ans
