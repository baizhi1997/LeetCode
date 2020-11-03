
# @Title: 有序链表转换二叉搜索树 (Convert Sorted List to Binary Search Tree)
# @Author: qinxinlei
# @Date: 2019-01-03 18:13:28
# @Runtime: 272 ms
# @Memory: N/A

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        tmp=[]
        while head:
            tmp.append(head.val)
            head=head.next
        def f(tmp):
            if not tmp:
                return None
            i=len(tmp)//2
            root=TreeNode(tmp[i])
            root.left=f(tmp[:i])
            root.right=f(tmp[i+1:])
            return root
        return f(tmp)
