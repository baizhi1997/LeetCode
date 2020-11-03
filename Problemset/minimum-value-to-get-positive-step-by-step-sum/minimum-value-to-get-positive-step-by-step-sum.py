
# @Title: 逐步求和得到正数的最小值 (Minimum Value to Get Positive Step by Step Sum)
# @Author: qinxinlei
# @Date: 2020-07-31 16:06:55
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        premin = float('inf')
        tmp = 0
        for num in nums:
            tmp += num
            premin = min(tmp, premin)
        return 1 if premin > -1 else 1 - premin
