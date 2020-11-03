
# @Title: 用两个栈实现队列 (用两个栈实现队列 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:42:48
# @Runtime: 584 ms
# @Memory: 16.6 MB

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
