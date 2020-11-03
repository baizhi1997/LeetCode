
# @Title: 保持城市天际线 (Max Increase to Keep City Skyline)
# @Author: qinxinlei
# @Date: 2018-11-19 15:11:53
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=0
        m,n=len(grid),len(grid[0])
        max_m=[max(row) for row in grid]
        max_n=[max(col) for col in zip(*grid)]
        for i in range(m):
            for j in range(n):
                ans+=(min(max_m[i],max_n[j])-grid[i][j])
        return ans
