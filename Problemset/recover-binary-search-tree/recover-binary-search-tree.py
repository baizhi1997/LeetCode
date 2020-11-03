
# @Title: 恢复二叉搜索树 (Recover Binary Search Tree)
# @Author: qinxinlei
# @Date: 2019-05-07 11:39:02
# @Runtime: 80 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        swap=[None,None]
        pre=TreeNode(float('-inf'))
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            p=stack.pop()
            if p.val<pre.val:
                if not swap[0]:
                    swap[0]=pre
                swap[1]=p
            pre=p
            root=p.right
        swap[0].val,swap[1].val=swap[1].val,swap[0].val
