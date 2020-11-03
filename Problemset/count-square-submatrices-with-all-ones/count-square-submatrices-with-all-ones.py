
# @Title: 统计全为 1 的正方形子矩阵 (Count Square Submatrices with All Ones)
# @Author: qinxinlei
# @Date: 2020-06-17 09:33:53
# @Runtime: 844 ms
# @Memory: 15.3 MB

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                matrix[i][j] *= min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
        return sum(map(sum, matrix))
