
# @Title: 从叶结点开始的最小字符串 (Smallest String Starting From Leaf)
# @Author: qinxinlei
# @Date: 2019-03-05 12:24:07
# @Runtime: 44 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        if not root:
            return ""
        if not root.left:
            s=self.smallestFromLeaf(root.right)
        elif not root.right:
            s=self.smallestFromLeaf(root.left)
        else:
            s=min(self.smallestFromLeaf(root.left),self.smallestFromLeaf(root.right))
        return s+chr(97+root.val)
