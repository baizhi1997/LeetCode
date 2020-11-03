
# @Title: 二叉搜索树的范围和 (Range Sum of BST)
# @Author: qinxinlei
# @Date: 2018-11-19 14:50:26
# @Runtime: 264 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if root.val<L:
            return self.rangeSumBST(root.right,L,R)
        if root.val>R:
            return self.rangeSumBST(root.left,L,R)
        return root.val+self.rangeSumBST(root.right,L,R)+self.rangeSumBST(root.left,L,R)
