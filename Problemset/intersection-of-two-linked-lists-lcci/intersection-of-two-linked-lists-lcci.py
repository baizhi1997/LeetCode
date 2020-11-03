
# @Title: 链表相交 (Intersection of Two Linked Lists LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 15:06:47
# @Runtime: 168 ms
# @Memory: 28.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ta,tb=headA,headB
        while ta!=tb:
            ta=ta.next if ta else headB
            tb=tb.next if tb else headA
        return tb
