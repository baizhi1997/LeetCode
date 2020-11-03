
# @Title: 二叉搜索树的最近公共祖先 (Lowest Common Ancestor of a Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-08 14:44:20
# @Runtime: 72 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root:
            x,y,z=p.val,q.val,root.val
            if x<z and y<z:
                return self.lowestCommonAncestor(root.left,p,q)
            if x>z and y>z:
                return self.lowestCommonAncestor(root.right,p,q)
        return root
