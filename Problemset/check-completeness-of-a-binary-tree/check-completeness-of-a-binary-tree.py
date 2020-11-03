
# @Title: 二叉树的完全性检验 (Check Completeness of a Binary Tree)
# @Author: qinxinlei
# @Date: 2019-03-13 11:47:53
# @Runtime: 44 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        q=[(root, 1)]
        j=0
        while j<len(q):
            n,i=q[j]
            if n:
                if n.left:
                    q.append((n.left,i*2))
                if n.right:
                    q.append((n.right,i*2+1))
            j+=1
        return q[-1][1]==len(q)
