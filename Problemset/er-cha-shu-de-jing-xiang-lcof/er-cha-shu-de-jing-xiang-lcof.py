
# @Title: 二叉树的镜像 (二叉树的镜像  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:53:27
# @Runtime: 40 ms
# @Memory: 13.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
