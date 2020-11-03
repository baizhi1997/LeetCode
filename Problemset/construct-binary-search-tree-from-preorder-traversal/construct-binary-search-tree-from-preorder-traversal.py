
# @Title: 前序遍历构造二叉搜索树 (Construct Binary Search Tree from Preorder Traversal)
# @Author: qinxinlei
# @Date: 2019-03-11 18:16:45
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, A: List[int]) -> TreeNode:
        if not A:
            return None
        root = TreeNode(A[0])
        i = bisect.bisect(A, A[0])
        root.left = self.bstFromPreorder(A[1:i])
        root.right = self.bstFromPreorder(A[i:])
        return root
