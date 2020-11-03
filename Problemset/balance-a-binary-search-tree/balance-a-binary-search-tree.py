
# @Title: 将二叉搜索树变平衡 (Balance a Binary Search Tree)
# @Author: qinxinlei
# @Date: 2020-06-19 23:59:21
# @Runtime: 268 ms
# @Memory: 19.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def getInorder(o):
            if o.left:
                getInorder(o.left)
            inorderSeq.append(o.val)
            if o.right:
                getInorder(o.right)
        
        def build(l, r):
            mid = (l + r) // 2
            o = TreeNode(inorderSeq[mid])
            if l <= mid - 1:
                o.left = build(l, mid - 1)
            if mid + 1 <= r:
                o.right = build(mid + 1, r)
            return o

        inorderSeq = list()
        getInorder(root)
        return build(0, len(inorderSeq) - 1)


