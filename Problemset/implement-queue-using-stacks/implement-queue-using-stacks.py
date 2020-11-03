
# @Title: 用栈实现队列 (Implement Queue using Stacks)
# @Author: qinxinlei
# @Date: 2018-11-16 16:27:53
# @Runtime: 32 ms
# @Memory: N/A

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack=[]

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.stack.pop(0)

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
