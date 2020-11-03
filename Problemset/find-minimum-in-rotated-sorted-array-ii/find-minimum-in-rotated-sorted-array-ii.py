
# @Title: 寻找旋转排序数组中的最小值 II (Find Minimum in Rotated Sorted Array II)
# @Author: qinxinlei
# @Date: 2019-05-22 23:20:03
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = len(nums) - 1
        if l == 0:
            return nums[0]
        m = l // 2
        if nums[m] < nums[-1]:
            return self.findMin(nums[:m+1])
        elif nums[m] == nums[-1]:
            return self.findMin(nums[:-1])
        else:
            return self.findMin(nums[m+1:])
