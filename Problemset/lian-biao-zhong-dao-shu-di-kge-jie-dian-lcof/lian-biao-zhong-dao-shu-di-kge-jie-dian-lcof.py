
# @Title: 链表中倒数第k个节点 (链表中倒数第k个节点 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:48:52
# @Runtime: 40 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        l = 0
        p = head
        while p:
            l += 1
            p = p.next
        for _ in range(l-k):
            head = head.next
        return head
