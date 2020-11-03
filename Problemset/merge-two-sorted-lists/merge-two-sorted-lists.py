
# @Title: 合并两个有序链表 (Merge Two Sorted Lists)
# @Author: qinxinlei
# @Date: 2018-10-02 15:38:01
# @Runtime: 28 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans=p=ListNode(0)
        while l1 and l2:
            if l1.val>l2.val:
                p.next=l2
                l2=l2.next
            else:
                p.next=l1
                l1=l1.next
            p=p.next
        p.next=l2 if l2 else l1
        return ans.next
    
