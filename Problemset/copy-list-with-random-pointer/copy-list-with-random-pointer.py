
# @Title: 复制带随机指针的链表 (Copy List with Random Pointer)
# @Author: qinxinlei
# @Date: 2019-05-14 19:04:13
# @Runtime: 52 ms
# @Memory: N/A

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)
