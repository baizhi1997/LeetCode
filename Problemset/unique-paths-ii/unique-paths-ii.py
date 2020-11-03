
# @Title: 不同路径 II (Unique Paths II)
# @Author: qinxinlei
# @Date: 2018-09-26 21:30:36
# @Runtime: 24 ms
# @Memory: N/A

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        ans=[[0 for col in range(n)] for row in range(m)]
        flag=False
        for i in range(m):    
            if obstacleGrid[i][0]!=0:
                flag=True
            if flag:
                ans[i][0]=0
            else:
                ans[i][0]=1
        flag=False
        for i in range(n):
            if obstacleGrid[0][i]!=0:
                flag=True
            if flag:
                ans[0][i]=0
            else:
                ans[0][i]=1
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==0:
                    ans[i][j]=ans[i-1][j]+ans[i][j-1]
        return ans[m-1][n-1]
