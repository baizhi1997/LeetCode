
# @Title: 检查平衡性 (Check Balance LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 12:37:44
# @Runtime: 68 ms
# @Memory: 17.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def f(root):
            if not root:
                return 0
            l,r=f(root.left),f(root.right)
            if l==-1 or r==-1 or abs(l-r)>1:
                return -1
            return max(l,r)+1
        return f(root)!=-1
