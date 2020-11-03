
# @Title: 栈的最小值 (Min Stack LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 17:56:31
# @Runtime: 68 ms
# @Memory: 16.4 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minarr = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minarr or x <= self.minarr[-1]:
            self.minarr.append(x)

    def pop(self) -> None:
        if self.minarr[-1] == self.stack.pop():
            self.minarr.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minarr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
