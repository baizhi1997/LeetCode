
# @Title: 螺旋矩阵 (Spiral Matrix)
# @Author: qinxinlei
# @Date: 2018-09-23 21:49:26
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans=[]
        while matrix:
            ans+=matrix.pop(0)
            matrix[:]=zip(*matrix)[::-1]
        return ans
