
# @Title: 旋转链表 (Rotate List)
# @Author: qinxinlei
# @Date: 2018-10-28 11:26:35
# @Runtime: 44 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        p=q=head
        l=1
        while p.next:
            p=p.next
            l+=1
        p.next=head
        k%=l
        for _ in range(l-k-1):
            q=q.next
        ans=q.next
        q.next=None
        return ans
