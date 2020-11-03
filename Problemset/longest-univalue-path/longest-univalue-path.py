
# @Title: 最长同值路径 (Longest Univalue Path)
# @Author: qinxinlei
# @Date: 2018-11-17 16:03:57
# @Runtime: 476 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def f(root):
            if not root:
                return 0
            l=f(root.left)
            r=f(root.right)
            l=l+1 if root.left and root.val==root.left.val else 0
            r=r+1 if root.right and root.val==root.right.val else 0
            self.ans=max(self.ans,l+r)
            return max(l,r)
        f(root)
        return self.ans
