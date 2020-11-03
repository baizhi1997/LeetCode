
# @Title: 单值二叉树 (Univalued Binary Tree)
# @Author: qinxinlei
# @Date: 2019-03-01 17:09:36
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        if root.left and root.left.val!=root.val:
            return False
        if root.right and root.right.val!=root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
