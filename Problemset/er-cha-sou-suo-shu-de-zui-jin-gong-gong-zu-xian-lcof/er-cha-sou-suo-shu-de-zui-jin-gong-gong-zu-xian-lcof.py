
# @Title: 二叉搜索树的最近公共祖先 (二叉搜索树的最近公共祖先 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 14:18:19
# @Runtime: 116 ms
# @Memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

