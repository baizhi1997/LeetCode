
# @Title: 二叉树的最大深度 (Maximum Depth of Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-03 11:25:47
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1 if root else 0
