
# @Title: 分隔链表 (Partition List)
# @Author: qinxinlei
# @Date: 2018-10-28 13:25:20
# @Runtime: 40 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        ans=p=ListNode(0)
        q=ListNode(0)
        p.next=head
        cur=q
        while p.next:
            if p.next.val<x:
                p=p.next
            else:
                cur.next=ListNode(p.next.val)
                cur=cur.next
                p.next=p.next.next
        p.next=q.next
        return ans.next
