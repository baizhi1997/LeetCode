
# @Title: 奇偶链表 (Odd Even Linked List)
# @Author: qinxinlei
# @Date: 2020-08-14 16:57:27
# @Runtime: 64 ms
# @Memory: 15.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:return head
        odd = head
        even_head = even = head.next
        while odd.next and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd,even = odd.next,even.next
        odd.next = even_head
        return head

