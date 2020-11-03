
# @Title: 统计有序矩阵中的负数 (Count Negative Numbers in a Sorted Matrix)
# @Author: qinxinlei
# @Date: 2020-07-28 15:46:35
# @Runtime: 52 ms
# @Memory: 14 MB

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        m, n = len(grid), len(grid[0])
        j = n-1
        for i in range(m):
            while grid[i][j] < 0 and j > -1:
                j -= 1
            if j == -1:
                break
            ans += (j+1)
        return m*n-ans

