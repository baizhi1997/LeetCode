
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-22 10:49:42
# @Runtime: 56 ms
# @Memory: 16.3 MB

class Solution:
    def minArray(self, nums: List[int]) -> int:
        l = len(nums) - 1
        if l == 0:
            return nums[0]
        m = l // 2
        x = nums[m] - nums[-1]
        if x < 0:
            return self.minArray(nums[:m+1])
        elif x > 0:
            return self.minArray(nums[m+1:])
        return self.minArray(nums[:-1])
