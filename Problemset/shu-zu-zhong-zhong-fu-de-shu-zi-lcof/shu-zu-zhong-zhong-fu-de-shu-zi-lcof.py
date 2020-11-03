
# @Title: 数组中重复的数字 (数组中重复的数字 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:15:33
# @Runtime: 40 ms
# @Memory: 22.6 MB

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        set1 = set()
        for n in nums:
            if n in set1:
                return n
            set1.add(n)
