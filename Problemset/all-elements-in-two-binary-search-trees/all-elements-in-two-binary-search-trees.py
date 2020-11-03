
# @Title: 两棵二叉搜索树中的所有元素 (All Elements in Two Binary Search Trees)
# @Author: qinxinlei
# @Date: 2020-06-03 21:22:49
# @Runtime: 412 ms
# @Memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans = []
        stack = [root1, root2]
        while stack:
            p = stack.pop()
            if not p:
                continue
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
            ans.append(p.val)
        return sorted(ans)
