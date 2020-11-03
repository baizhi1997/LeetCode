
# @Title: 祖父节点值为偶数的节点和 (Sum of Nodes with Even-Valued Grandparent)
# @Author: qinxinlei
# @Date: 2020-06-02 00:48:38
# @Runtime: 112 ms
# @Memory: 16.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        if root.val % 2:
            return self.sumEvenGrandparent(root.left) + self.sumEvenGrandparent(root.right)
        if root.left:
            ans += self.sumEvenGrandparent(root.left)
            ans += root.left.left.val if root.left.left else 0
            ans += root.left.right.val if root.left.right else 0
        if root.right:
            ans += self.sumEvenGrandparent(root.right)
            ans += root.right.left.val if root.right.left else 0
            ans += root.right.right.val if root.right.right else 0
        return ans

