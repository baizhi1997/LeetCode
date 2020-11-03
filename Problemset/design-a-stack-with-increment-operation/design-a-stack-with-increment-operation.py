
# @Title: 设计一个支持增量操作的栈 (Design a Stack With Increment Operation)
# @Author: qinxinlei
# @Date: 2020-06-04 11:06:50
# @Runtime: 136 ms
# @Memory: 14 MB

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        else:
            return self.stack.pop()

    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        self.stack[0:k] = [x + val for x in self.stack[0:k]]


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
