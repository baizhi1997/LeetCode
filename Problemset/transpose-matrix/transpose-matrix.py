
# @Title: 转置矩阵 (Transpose Matrix)
# @Author: qinxinlei
# @Date: 2018-10-18 21:30:49
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return zip(*A)
