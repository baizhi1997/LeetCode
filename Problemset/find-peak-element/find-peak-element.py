
# @Title: 寻找峰值 (Find Peak Element)
# @Author: qinxinlei
# @Date: 2018-11-29 15:46:51
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[m+1]:
                l=m+1
            else:
                r=m
        return r
