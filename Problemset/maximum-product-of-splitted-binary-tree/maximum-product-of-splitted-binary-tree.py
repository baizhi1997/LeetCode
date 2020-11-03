
# @Title: 分裂二叉树的最大乘积 (Maximum Product of Splitted Binary Tree)
# @Author: qinxinlei
# @Date: 2020-10-09 11:18:38
# @Runtime: 392 ms
# @Memory: 78.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxProduct(self, root: TreeNode) -> int:
        max_ = 0
        tree_sum = []

        def sum_(root):
            nonlocal tree_sum
            if not root:
                return 0
            l = sum_(root.left)
            r = sum_(root.right)
            tree_sum.append(l + r + root.val)
            return l + r + root.val

        mod = 10 ** 9 + 7
        for i in range(len(tree_sum) - 1):
            max_ = max(max_,(tree_sum[-1] - tree_sum[i]) * tree_sum[i])

        return max_ % mod

