
# @Title: 岛屿的周长 (Island Perimeter)
# @Author: qinxinlei
# @Date: 2018-10-20 13:04:13
# @Runtime: 240 ms
# @Memory: N/A

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    if i==0 or grid[i-1][j]==0:
                        ans+=2
                    if j==0 or grid[i][j-1]==0:
                        ans+=2
        return ans
