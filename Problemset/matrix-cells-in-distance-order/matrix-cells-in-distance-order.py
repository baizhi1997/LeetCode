
# @Title: 距离顺序排列矩阵单元格 (Matrix Cells in Distance Order)
# @Author: qinxinlei
# @Date: 2019-06-24 22:16:24
# @Runtime: 264 ms
# @Memory: N/A

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([[x, y] for x in range(R) for y in range(C)], key = lambda x: abs(x[0]-r0) + abs(x[1]-c0))
