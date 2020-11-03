
# @Title: 最大三角形面积 (Largest Triangle Area)
# @Author: qinxinlei
# @Date: 2018-10-05 16:38:10
# @Runtime: 76 ms
# @Memory: N/A

class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max(0.5*abs((y1-x1)*(z2-x2)-(z1-x1)*(y2-x2)) for (x1,x2),(y1,y2),(z1,z2) in itertools.combinations(points,3))
