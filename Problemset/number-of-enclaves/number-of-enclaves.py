
# @Title: 飞地的数量 (Number of Enclaves)
# @Author: qinxinlei
# @Date: 2019-04-08 21:14:56
# @Runtime: 92 ms
# @Memory: N/A

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        def dfs(i, j):
            A[i][j] = 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and A[x][y]:
                    dfs(x, y)
        m, n = len(A), len(A[0])
        for i in [0, m-1]:
            for j in range(n):
                if A[i][j]:
                    dfs(i, j)
        for j in [0, n-1]:
            for i in range(m):
                if A[i][j]:
                    dfs(i, j)
        return sum(sum(row) for row in A)
