
# @Title: K 个一组翻转链表 (Reverse Nodes in k-Group)
# @Author: qinxinlei
# @Date: 2019-04-28 22:39:13
# @Runtime: 52 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        node=head 
        for _ in range(k):
            if not node:
                return head
            node=node.next
        cur=head
        p=None
        for _ in range(k):
            tmp=cur.next
            cur.next=p
            p=cur
            cur=tmp
        head.next=self.reverseKGroup(cur,k)
        return p
