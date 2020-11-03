
# @Title: 二叉树的后序遍历 (Binary Tree Postorder Traversal)
# @Author: qinxinlei
# @Date: 2019-05-15 11:07:17
# @Runtime: 28 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = root and [root]
        while stack:
            p = stack.pop()
            ans.append(p.val)
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        return ans[::-1]
