
# @Title: 二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)
# @Author: qinxinlei
# @Date: 2018-11-06 15:06:25
# @Runtime: 68 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans=math.inf
        tmp=-math.inf
        q,stack=[],[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            p=stack.pop()
            tmp,ans=p.val,min(p.val-tmp,ans)
            root=p.right
        return ans
