
# @Title: 二叉树展开为链表 (Flatten Binary Tree to Linked List)
# @Author: qinxinlei
# @Date: 2019-01-03 21:13:28
# @Runtime: 68 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        stack = []
        p = root
        while stack or p:
            if p.right:
                stack.append(p.right)
            if p.left:
                p.right = p.left
                stack.append(p.left)
                p.left = None
            else:
                if not stack:
                    break
                p.right = stack[-1]
            p = stack.pop()
