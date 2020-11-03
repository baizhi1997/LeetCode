
# @Title: 最深叶节点的最近公共祖先 (Lowest Common Ancestor of Deepest Leaves)
# @Author: qinxinlei
# @Date: 2020-06-18 16:42:07
# @Runtime: 80 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None, 0
            lr, ld = dfs(root.left)
            rr, rd = dfs(root.right)
            if ld > rd:
                return lr, ld + 1
            elif ld < rd:
                return rr, rd + 1
            else:
                return root, ld + 1
        ans, h = dfs(root)
        return ans


