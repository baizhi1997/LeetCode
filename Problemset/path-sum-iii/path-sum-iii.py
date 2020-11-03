
# @Title: 路径总和 III (Path Sum III)
# @Author: qinxinlei
# @Date: 2018-11-09 13:34:06
# @Runtime: 64 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        D = {0: 1}
        self.ans = 0
        def rec(r, cur, D):
            if r:
                cur += r.val
                if cur-sum in D:
                    self.ans += D[cur-sum]
                if cur in D:
                    D[cur] += 1
                else:
                    D[cur] = 1
                rec(r.left, cur, D)
                rec(r.right, cur, D)
                D[cur] -= 1
        rec(root, 0, D)
        return self.ans
