
# @Title: 最近的请求次数 (Number of Recent Calls)
# @Author: qinxinlei
# @Date: 2018-11-16 20:51:36
# @Runtime: 200 ms
# @Memory: N/A

class RecentCounter:

    def __init__(self):
        self.arr = []
        self.i = 0
        self.cnt = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        self.cnt += 1
        while t - self.arr[self.i] > 3000:
            self.i += 1;
        return self.cnt - self.i

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
