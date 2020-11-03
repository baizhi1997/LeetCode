
# @Title: 把二叉搜索树转换为累加树 (Convert BST to Greater Tree)
# @Author: qinxinlei
# @Date: 2018-10-29 21:46:32
# @Runtime: 88 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        stack=[]
        cur=root
        tmp=0
        while True:
            while cur:
                stack.append(cur)
                cur=cur.right
            if not stack:
                break
            p=stack.pop()
            p.val+=tmp
            tmp=p.val
            cur=p.left
        return root
