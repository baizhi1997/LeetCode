
# @Title: 三维形体的表面积 (Surface Area of 3D Shapes)
# @Author: qinxinlei
# @Date: 2018-11-16 20:04:34
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return sum(v*4+2 for row in grid for v in row if v)-sum(min(a,b)*2 for row in (grid+list(zip(*grid))) for a,b in zip(row,row[1:]))
