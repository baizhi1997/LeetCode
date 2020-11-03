
# @Title: 环形链表 II (Linked List Cycle II)
# @Author: qinxinlei
# @Date: 2018-10-08 16:26:58
# @Runtime: 48 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                slow=head
                while slow!=fast:
                    slow=slow.next
                    fast=fast.next
                return slow
