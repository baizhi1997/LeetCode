
# @Title: 最接近原点的 K 个点 (K Closest Points to Origin)
# @Author: qinxinlei
# @Date: 2019-03-01 16:21:46
# @Runtime: 384 ms
# @Memory: N/A

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap=[]
        for p in points:
            heapq.heappush(heap,(-p[0]**2-p[1]**2,p))
            if len(heap)>K:
                heapq.heappop(heap)
        return [p for (d,p) in heap]
