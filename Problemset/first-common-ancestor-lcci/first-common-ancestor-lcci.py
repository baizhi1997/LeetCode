
# @Title: 首个共同祖先 (First Common Ancestor LCCI)
# @Author: qinxinlei
# @Date: 2020-06-17 10:48:26
# @Runtime: 100 ms
# @Memory: 23.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: return root
        return left if left else right

