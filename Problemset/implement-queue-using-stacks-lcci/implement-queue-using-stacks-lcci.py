
# @Title: 化栈为队 (Implement Queue using Stacks LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 11:25:07
# @Runtime: 28 ms
# @Memory: 13.4 MB

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
        return self.stack2.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []
        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack1 and not self.stack2 


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
