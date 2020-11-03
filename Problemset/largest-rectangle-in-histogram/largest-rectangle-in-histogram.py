
# @Title: 柱状图中最大的矩形 (Largest Rectangle in Histogram)
# @Author: qinxinlei
# @Date: 2018-09-28 21:14:56
# @Runtime: 132 ms
# @Memory: N/A

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        s=[-1]
        ans=0
        for i in range(len(heights)):
            while heights[i]<heights[s[-1]]:
                x=heights[s.pop()]
                y=i-1-s[-1]
                ans=max(ans,x*y)
            s.append(i)
        return ans

