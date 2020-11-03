
# @Title: 排序矩阵查找 (Sorted Matrix Search LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 21:21:49
# @Runtime: 48 ms
# @Memory: 18 MB

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x, y = len(matrix)-1, 0
        while x >= 0 and y < len(matrix[0]):
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                x -= 1
            else:
                y += 1
        return False
