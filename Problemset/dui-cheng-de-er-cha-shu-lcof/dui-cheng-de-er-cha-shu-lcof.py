
# @Title: 对称的二叉树 (对称的二叉树  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-26 11:14:08
# @Runtime: 52 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)
        return recur(root.left, root.right) if root else True

            
