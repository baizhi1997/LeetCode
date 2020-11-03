
# @Title: 找出克隆二叉树中的相同节点 (Find a Corresponding Node of a Binary Tree in a Clone of That Tree)
# @Author: qinxinlei
# @Date: 2020-05-31 22:32:35
# @Runtime: 816 ms
# @Memory: 22.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if original is None:
            return None

        if target is original:
            return cloned

        lret = self.getTargetCopy(original.left, cloned.left, target)
        if lret:
            return lret

        rret = self.getTargetCopy(original.right, cloned.right, target)
        if rret:
            return rret

        return None

