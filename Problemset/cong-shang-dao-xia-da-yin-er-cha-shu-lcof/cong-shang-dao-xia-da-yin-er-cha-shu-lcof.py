
# @Title: 从上到下打印二叉树 (从上到下打印二叉树 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-23 10:01:43
# @Runtime: 52 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        q = root and [root]
        ans = []
        while q:
            ans += [r.val for r in q]
            q = [x for r in q for x in (r.left, r.right) if x]
        return ans
