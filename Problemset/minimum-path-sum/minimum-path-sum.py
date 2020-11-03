
# @Title: 最小路径和 (Minimum Path Sum)
# @Author: qinxinlei
# @Date: 2018-09-26 18:54:35
# @Runtime: 32 ms
# @Memory: N/A

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n=len(grid),len(grid[0])
        for i in range(1,m):
            grid[i][0]+=grid[i-1][0]
        for i in range(1,n):
            grid[0][i]+=grid[0][i-1]
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i-1][j],grid[i][j-1])
        return grid[m-1][n-1]

