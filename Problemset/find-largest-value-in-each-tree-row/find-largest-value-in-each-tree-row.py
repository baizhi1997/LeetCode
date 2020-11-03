
# @Title: 在每个树行中找最大值 (Find Largest Value in Each Tree Row)
# @Author: qinxinlei
# @Date: 2018-10-29 20:42:57
# @Runtime: 56 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans=[]
        q=root and [root]
        while q:
            ans.append(max(r.val for r in q))
            q=[x for r in q for x in (r.left,r.right) if x]
        return ans
