
# @Title: 搜索旋转排序数组 (Search in Rotated Sorted Array)
# @Author: qinxinlei
# @Date: 2018-09-28 10:25:22
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)/2
            if nums[m]==target:
                return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            if nums[m]<=nums[r]:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return -1

