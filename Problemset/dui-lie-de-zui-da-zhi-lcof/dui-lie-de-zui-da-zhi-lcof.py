
# @Title: 队列的最大值 (队列的最大值 LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 17:29:15
# @Runtime: 336 ms
# @Memory: 16.9 MB

class MaxQueue:

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def max_value(self) -> int:
        if not self.queue1:
            return -1
        return self.queue2[0]

    def push_back(self, value: int) -> None:
        self.queue1.append(value)
        while self.queue2 and value > self.queue2[-1]:
            self.queue2.pop()
        self.queue2.append(value)

    def pop_front(self) -> int:
        if not self.queue1:
            return -1
        tmp = self.queue1.pop(0)
        if tmp == self.queue2[0]:
            self.queue2.pop(0)
        return tmp

# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
