
# @Title: 数据流中的第 K 大元素 (Kth Largest Element in a Stream)
# @Author: qinxinlei
# @Date: 2018-11-18 20:46:18
# @Runtime: 72 ms
# @Memory: N/A

class KthLargest:
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool=nums
        self.k=k
        heapq.heapify(self.pool)
        while len(self.pool)>k:
            heapq.heappop(self.pool)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.pool)<self.k:
            heapq.heappush(self.pool,val)
        elif self.pool[0]<val:
            heapq.heappop(self.pool)
            heapq.heappush(self.pool,val)
        return self.pool[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
