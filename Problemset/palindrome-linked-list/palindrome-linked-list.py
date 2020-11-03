
# @Title: 回文链表 (Palindrome Linked List)
# @Author: qinxinlei
# @Date: 2018-11-01 14:57:10
# @Runtime: 76 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        l=0
        p=ListNode(0)
        p.next=head
        cur=head
        while cur:
            l+=1
            cur=cur.next
        for _ in range(l//2):
            cur=head
            head=head.next
            cur.next=p.next
            p.next=cur
        if l&1:
            head=head.next
        for _ in range(l//2):
            if cur.val!=head.val:
                return False
            cur=cur.next
            head=head.next
        return True
