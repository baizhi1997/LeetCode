
# @Title: 二叉树的中序遍历 (Binary Tree Inorder Traversal)
# @Author: qinxinlei
# @Date: 2018-11-06 15:07:59
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans,stack=[],[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            p=stack.pop()
            ans.append(p.val)
            root=p.right
        return ans
t
        
