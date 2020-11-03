
# @Title: 堆盘子 (Stack of Plates LCCI)
# @Author: qinxinlei
# @Date: 2020-07-18 22:41:30
# @Runtime: 136 ms
# @Memory: 19.7 MB

class StackOfPlates:

    def __init__(self, cap: int):
        self.cap = cap
        self.array = []

    def push(self, val: int) -> None:
        # 处理边界情况：cap == 0 不让push
        if self.cap == 0:
            return

        if not self.array or len(self.array[-1]) >= self.cap:
            self.array.append([val])
        else:
            self.array[-1].append(val)

    def pop(self) -> int:
        val = -1
        if self.array and self.array[-1]:
            val = self.array[-1].pop()
            if not self.array[-1]: self.array.pop()
        return val

    def popAt(self, index: int) -> int:
        val = -1
        if len(self.array) >= index + 1:
            val = self.array[index].pop()
            if not self.array[index]: self.array.pop(index)
        return val


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
