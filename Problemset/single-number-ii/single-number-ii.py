
# @Title: 只出现一次的数字 II (Single Number II)
# @Author: qinxinlei
# @Date: 2018-10-16 17:04:07
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=b=0
        for num in nums:
            b=b^num&~a
            a=a^num&~b
        return b
