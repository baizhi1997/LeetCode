
# @Title: 各位相加 (Add Digits)
# @Author: qinxinlei
# @Date: 2018-10-18 20:55:05
# @Runtime: 136 ms
# @Memory: N/A

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num-1)%9+1 if num else 0
