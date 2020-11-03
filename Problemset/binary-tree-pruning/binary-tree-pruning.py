
# @Title: 二叉树剪枝 (Binary Tree Pruning)
# @Author: qinxinlei
# @Date: 2018-10-29 20:25:56
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if root.val==1 or root.left or root.right:
            return root
        return None
