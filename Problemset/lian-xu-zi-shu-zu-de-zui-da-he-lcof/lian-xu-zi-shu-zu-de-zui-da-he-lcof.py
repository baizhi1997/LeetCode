
# @Title: 连续子数组的最大和 (连续子数组的最大和  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 21:22:04
# @Runtime: 76 ms
# @Memory: 17.2 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        tmp = 0
        for i in range(len(nums)):
            if tmp > 0:
                tmp += nums[i]
            else:
                tmp = nums[i]
            ans = max(tmp, ans)
        return ans
