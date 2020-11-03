
# @Title: 位1的个数 (Number of 1 Bits)
# @Author: qinxinlei
# @Date: 2018-11-10 13:29:09
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        return bin(n).count('1')
