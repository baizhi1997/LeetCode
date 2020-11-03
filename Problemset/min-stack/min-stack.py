
# @Title: 最小栈 (Min Stack)
# @Author: qinxinlei
# @Date: 2018-11-14 21:43:05
# @Runtime: 56 ms
# @Memory: N/A

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.min=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if not self.min or x<=self.min[-1]:
            self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack.pop()==self.min[-1]:
            self.min.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
