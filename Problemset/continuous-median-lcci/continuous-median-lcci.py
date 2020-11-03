
# @Title: 连续中值 (Continuous Median LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 15:56:32
# @Runtime: 232 ms
# @Memory: 23.8 MB

class MedianFinder:
    
    def __init__(self):
        self.s, self.l = [], []

    def addNum(self, num: int) -> None:
        if len(self.s) == len(self.l):
            heapq.heappush(self.s, -heapq.heappushpop(self.l, -num))
        else:
            heapq.heappush(self.l, -heapq.heappushpop(self.s, num))
        
    def findMedian(self) -> float:
        return len(self.s) == len(self.l) and (self.s[0] - self.l[0]) / 2 or self.s[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
