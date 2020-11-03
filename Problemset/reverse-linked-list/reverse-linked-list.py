
# @Title: 反转链表 (Reverse Linked List)
# @Author: qinxinlei
# @Date: 2018-10-30 21:00:04
# @Runtime: 40 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre=None
        p=head
        while p:
            tmp=p.next
            p.next=pre
            pre=p
            p=tmp
        return pre
