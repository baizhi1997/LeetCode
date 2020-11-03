
# @Title: 消失的数字 (Missing Number LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 14:26:56
# @Runtime: 56 ms
# @Memory: 14.3 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            res ^= i
            res ^=nums[i]
        res ^= len(nums)
        return res

