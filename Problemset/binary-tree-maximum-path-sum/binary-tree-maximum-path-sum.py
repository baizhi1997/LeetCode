
# @Title: 二叉树中的最大路径和 (Binary Tree Maximum Path Sum)
# @Author: qinxinlei
# @Date: 2019-05-07 19:10:51
# @Runtime: 88 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.globalmax = float('-inf')
        self.f(root)
        return self.globalmax

    def f(self, node):
        if not node:
            return 0
        left = self.f(node.left)
        right = self.f(node.right)
        if left < 0:
            left = 0
        if right < 0:
            right = 0
        self.globalmax = max(left + right + node.val, self.globalmax)
        return max(left, right) + node.val
