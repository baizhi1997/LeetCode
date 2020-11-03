
# @Title: 路径总和 II (Path Sum II)
# @Author: qinxinlei
# @Date: 2020-07-03 14:33:52
# @Runtime: 60 ms
# @Memory: 14.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right and root.val==sum: return [[sum]]
        return [[root.val]+x for x in self.pathSum(root.left,sum-root.val) + self.pathSum(root.right,sum-root.val)]
