
# @Title: 三合一 (Three in One LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 15:27:45
# @Runtime: 240 ms
# @Memory: 20.8 MB

class TripleInOne:

    def __init__(self, stackSize: int):
        self.N = 3
        self.stackSize = stackSize
        self.d = [0] * (stackSize + 1) * self.N

    def _get_size_index(self, stackNum):
        return self.stackSize * self.N + stackNum

    def push(self, stackNum: int, value: int) -> None:
        size = self.d[self._get_size_index(stackNum)]
        if size >= self.stackSize:
            return

        self.d[size * self.N + stackNum] = value
        self.d[self._get_size_index(stackNum)] += 1

    def pop(self, stackNum: int) -> int:
        size = self.d[self._get_size_index(stackNum)]
        if size > 0:
            self.d[self._get_size_index(stackNum)] -= 1
            return self.d[(size-1) * self.N + stackNum]
        return -1

    def peek(self, stackNum: int) -> int:
        size = self.d[self._get_size_index(stackNum)]
        if size > 0:
            return self.d[(size - 1) * self.N + stackNum]
        return -1

    def isEmpty(self, stackNum: int) -> bool:
        return self.d[self._get_size_index(stackNum)] == 0


# Your TripleInOne object will be instantiated and called as such:
# obj = TripleInOne(stackSize)
# obj.push(stackNum,value)
# param_2 = obj.pop(stackNum)
# param_3 = obj.peek(stackNum)
# param_4 = obj.isEmpty(stackNum)
