
# @Title: 完全二叉树的节点个数 (Count Complete Tree Nodes)
# @Author: qinxinlei
# @Date: 2018-10-16 16:40:03
# @Runtime: 112 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def h(self, root):
        return 1+self.h(root.left) if root else 0
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lh=self.h(root.left)
        rh=self.h(root.right)
        return pow(2,lh)+self.countNodes(root.right) if lh==rh else pow(2,rh)+self.countNodes(root.left)
