
# @Title: 反转链表 II (Reverse Linked List II)
# @Author: qinxinlei
# @Date: 2018-12-13 16:09:33
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        prev=dummy=ListNode(0)
        dummy.next=head
        for _ in range(m-1):
            prev=prev.next
        p=prev.next
        q=p.next
        for _ in range(n-m):
            p.next=q.next
            q.next=prev.next
            prev.next=q
            q=p.next
        return dummy.next
