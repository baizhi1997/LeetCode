
# @Title: 矩阵对角线元素的和 (Matrix Diagonal Sum)
# @Author: qinxinlei
# @Date: 2020-10-28 22:53:17
# @Runtime: 36 ms
# @Memory: 13.7 MB

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        ans = 0
        for i in range(m):
            if i != m-1-i:
                ans += mat[i][i] + mat[i][m-1-i]
            else:
                ans += mat[i][i]
        return ans
