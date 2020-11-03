
# @Title: 验证二叉搜索树 (Validate Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-15 17:24:58
# @Runtime: 52 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def isval(root, l, r):
            if not root:
                return True
            if root.val <= l or root.val >= r:
                return False
            return isval(root.left, l, root.val) and isval(root.right, root.val, r)
        return isval(root, float('-inf'), float('inf'))

