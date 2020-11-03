
# @Title: 重排链表 (Reorder List)
# @Author: qinxinlei
# @Date: 2019-05-11 13:25:28
# @Runtime: 88 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        q = []
        p = head
        while p:
            q.append(p)
            p = p.next
        i = 0
        j = len(q) - 1
        x = 1
        while i < j:
            if x == 1:
                q[i].next = q[j]
                i += 1
            else:
                q[j].next = q[i]
                j -= 1
            x *= -1
        if x == 1:
            q[j].next = None
        else:
            q[i].next = None
