
# @Title: 填充每个节点的下一个右侧节点指针 II (Populating Next Right Pointers in Each Node II)
# @Author: qinxinlei
# @Date: 2019-01-04 15:45:17
# @Runtime: 88 ms
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
        if not root: return None
        root.next = None
        q = [root]
        while q:
            q = [x for r in q for x in (r.left, r.right) if x]
            for i in range(len(q)-1):
                q[i].next = q[i+1]
