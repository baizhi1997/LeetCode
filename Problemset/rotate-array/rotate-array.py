
# @Title: 旋转数组 (Rotate Array)
# @Author: qinxinlei
# @Date: 2018-10-08 20:23:29
# @Runtime: 40 ms
# @Memory: N/A

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=-k%(len(nums))
        nums[:]=nums[k:]+nums[:k]
