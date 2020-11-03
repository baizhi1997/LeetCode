
# @Title: 非递减数列 (Non-decreasing Array)
# @Author: qinxinlei
# @Date: 2018-10-23 19:41:58
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        k=1
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:   
                k-=1
                if k<0:
                    return False
                if i<2 or nums[i-2]<=nums[i]:
                    nums[i-1]=nums[i]
                else:
                    nums[i]=nums[i-1]
        return True
