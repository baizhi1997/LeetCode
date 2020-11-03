
# @Title: 非递增顺序的最小子序列 (Minimum Subsequence in Non-Increasing Order)
# @Author: qinxinlei
# @Date: 2020-07-31 12:59:20
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        tmp = sum(nums)/2.0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            tmp -= nums[i]
            if tmp < 0:
                return nums[:i+1]

