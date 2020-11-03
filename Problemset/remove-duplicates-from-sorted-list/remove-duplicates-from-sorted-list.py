
# @Title: 删除排序链表中的重复元素 (Remove Duplicates from Sorted List)
# @Author: qinxinlei
# @Date: 2018-10-02 16:28:05
# @Runtime: 28 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur=head
        while cur and cur.next:
            p=cur.next
            if p.val==cur.val:
                cur.next=p.next
            else:
                cur=p
        return head
