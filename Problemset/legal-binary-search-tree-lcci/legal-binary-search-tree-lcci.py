
# @Title: 合法二叉搜索树 (Legal Binary Search Tree LCCI)
# @Author: qinxinlei
# @Date: 2020-07-16 18:38:57
# @Runtime: 52 ms
# @Memory: 15.5 MB

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
