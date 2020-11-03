
# @Title: 二叉树着色游戏 (Binary Tree Coloring Game)
# @Author: qinxinlei
# @Date: 2019-08-06 19:12:29
# @Runtime: 32 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        def count(root):
            if not root:
                return 0
            return 1 + count(root.right) + count(root.left)
        q = [root]
        flag = True
        a = 0
        b = 0
        while flag:
            for r in q:
                if r.val == x:
                    a = count(r.right)
                    b = count(r.left)
                    flag = False
            q = [x for r in q for x in (r.left, r.right) if x]
        return a>n-a or b>n-b or n>(a+b+1)*2
