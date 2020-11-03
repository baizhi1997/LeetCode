
# @Title: 寻找旋转排序数组中的最小值 (Find Minimum in Rotated Sorted Array)
# @Author: qinxinlei
# @Date: 2019-05-22 23:10:49
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums) - 1
        if l == 0:
            return nums[0]
        m = l // 2
        if nums[m] < nums[-1]:
            return self.findMin(nums[:m+1])
        return self.findMin(nums[m+1:])
