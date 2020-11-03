
# @Title: 链表的中间结点 (Middle of the Linked List)
# @Author: qinxinlei
# @Date: 2018-10-18 21:59:58
# @Runtime: 20 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
