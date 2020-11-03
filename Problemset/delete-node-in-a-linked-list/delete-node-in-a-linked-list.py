
# @Title: 删除链表中的节点 (Delete Node in a Linked List)
# @Author: qinxinlei
# @Date: 2018-10-22 16:02:27
# @Runtime: 52 ms
# @Memory: N/A

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
        node.val=node.next.val
        node.next=node.next.next
