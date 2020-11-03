
# @Title: 从根到叶的二进制数之和 (Sum of Root To Leaf Binary Numbers)
# @Author: qinxinlei
# @Date: 2019-04-08 22:07:33
# @Runtime: 44 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode, val = 0) -> int:
        def dfs(root,val):
            if not root:
                return 0
            cur=(val*2)+root.val
            if not root.left and not root.right:
                return cur
            return dfs(root.left,cur)+dfs(root.right,cur)
        return dfs(root,0)
