
# @Title: 栈排序 (Sort of Stacks LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 17:25:33
# @Runtime: 976 ms
# @Memory: 14.2 MB

class SortedStack:

    def __init__(self):
        self.stk = []


    def push(self, val: int) -> None:
        tmp_stk = []
        while self.stk and self.stk[-1] < val:
            tmp_stk.append(self.stk.pop())
        self.stk.append(val)
        while tmp_stk:
            self.stk.append(tmp_stk.pop())


    def pop(self) -> None:
        if self.isEmpty():
            return
        self.stk.pop()

    def peek(self) -> int:
        if self.isEmpty():
            return -1
        return self.stk[-1]


    def isEmpty(self) -> bool:
        return len(self.stk) == 0


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
