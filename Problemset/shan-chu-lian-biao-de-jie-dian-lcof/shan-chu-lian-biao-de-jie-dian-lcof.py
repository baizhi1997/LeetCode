
# @Title: 删除链表的节点 (删除链表的节点 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 21:12:31
# @Runtime: 44 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p = head
        if p.val == val:
            return p.next
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return head
            else:
                p = p.next
        return head
