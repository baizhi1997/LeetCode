
# @Title: 二叉树的深度 (二叉树的深度 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:52:07
# @Runtime: 44 ms
# @Memory: 15.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
