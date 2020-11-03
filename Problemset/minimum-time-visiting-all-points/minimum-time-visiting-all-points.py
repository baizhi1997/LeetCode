
# @Title: 访问所有点的最小时间 (Minimum Time Visiting All Points)
# @Author: qinxinlei
# @Date: 2020-07-28 13:57:53
# @Runtime: 64 ms
# @Memory: 13.4 MB

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        pre = points[0]
        for point in points[1:]:
            ans += max(abs(point[0]-pre[0]), abs(point[1]-pre[1]))
            pre = point
        return ans

