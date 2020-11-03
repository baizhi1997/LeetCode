
# @Title: 图像渲染 (Flood Fill)
# @Author: qinxinlei
# @Date: 2018-11-18 22:43:29
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        def dfs(i,j):
            image[i][j]=newColor
            for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=x<m and 0<=y<n and image[x][y]==color:
                    dfs(x,y)
        color,m,n=image[sr][sc],len(image),len(image[0])
        if color!=newColor:
            dfs(sr,sc)
        return image
