
# @Title: 只出现一次的数字 (Single Number)
# @Author: qinxinlei
# @Date: 2020-05-14 13:46:59
# @Runtime: 52 ms
# @Memory: 15 MB

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            ans = ans ^ n
        return ans
