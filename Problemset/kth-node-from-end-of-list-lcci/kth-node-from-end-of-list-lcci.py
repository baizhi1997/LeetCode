
# @Title: 返回倒数第 k 个节点 (Kth Node From End of List LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 10:22:59
# @Runtime: 32 ms
# @Memory: 13.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        p = head
        for _ in range(k):
            p = p.next
        while p and head:
            p = p.next
            head = head.next
        return head.val
