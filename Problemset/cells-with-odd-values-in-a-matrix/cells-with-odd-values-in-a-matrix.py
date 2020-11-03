
# @Title: 奇数值单元格的数目 (Cells with Odd Values in a Matrix)
# @Author: qinxinlei
# @Date: 2020-07-28 16:08:40
# @Runtime: 60 ms
# @Memory: 13.4 MB

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        rows = [False] * n
        cols = [False] * m
        for r, c in indices:
            rows[r] = not rows[r]
            cols[c] = not cols[c]
        rows_true = rows.count(True)
        rows_false = n - rows_true
        cols_true = cols.count(True)
        cols_false = m - cols_true
        return rows_true * cols_false + rows_false * cols_true
