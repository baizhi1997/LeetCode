
# @Title: 从尾到头打印链表 (从尾到头打印链表 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:58:58
# @Runtime: 52 ms
# @Memory: 15.1 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans[::-1]
