
# @Title: 最佳直线 (Best Line LCCI)
# @Author: qinxinlei
# @Date: 2020-07-14 23:19:23
# @Runtime: 264 ms
# @Memory: 13.6 MB

class Solution:
    def bestLine(self, points: List[List[int]]) -> List[int]:
        n = len(points)
        def gcd(a, b):
            while a:
                a, b = b % a, a
            return b
        max_points, res = 0, None
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                g = gcd(dx, dy)
                slope = (dx // g, dy // g)
                if slope in slopes:
                    slopes[slope][0] += 1
                else:
                    slopes[slope] = [1, (i, j)]
                if slopes[slope][0] > max_points:
                    max_points = slopes[slope][0]
                    res = slopes[slope][1]
        return res

