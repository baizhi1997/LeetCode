
# @Title: 最大层内元素和 (Maximum Level Sum of a Binary Tree)
# @Author: qinxinlei
# @Date: 2019-08-26 22:03:16
# @Runtime: 312 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        level = []
        q = [root]
        while q:
            level.append(sum([r.val for r in q]))
            q = [x for r in q for x in (r.left, r.right) if x]
        m = level[0]
        ans = 0
        for i in range(len(level)):
            if level[i] > m:
                m = level[i]
                ans = i
        return ans + 1
