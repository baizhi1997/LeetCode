
# @Title: 矩形重叠 (Rectangle Overlap)
# @Author: qinxinlei
# @Date: 2018-10-05 11:28:56
# @Runtime: 20 ms
# @Memory: N/A

class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        def f(x1,x2,y1,y2):
            return y1<=x1<y2 or x1<=y1<x2
        return f(rec1[0],rec1[2],rec2[0],rec2[2]) and f(rec1[1],rec1[3],rec2[1],rec2[3])
