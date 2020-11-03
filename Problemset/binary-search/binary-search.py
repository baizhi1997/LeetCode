
# @Title: 二分查找 (Binary Search)
# @Author: qinxinlei
# @Date: 2018-11-01 15:09:35
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i=bisect.bisect_left(nums,target)
        return i if i<len(nums) and nums[i]==target else -1
