
# @Title: 二叉搜索树中的众数 (Find Mode in Binary Search Tree)
# @Author: qinxinlei
# @Date: 2018-11-08 20:58:20
# @Runtime: 64 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack=[]
        ans=[]
        cnt=0
        pre=math.inf
        l=0
        while True:
            while root:
                stack.append(root)
                root=root.left
            if not stack:
                break
            p=stack.pop()
            if p.val!=pre:
                cnt=1
            else:
                cnt+=1
            if cnt==l:
                ans.append(p.val)
            elif cnt>l:
                ans=[p.val]
                l=cnt
            pre=p.val
            root=p.right
        return ans
