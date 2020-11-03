
# @Title: 二叉树的坡度 (Binary Tree Tilt)
# @Author: qinxinlei
# @Date: 2018-10-29 21:26:34
# @Runtime: 68 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.tilt=0
        self.f(root)
        return self.tilt
    
    def f(self,root):
        if not root:
            return 0
        left=self.f(root.left)
        right=self.f(root.right)
        self.tilt+=abs(left-right)
        return root.val+left+right
