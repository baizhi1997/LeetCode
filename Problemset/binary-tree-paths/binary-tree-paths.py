
# @Title: 二叉树的所有路径 (Binary Tree Paths)
# @Author: qinxinlei
# @Date: 2018-11-06 17:04:20
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        ans=[]
        stack=[('',root)]
        while len(stack):
            s,n=stack.pop()
            s+=str(n.val)
            if n.left:
                stack.append((s+'->',n.left))
            if n.right:
                stack.append((s+'->',n.right))
            if not n.left and not n.right:
                ans.append(s)
        return ans
