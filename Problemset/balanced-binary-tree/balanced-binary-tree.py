
# @Title: 平衡二叉树 (Balanced Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-07 17:38:27
# @Runtime: 44 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root):
            if not root:
                return 0
            l,r=f(root.left),f(root.right)
            if l==-1 or r==-1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        return f(root)!=-1
