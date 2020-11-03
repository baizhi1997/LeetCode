
# @Title: 链表中的下一个更大节点 (Next Greater Node In Linked List)
# @Author: qinxinlei
# @Date: 2019-04-08 20:44:31
# @Runtime: 412 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        ans=[]
        stack=[]
        i=0
        while head:
            while stack and stack[-1][1]<head.val:
                ans[stack.pop()[0]]=head.val
            stack.append((i,head.val))
            ans.append(0)
            i+=1
            head=head.next
        return ans
