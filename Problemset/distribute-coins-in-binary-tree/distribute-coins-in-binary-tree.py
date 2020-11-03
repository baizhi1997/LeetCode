
# @Title: 在二叉树中分配硬币 (Distribute Coins in Binary Tree)
# @Author: qinxinlei
# @Date: 2019-03-13 10:41:03
# @Runtime: 48 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.ans=0
        def f(root):
            if not root:
                return 0
            l,r=f(root.left),f(root.right)
            self.ans+=abs(r)+abs(l)
            return root.val+r+l-1
        f(root)
        return self.ans
