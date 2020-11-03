
# @Title: 删除排序链表中的重复元素 II (Remove Duplicates from Sorted List II)
# @Author: qinxinlei
# @Date: 2018-10-28 12:06:19
# @Runtime: 48 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x=ListNode(0)
        x.next=head 
        pre=x
        cur=head
        while cur:
            if cur.next and cur.val==cur.next.val:
                while cur.next and cur.val==cur.next.val:
                    cur=cur.next
                pre.next=cur.next
            else:
                pre=pre.next 
            cur=cur.next
        return x.next
