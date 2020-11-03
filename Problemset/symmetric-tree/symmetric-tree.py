
# @Title: 对称二叉树 (Symmetric Tree)
# @Author: qinxinlei
# @Date: 2018-10-03 11:15:04
# @Runtime: 32 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(r,l):
            return r and l and r.val==l.val and compare(r.right,l.left) and compare(r.left,l.right) or r==l
        return compare(root.right,root.left) if root else True
