
# @Title: 二叉树的层平均值 (Average of Levels in Binary Tree)
# @Author: qinxinlei
# @Date: 2018-10-22 12:08:04
# @Runtime: 60 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ans=[]
        q=[root]
        while q:
            ans.append(sum([p.val for p in q])/len(q))
            q=[x for p in q for x in [p.left,p.right] if x]
        return ans

