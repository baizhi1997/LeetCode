
# @Title: 最大二叉树 II (Maximum Binary Tree II)
# @Author: qinxinlei
# @Date: 2019-02-28 16:27:31
# @Runtime: 56 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoMaxTree(self, root: TreeNode, val: int) -> TreeNode:
        p=TreeNode(val)
        if not root:
            return p
        if val>root.val:
            p.left=root
            return p
        root.right=self.insertIntoMaxTree(root.right,val)
        return root        
