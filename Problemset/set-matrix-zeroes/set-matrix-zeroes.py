
# @Title: 矩阵置零 (Set Matrix Zeroes)
# @Author: qinxinlei
# @Date: 2018-11-14 21:18:12
# @Runtime: 100 ms
# @Memory: N/A

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flag1 = False
        flag2 = False
        for i in range(len(matrix[0])):
            if matrix[0][i] == 0:
                flag1 = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                flag2 = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if flag1:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if flag2:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        return matrix
