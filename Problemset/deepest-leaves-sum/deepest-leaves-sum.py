
# @Title: 层数最深叶子节点的和 (Deepest Leaves Sum)
# @Author: qinxinlei
# @Date: 2020-06-02 00:26:53
# @Runtime: 140 ms
# @Memory: 16.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        q = [root]
        while q:
            tmp = [x for n in q for x in (n.left, n.right) if x]
            if not tmp:
                return sum(n.val for n in q)
            q = tmp

