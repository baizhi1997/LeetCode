
# @Title: 托普利茨矩阵 (Toeplitz Matrix)
# @Author: qinxinlei
# @Date: 2018-11-17 11:37:22
# @Runtime: 48 ms
# @Memory: N/A

class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        tmp=matrix[-1]
        for i in range(1,len(matrix)):
            tmp.append(matrix[-i-1][-1])
            for j in range(len(matrix[0])):
                if matrix[-i-1][-j-1]!=tmp[-j-1]:
                    return False
        return True
