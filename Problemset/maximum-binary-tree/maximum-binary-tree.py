
# @Title: 最大二叉树 (Maximum Binary Tree)
# @Author: qinxinlei
# @Date: 2019-02-28 16:15:38
# @Runtime: 124 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack=[]
        for num in nums:
            cur=TreeNode(num)
            while stack and stack[-1].val<num:
                cur.left=stack.pop()
            if stack:
                stack[-1].right=cur
            stack.append(cur)
        return stack[0]
