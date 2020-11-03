
# @Title: 合并两个排序的链表 (合并两个排序的链表  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:11:00
# @Runtime: 56 ms
# @Memory: 14 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = q = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
        p.next = l1 if l1 else l2
        return q.next
