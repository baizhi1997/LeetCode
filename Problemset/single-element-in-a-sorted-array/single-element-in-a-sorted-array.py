
# @Title: 有序数组中的单一元素 (Single Element in a Sorted Array)
# @Author: qinxinlei
# @Date: 2018-10-25 18:53:32
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=(len(nums)-1)//2
        if m==0:
            return nums[0]
        if nums[m]==nums[m-1]:
            if m&1:
                return self.singleNonDuplicate(nums[m+1:])  
            else:
                return self.singleNonDuplicate(nums[:m-1])
        if nums[m]==nums[m+1]:
            if m&1:
                return self.singleNonDuplicate(nums[:m])      
            else:
                return self.singleNonDuplicate(nums[m+2:])
        return nums[m]
