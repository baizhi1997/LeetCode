
# @Title: 最小高度树 (Minimum Height Tree LCCI)
# @Author: qinxinlei
# @Date: 2020-07-08 09:50:11
# @Runtime: 64 ms
# @Memory: 15.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        i =len(nums)//2
        root = TreeNode(nums[i])
        root.left = self.sortedArrayToBST(nums[:i])
        root.right = self.sortedArrayToBST(nums[i+1:])
        return root
