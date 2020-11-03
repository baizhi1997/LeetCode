
# @Title: 二叉搜索树节点最小距离 (Minimum Distance Between BST Nodes)
# @Author: qinxinlei
# @Date: 2018-11-06 15:03:28
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=math.inf
        tmp=-math.inf
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            p=stack.pop()
            tmp,ans=p.val,min(ans,p.val-tmp)
            root=p.right
        return ans
