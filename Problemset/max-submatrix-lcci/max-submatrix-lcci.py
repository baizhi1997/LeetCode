
# @Title: 最大子矩阵 (Max Submatrix LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 21:43:23
# @Runtime: 2748 ms
# @Memory: 15.2 MB

class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        N, M = len(matrix), len(matrix[0])
        cols = [[0] * (N + 1) for _ in range(M)]
        for r in range(N):
            for c in range(M):
                cols[c][r + 1] = cols[c][r] + matrix[r][c]
        res, max_s = None, float('-inf')
        for r1 in range(N):
            for r2 in range(r1, N):
                c1 = 0
                cur = 0
                for c2 in range(M):
                    cur += cols[c2][r2 + 1] - cols[c2][r1]
                    if cur > max_s:
                        max_s = cur
                        res = [r1, c1, r2, c2]
                    if cur <= 0:
                        cur = 0
                        c1 = c2 + 1
        return res
