
# @Title: 螺旋矩阵 II (Spiral Matrix II)
# @Author: qinxinlei
# @Date: 2018-09-26 21:29:53
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ans=[[0 for col in range(n)] for row in range(n)]
        list_n=list(range(n**2,0,-1))
        i=0
        while list_n:
            for j in range(i,n-i):
                ans[i][j]=list_n.pop()
            for j in range(i+1,n-i):
                ans[j][n-i-1]=list_n.pop()
            for j in range(n-i-2,i-1,-1):
                ans[n-i-1][j]=list_n.pop()
            for j in range(n-i-2,i,-1):
                ans[j][i]=list_n.pop()
            i+=1
        return ans

