
# @Title: 把二叉搜索树转换为累加树 (Binary Search Tree to Greater Sum Tree)
# @Author: qinxinlei
# @Date: 2019-06-26 11:39:31
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        ans=root
        stack=[]
        tmp=0
        while True:
            while root:
                stack.append(root)
                root=root.right
            if not stack:
                break
            p=stack.pop()
            p.val+=tmp
            tmp=p.val
            root=p.left
        return ans
