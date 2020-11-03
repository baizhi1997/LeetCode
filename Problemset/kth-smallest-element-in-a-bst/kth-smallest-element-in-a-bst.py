
# @Title: 二叉搜索树中第K小的元素 (Kth Smallest Element in a BST)
# @Author: qinxinlei
# @Date: 2019-01-07 10:49:57
# @Runtime: 80 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        s=[]
        while True:
            while root:
                s.append(root)
                root=root.left
            k-=1
            if k==0:
                return s[-1].val
            root=s.pop().right
