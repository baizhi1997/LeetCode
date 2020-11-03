
# @Title: 从上到下打印二叉树 III (从上到下打印二叉树 III LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 12:07:50
# @Runtime: 32 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = root and [root]
        ans = []
        i = 0
        while q:
            tmp = [n.val for n in q]
            if i&1:
                tmp = tmp[::-1]
            ans.append(tmp)
            q = [x for n in q for x in (n.left, n.right) if x]
            i += 1
        return ans
