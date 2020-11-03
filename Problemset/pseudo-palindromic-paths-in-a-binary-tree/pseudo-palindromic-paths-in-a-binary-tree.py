
# @Title: 二叉树中的伪回文路径 (Pseudo-Palindromic Paths in a Binary Tree)
# @Author: qinxinlei
# @Date: 2020-08-14 14:25:54
# @Runtime: 472 ms
# @Memory: 48.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.res = 0
        if not root:
            return 0
        def changeset(oddsets, v):
            if v in oddsets:
                oddsets.remove(v)
            else:
                oddsets.add(v)
        def dfs(node, oddsets):
            if not node.left and not node.right:
                if len(oddsets) <= 1:
                    self.res += 1
                return
            if node.left:
                changeset(oddsets, node.left.val)
                dfs(node.left, oddsets)
                changeset(oddsets, node.left.val)
            if node.right:
                changeset(oddsets, node.right.val)
                dfs(node.right, oddsets)
                changeset(oddsets, node.right.val)

        dfs(root, {root.val})
        return self.res

