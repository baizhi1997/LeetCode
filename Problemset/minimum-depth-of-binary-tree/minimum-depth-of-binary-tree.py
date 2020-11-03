
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-07 17:51:49
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left:
            return self.minDepth(root.right)+1
        if not root.right:
            return self.minDepth(root.left)+1
        return min(self.minDepth(root.left),self.minDepth(root.right))+1
    
