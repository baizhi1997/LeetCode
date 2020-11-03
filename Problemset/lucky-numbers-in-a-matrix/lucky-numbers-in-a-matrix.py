
# @Title: 矩阵中的幸运数 (Lucky Numbers in a Matrix)
# @Author: qinxinlei
# @Date: 2020-07-29 15:51:38
# @Runtime: 84 ms
# @Memory: 13.5 MB

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        r, c = len(matrix), len(matrix[0])
        rMin, cMax = [10**9] * r, [0] * c
        for i in range(r):
            for j in range(c):
                rMin[i] = min(rMin[i], matrix[i][j])
                cMax[j] = max(cMax[j], matrix[i][j])
        
        ans = list()
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == rMin[i] and matrix[i][j] == cMax[j]:
                    ans.append(matrix[i][j])
        return ans

