
# @Title: 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
# @Author: qinxinlei
# @Date: 2019-01-03 16:29:24
# @Runtime: 76 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        s=[root]
        j=0
        for i in range(1,len(preorder)):
            if inorder[j]!=s[-1].val:
                node=TreeNode(preorder[i])
                s[-1].left=node
                s.append(node)
            else:
                while s and s[-1].val==inorder[j]:
                    p=s.pop()
                    j+=1
                node=TreeNode(preorder[i])
                p.right=node
                s.append(node)
        return root
