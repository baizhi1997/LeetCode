
# @Title: 二叉树的锯齿形层次遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: qinxinlei
# @Date: 2018-10-16 15:40:49
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q=[root] if root else []
        ans=[]
        flag=True
        while q:
            if flag:
                ans.append([i.val for i in q])
            else:
                ans.append([i.val for i in q[::-1]])
            q=[x for i in q for x in (i.left,i.right) if x]
            flag=not flag
        return ans
