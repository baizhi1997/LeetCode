
# @Title: 二叉树中第二小的节点 (Second Minimum Node In a Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-30 14:29:35
# @Runtime: 32 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=sys.maxsize
        q=[root]
        while q:
            for r in q:
                if r.val>root.val:
                    ans=min(ans,r.val)
            q=[x for r in q for x in (r.left,r.right) if r.val==root.val and x]
        return -1 if ans==sys.maxsize else ans
