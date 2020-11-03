
# @Title: 填充每个节点的下一个右侧节点指针 (Populating Next Right Pointers in Each Node)
# @Author: qinxinlei
# @Date: 2019-01-04 11:48:45
# @Runtime: 80 ms
# @Memory: N/A

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root and root.left:
            root.left.next = root.right
            if root.next: 
                root.right.next = root.next.left 
            self.connect(root.left)
            self.connect(root.right)
