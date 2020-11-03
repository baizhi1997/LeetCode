
# @Title: 找树左下角的值 (Find Bottom Left Tree Value)
# @Author: qinxinlei
# @Date: 2018-10-29 20:33:18
# @Runtime: 52 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q=[root]
        ans=[]
        while q:
            ans=q[:]
            q=[x for r in q for x in (r.left,r.right) if x]
        return ans[0].val
