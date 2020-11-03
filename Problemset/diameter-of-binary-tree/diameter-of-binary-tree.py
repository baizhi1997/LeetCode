
# @Title: 二叉树的直径 (Diameter of Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-30 12:18:59
# @Runtime: 56 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter=0
        self.f(root)
        return self.diameter
    def f(self,root):
        if not root:
            return 0
        l=self.f(root.left)
        r=self.f(root.right)
        self.diameter=max(self.diameter,l+r)
        return max(l,r)+1
