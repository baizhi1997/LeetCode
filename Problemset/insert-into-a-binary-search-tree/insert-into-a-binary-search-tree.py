
# @Title: 二叉搜索树中的插入操作 (Insert into a Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-29 20:11:10
# @Runtime: 136 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        p=root
        if not p:
            return TreeNode(val)
        while p:
            if p.val<val:
                if p.right:
                    p=p.right
                else:
                    p.right=TreeNode(val)
                    break
            else:
                if p.left:
                    p=p.left
                else:
                    p.left=TreeNode(val)
                    break
        return root
