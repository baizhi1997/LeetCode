
# @Title: 对链表进行插入排序 (Insertion Sort List)
# @Author: qinxinlei
# @Date: 2019-05-24 10:55:41
# @Runtime: 1940 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        q = ListNode(0)
        while head:
            p = q
            while p.next and p.next.val < head.val:
                p = p.next
            tmp = head
            head = head.next
            tmp.next = p.next
            p.next = tmp
        return q.next
