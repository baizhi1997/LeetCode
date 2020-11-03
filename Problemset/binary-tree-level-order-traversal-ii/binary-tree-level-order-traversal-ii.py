
# @Title: 二叉树的层次遍历 II (Binary Tree Level Order Traversal II)
# @Author: qinxinlei
# @Date: 2018-10-16 15:29:05
# @Runtime: 52 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=[root] if root else []
        ans=[]
        while q:
            ans.append([i.val for i in q])
            q=[x for i in q for x in (i.left,i.right) if x]
        return ans[::-1]
