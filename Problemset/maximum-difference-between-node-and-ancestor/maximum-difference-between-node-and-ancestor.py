
# @Title: 节点与其祖先之间的最大差值 (Maximum Difference Between Node and Ancestor)
# @Author: qinxinlei
# @Date: 2020-08-15 18:51:34
# @Runtime: 52 ms
# @Memory: 18.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.maxvalue=0
        self.dfs(root,0,100001)
        return self.maxvalue
    
    def dfs(self,node,maxv,minv):
        if not node:
            self.maxvalue = max(maxv-minv, self.maxvalue)
        else:
            maxv, minv = max(maxv,node.val), min(minv,node.val)
            self.dfs(node.left,maxv,minv)
            self.dfs(node.right,maxv,minv)            

