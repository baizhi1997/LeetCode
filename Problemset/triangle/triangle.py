
# @Title: 三角形最小路径和 (Triangle)
# @Author: qinxinlei
# @Date: 2019-01-03 21:49:24
# @Runtime: 68 ms
# @Memory: N/A

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-1,0,-1):
            for j in range(i):
                triangle[i-1][j]+=min(triangle[i][j],triangle[i][j+1])
        return triangle[0][0]
