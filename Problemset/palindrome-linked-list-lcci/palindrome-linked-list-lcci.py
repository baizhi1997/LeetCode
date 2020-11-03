
# @Title: 回文链表 (Palindrome Linked List LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 13:57:09
# @Runtime: 100 ms
# @Memory: 23.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        pre = slow
        while slow and slow.next:
            tmp = slow.next.next
            slow.next.next = pre
            pre = slow.next
            slow.next = tmp
        while head and pre:
            if head.val != pre.val:
                return False
            head = head.next
            pre = pre.next
        return True
