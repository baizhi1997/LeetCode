
# @Title: 环路检测 (Linked List Cycle LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 14:22:59
# @Runtime: 60 ms
# @Memory: 16.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast != slow:
            return
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

