
# @Title: 检查子树 (Check SubTree LCCI)
# @Author: qinxinlei
# @Date: 2020-06-04 22:00:45
# @Runtime: 160 ms
# @Memory: 22.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        def isSameTree(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 and t2:
                return False
            if t1 and not t2:
                return False
            return t1.val == t2.val and isSameTree(t1.left, t2.left) and isSameTree(t1.right, t2.right)

        if not t2:
            return True
        if not t1:
            return False
        return isSameTree(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)
