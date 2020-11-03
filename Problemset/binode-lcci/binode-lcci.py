
# @Title: BiNode (BiNode LCCI)
# @Author: qinxinlei
# @Date: 2020-07-09 17:43:11
# @Runtime: 136 ms
# @Memory: 19.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBiNode(self, root: TreeNode) -> TreeNode:
        def frontRetrive(root):
            if root is None:
                return
            # 遍历左子树
            frontRetrive(root.left)
            
            root.left = None
            self.pointer.right = root
            self.pointer = root

            # 遍历右子树
            frontRetrive(root.right)

            
        self.start = self.pointer = TreeNode(-1)
        frontRetrive(root)
        return self.start.right

