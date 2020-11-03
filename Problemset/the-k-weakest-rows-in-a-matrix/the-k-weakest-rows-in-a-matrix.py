
# @Title: 方阵中战斗力最弱的 K 行 (The K Weakest Rows in a Matrix)
# @Author: qinxinlei
# @Date: 2020-08-02 14:30:26
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return sorted(list(range(len(mat))), key=lambda x:(sum(mat[x]), x))[:k]
