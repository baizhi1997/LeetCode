
# @Title: 礼物的最大价值 (礼物的最大价值 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-17 16:16:29
# @Runtime: 80 ms
# @Memory: 14.7 MB

class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += max(grid[i][j-1], grid[i-1][j])
        return grid[m-1][n-1]
