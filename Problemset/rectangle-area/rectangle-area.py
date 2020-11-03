
# @Title: 矩形面积 (Rectangle Area)
# @Author: qinxinlei
# @Date: 2018-11-27 22:08:35
# @Runtime: 108 ms
# @Memory: N/A

class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        l=max(A,E)
        r=max(min(C,G),l)
        b=max(B,F)
        t=max(min(D,H),b)
        return (C-A)*(D-B)+(G-E)*(H-F)-(r-l)*(t-b)
