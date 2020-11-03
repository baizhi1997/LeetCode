
# @Title: 岛屿数量 (Number of Islands)
# @Author: qinxinlei
# @Date: 2019-05-17 14:37:28
# @Runtime: 76 ms
# @Memory: N/A

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or j < 0 or i >= self.n or j >= self.m or grid[i][j] != '1':
                return
            grid[i][j] = '*'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        if not grid:
            return 0
        ans = 0
        self.n, self.m = len(grid), len(grid[0])
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
