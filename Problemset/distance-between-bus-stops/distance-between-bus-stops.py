
# @Title: 公交站间的距离 (Distance Between Bus Stops)
# @Author: qinxinlei
# @Date: 2020-08-02 22:38:56
# @Runtime: 60 ms
# @Memory: 14.4 MB

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start
        x = sum(distance[start:destination])
        y = sum(distance)-x
        return min(x, y)
