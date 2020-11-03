
# @Title: 图片平滑器 (Image Smoother)
# @Author: qinxinlei
# @Date: 2018-11-17 15:02:14
# @Runtime: 572 ms
# @Memory: N/A

class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(M)
        n=len(M[0])
        ans=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                tmp=[M[x][y] for x in (i-1,i,i+1) for y in (j-1,j,j+1) if 0<=x<m and 0<=y<n]
                ans[i][j]=sum(tmp)//len(tmp)
        return ans
