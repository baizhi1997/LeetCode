
# @Title: 二叉搜索树中的搜索 (Search in a Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-18 22:15:53
# @Runtime: 68 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        while root:
            if root.val==val:
                return root
            elif root.val<val:
                root=root.right
            else: 
                root=root.left
        return []
