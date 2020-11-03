
# @Title: 二叉树的前序遍历 (Binary Tree Preorder Traversal)
# @Author: qinxinlei
# @Date: 2018-10-29 20:54:13
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        stack=root and [root]
        while stack:
            p=stack.pop()
            ans.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return ans
