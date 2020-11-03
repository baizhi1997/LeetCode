
# @Title: 二叉搜索树的第k大节点 (二叉搜索树的第k大节点  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:40:12
# @Runtime: 72 ms
# @Memory: 17.3 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.right
            p = stack.pop()
            k -= 1
            if k == 0:
                return p.val
            root = p.left

