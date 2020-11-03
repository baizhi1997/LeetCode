
# @Title: 0～n-1中缺失的数字 (缺失的数字  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 13:40:18
# @Runtime: 52 ms
# @Memory: 14.4 MB

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] == m: i = m + 1
            else: j = m - 1
        return i

