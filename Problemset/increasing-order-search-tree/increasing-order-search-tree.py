
# @Title: 递增顺序查找树 (Increasing Order Search Tree)
# @Author: qinxinlei
# @Date: 2018-10-20 16:10:34
# @Runtime: 232 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        head = TreeNode(0)
        head.right = root
        p = head
        q = root
        while q:
            if q.left:
                r = q.left
                while r.right:
                    r = r.right
                r.right = q
                p.right = q.left
                q.left = None
                q = p.right
            else:
                p = q
                q = q.right
        return head.right
