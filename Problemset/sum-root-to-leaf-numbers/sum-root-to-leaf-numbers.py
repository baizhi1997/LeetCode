
# @Title: 求根到叶子节点数字之和 (Sum Root to Leaf Numbers)
# @Author: qinxinlei
# @Date: 2019-01-06 13:48:39
# @Runtime: 36 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ans=0
        q=[root]
        while q:
            p=[]
            for r in q:
                if r.left:
                    r.left.val+=r.val*10
                    p.append(r.left)
                if r.right:
                    r.right.val+=r.val*10
                    p.append(r.right)
                if not r.left and not r.right:
                    ans+=r.val
            q=p
        return ans
