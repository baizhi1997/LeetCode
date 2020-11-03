
# @Title: 二维数组中的查找 (二维数组中的查找 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 14:28:43
# @Runtime: 48 ms
# @Memory: 17.1 MB

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True
        return False

