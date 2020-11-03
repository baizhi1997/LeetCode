
# @Title: 最短无序连续子数组 (Shortest Unsorted Continuous Subarray)
# @Author: qinxinlei
# @Date: 2018-11-16 19:09:52
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=sorted(nums)
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]!=x[i]:
                break
            i+=1
        while j>=i:
            if nums[j]!=x[j]:
                break
            j-=1
        return j-i+1
