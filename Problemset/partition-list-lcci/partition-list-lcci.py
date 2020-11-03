
# @Title: 分割链表 (Partition List LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 17:18:07
# @Runtime: 32 ms
# @Memory: 13.5 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pc = head
        pw = head
        while pc:
            if pc.val < x:
                pc.val, pw.val = pw.val, pc.val
                pw = pw.next
            pc = pc.next
            
        return head

