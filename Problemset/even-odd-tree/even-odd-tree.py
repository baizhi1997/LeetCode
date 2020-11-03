
# @Title: 奇偶树 (Even Odd Tree)
# @Author: qinxinlei
# @Date: 2020-10-09 18:46:48
# @Runtime: 548 ms
# @Memory: 41.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        q = [root]
        flag = True
        while q:
            if flag:
                tmp = float('-inf')
                for node in q:
                    if node.val <= tmp or not (node.val & 1):
                        return False
                    tmp = node.val
            else:
                tmp =float('inf')
                for node in q:
                    if node.val >= tmp or (node.val & 1):
                        return False
                    tmp = node.val
            flag = not flag
            q = [n for node in q for n in (node.left, node.right) if n]
        return True
