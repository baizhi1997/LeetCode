
# @Title: 搜索旋转排序数组 II (Search in Rotated Sorted Array II)
# @Author: qinxinlei
# @Date: 2018-09-28 11:48:19
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)/2
            if nums[m]==target:
                return True
            while l<m and nums[l]==nums[m]:
                l+=1
            if nums[l]<=nums[m]:
                if nums[l]<=target<nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
        return False
