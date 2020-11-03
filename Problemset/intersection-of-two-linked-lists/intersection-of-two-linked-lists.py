
# @Title: 相交链表 (Intersection of Two Linked Lists)
# @Author: qinxinlei
# @Date: 2018-10-25 17:52:47
# @Runtime: 216 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA and headB:
            pA=headA 
            pB=headB 
            while pA!=pB:
                pA=pA.next if pA else headB
                pB=pB.next if pB else headA
            return pA
        return None
