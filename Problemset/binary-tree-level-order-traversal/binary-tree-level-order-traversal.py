
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: qinxinlei
# @Date: 2018-10-16 15:26:28
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=[root] if root else []
        ans=[]
        while q:
            ans.append([i.val for i in q])
            q=[c for i in q for c in (i.left,i.right) if c]
        return ans
