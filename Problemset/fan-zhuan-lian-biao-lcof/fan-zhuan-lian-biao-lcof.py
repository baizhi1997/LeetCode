
# @Title: 反转链表 (反转链表 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:04:55
# @Runtime: 44 ms
# @Memory: 14.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tmp = []
        while head:
            tmp.append(head)
            head = head.next
        p = tmp.pop()
        q = p
        for node in tmp[::-1]:
            p.next = node
            p = p.next
        p.next = None
        return q
