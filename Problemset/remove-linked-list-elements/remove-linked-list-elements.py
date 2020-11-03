
# @Title: 移除链表元素 (Remove Linked List Elements)
# @Author: qinxinlei
# @Date: 2018-11-01 13:03:33
# @Runtime: 72 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        p=ListNode(0)
        p.next=head
        pre=p
        while head:
            if head.val==val:
                head=head.next
                pre.next=head
            else:
                head=head.next
                pre=pre.next
        return p.next
