
# @Title: 二进制链表转整数 (Convert Binary Number in a Linked List to Integer)
# @Author: qinxinlei
# @Date: 2020-07-28 15:07:56
# @Runtime: 36 ms
# @Memory: 13.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans <<= 1
            ans += head.val
            head = head.next
        return ans
