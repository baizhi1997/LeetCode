
# @Title: 合并K个升序链表 (Merge k Sorted Lists)
# @Author: qinxinlei
# @Date: 2019-01-19 14:25:54
# @Runtime: 112 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        ls = []
        for ele in lists:
            while ele:
                ls.append(ele.val)
                ele = ele.next
        ls.sort()
        head = p = ListNode(None)
        for i in ls:
            head.next = ListNode(i)
            head = head.next
        return p.next
