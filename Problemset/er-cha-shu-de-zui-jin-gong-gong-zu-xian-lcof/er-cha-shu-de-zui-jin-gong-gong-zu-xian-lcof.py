
# @Title: 二叉树的最近公共祖先 (二叉树的最近公共祖先 LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 17:45:50
# @Runtime: 92 ms
# @Memory: 23.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val: return root
        l = self.lowestCommonAncestor(root.left,  p , q)
        r = self.lowestCommonAncestor(root.right,  p , q)
        return root if l and r else l or r

