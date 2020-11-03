
# @Title: 岛屿的最大面积 (Max Area of Island)
# @Author: qinxinlei
# @Date: 2018-10-13 21:30:50
# @Runtime: 116 ms
# @Memory: N/A

class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        seen=set()
        m=len(grid)
        n=len(grid[0])
        def area(r,c):
            if 0<=r<m and 0<=c<n and grid[r][c] and (r,c) not in seen:
                seen.add((r,c))
                return (1+area(r+1,c)+area(r-1,c)+area(r,c-1)+area(r,c+1))
            return 0
        return max(area(r,c) for r in range(m) for c in range(n))
