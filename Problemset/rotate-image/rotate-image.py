
# @Title: 旋转图像 (Rotate Image)
# @Author: qinxinlei
# @Date: 2018-09-23 19:51:20
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=zip(*matrix[::-1])
