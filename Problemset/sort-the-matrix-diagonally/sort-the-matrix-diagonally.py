
# @Title: 将矩阵按对角线排序 (Sort the Matrix Diagonally)
# @Author: qinxinlei
# @Date: 2020-06-03 20:24:19
# @Runtime: 96 ms
# @Memory: 13.2 MB

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        dic = {}
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i-j in dic:
                    dic[i-j].append(mat[i][j])
                else:
                    dic[i-j] = [mat[i][j]]
        for k in dic:
            dic[k] = sorted(dic[k], reverse=True)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = dic[i-j].pop()
        return mat
