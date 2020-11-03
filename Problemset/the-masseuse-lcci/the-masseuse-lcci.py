
# @Title: 按摩师 (The Masseuse LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 13:09:00
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def massage(self, nums: List[int]) -> int:
        dp0, dp1 = 0, 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1
