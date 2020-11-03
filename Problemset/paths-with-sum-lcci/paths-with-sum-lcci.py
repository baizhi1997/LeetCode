
# @Title: 求和路径 (Paths with Sum LCCI)
# @Author: qinxinlei
# @Date: 2020-07-15 18:06:48
# @Runtime: 104 ms
# @Memory: 26.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def f(r, s):
            if r:
                s = [i + r.val for i in s] + [r.val]
                return s.count(sum) + f(r.left, s) + f(r.right, s)
            return 0
        return f(root, []) 

