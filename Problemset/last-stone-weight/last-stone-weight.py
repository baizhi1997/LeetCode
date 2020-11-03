
# @Title: 最后一块石头的重量 (Last Stone Weight)
# @Author: qinxinlei
# @Date: 2019-05-19 19:30:28
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-x for x in stones]
        heapq.heapify(pq)
        for i in range(len(stones) - 1):
            x, y = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(x - y))
        return -pq[0]
