
# @Title: 顺时针打印矩阵 (顺时针打印矩阵  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 12:56:24
# @Runtime: 64 ms
# @Memory: 13.5 MB

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
        return res
