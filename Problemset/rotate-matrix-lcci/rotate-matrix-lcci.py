
# @Title: 旋转矩阵 (Rotate Matrix LCCI)
# @Author: qinxinlei
# @Date: 2020-06-02 18:21:13
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])
