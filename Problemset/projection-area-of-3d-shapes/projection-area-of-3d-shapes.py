
# @Title: 三维形体投影面积 (Projection Area of 3D Shapes)
# @Author: qinxinlei
# @Date: 2018-11-16 19:46:58
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return len(grid)**2-sum(x.count(0) for x in grid)+sum(map(max,grid))+sum(map(max,list(zip(*grid))))
