
# @Title: 输出二叉树 (Print Binary Tree)
# @Author: qinxinlei
# @Date: 2020-10-09 19:16:42
# @Runtime: 56 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def maxDepth(r = root):
            return 0 if r is None else 1 + max(maxDepth(r.left), maxDepth(r.right))
        m = maxDepth()
        n = (1 << m) - 1
        board = [['' for _ in range(n)] for _ in range(m)]
        def fill(root, d, l, r):
            if root is None: return
            mid = l + ((r - l) >> 1)
            board[d][mid] = str(root.val)
            fill(root.left, d + 1, l, mid - 1)
            fill(root.right, d + 1, mid + 1, r)
        fill(root, 0, 0, n - 1)
        return board

