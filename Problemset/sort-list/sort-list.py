
# @Title: 排序链表 (Sort List)
# @Author: qinxinlei
# @Date: 2019-05-13 14:13:20
# @Runtime: 236 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def merge(self, l1, l2):
        p = head = ListNode(0)
        while l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            p.next = l1
            l1 = l1.next
            p = p.next
        p.next = l1 or l2
        return head.next
        
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(mid))
