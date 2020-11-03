
# @Title: 二进制矩阵中的特殊位置 (Special Positions in a Binary Matrix)
# @Author: qinxinlei
# @Date: 2020-10-28 23:02:57
# @Runtime: 40 ms
# @Memory: 13.7 MB

class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        cols = [sum(num) for num in mat]
        rows = [sum(num) for num in zip(*mat)]
        return sum(rows[mat[i].index(1)]==1 for i in range(len(cols)) if cols[i]==1)

