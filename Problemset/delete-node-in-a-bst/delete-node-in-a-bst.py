
# @Title: 删除二叉搜索树中的节点 (Delete Node in a BST)
# @Author: qinxinlei
# @Date: 2020-10-09 16:22:25
# @Runtime: 88 ms
# @Memory: 17.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                root = None
                return root
            elif root.left is not None and root.right is None:
                tmp = root.left
                root = None
                return tmp
            elif root.right is not None and root.left is None:
                tmp = root.right
                root = None
                return tmp
            else:
                curr = root.right
                while curr.left:
                    curr = curr.left
                root.val = curr.val
                root.right = self.deleteNode(root.right, curr.val)
        return root
