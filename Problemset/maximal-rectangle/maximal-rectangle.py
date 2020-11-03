
# @Title: 最大矩形 (Maximal Rectangle)
# @Author: qinxinlei
# @Date: 2018-09-29 10:25:42
# @Runtime: 76 ms
# @Memory: N/A

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        n=len(matrix[0])
        h=[0]*(n+1)
        ans=0
        for row in matrix:
            for i in range(n):
                if row[i]=='1':
                    h[i]=h[i]+1 
                else:
                    h[i]=0
            stack=[-1]
            for i in range(n+1):
                while h[i]<h[stack[-1]]:
                    x=h[stack.pop()]
                    y=i-1-stack[-1]
                    ans=max(ans,x*y)
                stack.append(i)
        return ans

