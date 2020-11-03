
# @Title: 连续数列 (Contiguous Sequence LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 18:29:21
# @Runtime: 64 ms
# @Memory: 14 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            ans = max(ans, tmp)
            if tmp < 0:
                tmp = 0
        return ans
