
# @Title: 删除中间节点 (Delete Middle Node LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 01:15:12
# @Runtime: 48 ms
# @Memory: 13.7 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next.next:
            node.val = node.next.val
            node = node.next
        node.val = node.next.val
        node.next = None
