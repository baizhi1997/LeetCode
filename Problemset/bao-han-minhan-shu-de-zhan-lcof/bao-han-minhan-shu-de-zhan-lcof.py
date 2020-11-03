
# @Title: 包含min函数的栈 (包含min函数的栈 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 11:00:26
# @Runtime: 72 ms
# @Memory: 16.4 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = [] 

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minstack[-1]:
            self.minstack.pop()
        return x

    def top(self) -> int:
        return self.stack[-1]

    def min(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
