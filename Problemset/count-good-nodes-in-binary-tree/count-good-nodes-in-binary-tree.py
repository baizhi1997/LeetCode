
# @Title: 统计二叉树中好节点的数目 (Count Good Nodes in Binary Tree)
# @Author: qinxinlei
# @Date: 2020-06-17 09:48:56
# @Runtime: 284 ms
# @Memory: 31.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxnum):
            if not root:
                return 0
            if root.val >= maxnum:
                return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
            else:
                return dfs(root.left, maxnum) + dfs(root.right, maxnum)
        return dfs(root, float('-inf'))
