
# @Title: 矩阵中的幻方 (Magic Squares In Grid)
# @Author: qinxinlei
# @Date: 2018-11-06 13:23:13
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def isMagic(i, j):
            s=''.join(str(grid[i+x//3][j+x%3]) for x in [0,1,2,5,8,7,6,3])
            return grid[i][j]&1==0 and (s in "43816729"*2 or s in "92761834"*2)
        return sum(isMagic(i,j) for i in range(len(grid)-2) for j in range(len(grid[0])-2) if grid[i+1][j+1]==5)
