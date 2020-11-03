
# @Title: 翻转二叉树 (Invert Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-08 11:44:21
# @Runtime: 20 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root:
            root.left,root.right=self.invertTree(root.right),self.invertTree(root.left)
            return root
