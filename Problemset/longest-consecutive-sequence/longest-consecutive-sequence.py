
# @Title: 最长连续序列 (Longest Consecutive Sequence)
# @Author: qinxinlei
# @Date: 2019-05-08 20:00:53
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        ans = 0
        for num in nums:
            if num + 1 not in nums:
                cur = 1
                while num - 1 in nums:
                    cur += 1
                    num -= 1
                ans = max(ans, cur)
        return ans
