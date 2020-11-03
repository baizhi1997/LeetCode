
# @Title: 修剪二叉搜索树 (Trim a Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-20 12:59:39
# @Runtime: 56 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        if not root:
            return
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)
        root.left = self.trimBST(root.left, L, R)
        return root
    return root
