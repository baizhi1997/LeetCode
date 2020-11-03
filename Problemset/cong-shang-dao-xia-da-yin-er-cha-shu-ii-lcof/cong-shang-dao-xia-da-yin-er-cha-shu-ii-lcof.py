
# @Title: 从上到下打印二叉树 II (从上到下打印二叉树 II LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 23:45:40
# @Runtime: 40 ms
# @Memory: 13.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = root and [root]
        while q:
            ans.append([n.val for n in q])
            q = [x for n in q for x in (n.left, n.right) if x]
        return ans
