
# @Title: 两两交换链表中的节点 (Swap Nodes in Pairs)
# @Author: qinxinlei
# @Date: 2018-10-27 19:16:16
# @Runtime: 44 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=head
        if not p:
            return p
        q=head.next
        if not q:
            return p
        while q:
            q.val,p.val=p.val,q.val
            if q.next:
                p=p.next.next
                q=q.next.next
            else:
                break
        return head
