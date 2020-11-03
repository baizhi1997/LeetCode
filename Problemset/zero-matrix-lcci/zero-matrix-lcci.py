
# @Title: 零矩阵 (Zero Matrix LCCI)
# @Author: qinxinlei
# @Date: 2020-06-22 23:22:53
# @Runtime: 52 ms
# @Memory: 13.6 MB

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        x, y = -1, -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    x = i
                    y = j
                    break
            else:
                continue
            break
        if x == -1:
            return matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[x][j] = 0
                    matrix[i][y] = 0
        for i in range(m):
            if matrix[i][y] == 0 and i != x:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(n):
            if matrix[x][j] == 0 and j != y:
                for i in range(m):
                    matrix[i][j] = 0
        for i in range(m):
            matrix[i][y] = 0
        for j in range(n):
            matrix[x][j] = 0
        return matrix
