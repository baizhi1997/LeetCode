
# @Title: 二叉树的右视图 (Binary Tree Right Side View)
# @Author: qinxinlei
# @Date: 2019-01-06 16:57:22
# @Runtime: 64 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        ans=[]
        stack=[root]
        while stack:
            ans.append(stack[-1].val)
            stack=[x for r in stack for x in (r.left,r.right) if x]
        return ans
