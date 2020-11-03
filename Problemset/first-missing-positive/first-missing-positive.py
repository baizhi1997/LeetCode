
# @Title: 缺失的第一个正数 (First Missing Positive)
# @Author: qinxinlei
# @Date: 2018-09-23 19:40:10
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]-1<len(nums) and nums[i]>0 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
            else:
                i+=1
        for i,num in enumerate(nums):
            if num!=i+1:
                return i+1
        return len(nums)+1
