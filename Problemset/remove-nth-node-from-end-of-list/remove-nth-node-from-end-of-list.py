
# @Title: 删除链表的倒数第N个节点 (Remove Nth Node From End of List)
# @Author: qinxinlei
# @Date: 2018-10-26 22:36:34
# @Runtime: 40 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        p=q=head
        while p:
            p=p.next
            if n<0:
                q=q.next
            n-=1
        if n>=0:
            return head.next
        q.next=q.next.next
        return head
