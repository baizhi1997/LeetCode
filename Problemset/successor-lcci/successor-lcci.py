
# @Title: 后继者 (Successor LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 16:19:24
# @Runtime: 84 ms
# @Memory: 17.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        cur = root
        res = None
        while cur:
            if cur.val <= p.val:
                cur = cur.right
            else:
                res = cur
                cur = cur.left
        return res

