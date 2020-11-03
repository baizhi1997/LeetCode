
# @Title: 二叉树的堂兄弟节点 (Cousins in Binary Tree)
# @Author: qinxinlei
# @Date: 2019-03-04 21:06:35
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(root, depth, parent, val):
            if root:
                if root.val == val:
                    return depth, parent
                return dfs(root.left, depth + 1, root, val) or dfs(root.right, depth + 1, root, val)
        dx, px=dfs(root, 0, None, x)
        dy, py=dfs(root, 0, None, y)
        return dx == dy and px != py
