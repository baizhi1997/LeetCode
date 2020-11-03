
# @Title: 合并二叉树 (Merge Two Binary Trees)
# @Author: qinxinlei
# @Date: 2018-10-18 19:43:27
# @Runtime: 140 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val+=t2.val
        t1.left=self.mergeTrees(t1.left,t2.left)
        t1.right=self.mergeTrees(t1.right,t2.right)
        return t1
