
# @Title: 链表求和 (Sum Lists LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 21:36:38
# @Runtime: 68 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p = l1
        carry = 0
        while l1 and l2:
            l1.val += (l2.val + carry)
            carry, l1.val = divmod(l1.val, 10)
            if not l1.next or not l2.next:
                break
            l1 = l1.next
            l2 = l2.next
        if not l1.next:
            l1.next = l2.next
        while l1.next and carry:
            l1.next.val += carry
            carry, l1.next.val = divmod(l1.next.val, 10)
            l1 = l1.next
        if carry:
            l1.next = ListNode(carry) 
        return p
