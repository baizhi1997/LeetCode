
# @Title: 相同的树 (Same Tree)
# @Author: qinxinlei
# @Date: 2018-10-02 16:59:45
# @Runtime: 20 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return p and q and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) or p==q
