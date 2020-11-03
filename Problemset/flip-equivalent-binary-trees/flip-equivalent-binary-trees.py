
# @Title: 翻转等价二叉树 (Flip Equivalent Binary Trees)
# @Author: qinxinlei
# @Date: 2018-12-02 10:53:17
# @Runtime: 44 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val!=root2.val:
            return False
        return (self.flipEquiv(root1.right,root2.right) and self.flipEquiv(root1.left,root2.left)) or (self.flipEquiv(root1.left,root2.right) and self.flipEquiv(root1.right,root2.left))
