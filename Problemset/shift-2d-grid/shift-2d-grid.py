
# @Title: 二维网格迁移 (Shift 2D Grid)
# @Author: qinxinlei
# @Date: 2020-08-02 15:44:02
# @Runtime: 200 ms
# @Memory: 13.5 MB

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
        num_rows = len(grid)
        num_cols = len(grid[0])
        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col + k) % num_cols
                wrap_around_count = (col + k) // num_cols
                new_row = (row + wrap_around_count) % num_rows
                new_grid[new_row][new_col] = grid[row][col]
        return new_grid

