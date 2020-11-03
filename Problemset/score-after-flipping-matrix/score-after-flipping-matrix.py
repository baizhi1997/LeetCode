
# @Title: 翻转矩阵后的得分 (Score After Flipping Matrix)
# @Author: qinxinlei
# @Date: 2018-11-21 21:10:45
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m=len(A)
        n=len(A[0])
        for i in range(m):
            if A[i][0]==0:
                for j in range(n):
                    A[i][j]^=1
        ans=0
        i=1
        for row in list(zip(*A))[::-1]:
            x=sum(row)
            ans+=max(x,m-x)*i
            i*=2
        return ans
