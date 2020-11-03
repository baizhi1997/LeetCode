
# @Title: 叶子相似的树 (Leaf-Similar Trees)
# @Author: qinxinlei
# @Date: 2018-10-20 13:05:43
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def f(r):
            if not r:
                return []
            if not (r.left or r.right):
                return [r.val]
            return f(r.left)+f(r.right)
        return f(root1)==f(root2)
