
# @Title: 在二叉树中增加一行 (Add One Row to Tree)
# @Author: qinxinlei
# @Date: 2020-10-09 18:55:22
# @Runtime: 76 ms
# @Memory: 16 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root:
            return

        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        if d == 2:
            L = TreeNode(v)
            R = TreeNode(v)

            L.left = root.left
            R.right = root.right

            root.left = L
            root.right = R
            return root

        self.addOneRow(root.left, v, d-1)
        self.addOneRow(root.right, v, d-1)
        return root

