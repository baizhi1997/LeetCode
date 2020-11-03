
# @Title: 汉明距离 (Hamming Distance)
# @Author: qinxinlei
# @Date: 2018-10-23 22:15:12
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
