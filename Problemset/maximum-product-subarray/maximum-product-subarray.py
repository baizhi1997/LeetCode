
# @Title: 乘积最大子数组 (Maximum Product Subarray)
# @Author: qinxinlei
# @Date: 2019-05-17 13:31:34
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tmp = nums[::-1]
        for i in range(1, len(nums)):
            nums[i] *= nums[i - 1] or 1
            tmp[i] *= tmp[i - 1] or 1
        return max(tmp + nums)
