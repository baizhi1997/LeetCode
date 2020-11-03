
# @Title: 二叉搜索树序列 (BST Sequences LCCI)
# @Author: qinxinlei
# @Date: 2020-07-19 15:48:03
# @Runtime: 72 ms
# @Memory: 18.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]
        res = []
        def findPath(cur, q, path):
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            if not q:
                res.append(path)
                return
            for i, nex in enumerate(q):
                newq = q[:i] + q[i + 1:]
                findPath(nex, newq, path + [nex.val])
        findPath(root, [], [root.val])
        return res

