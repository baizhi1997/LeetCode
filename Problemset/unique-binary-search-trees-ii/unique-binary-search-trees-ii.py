
# @Title: 不同的二叉搜索树 II (Unique Binary Search Trees II)
# @Author: qinxinlei
# @Date: 2018-10-15 16:15:32
# @Runtime: 60 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def f(i,j):
            if j-i<0:
                return [None]
            elif j-i==0:
                return [TreeNode(i)]
            else:
                ans=[]
                for k in range(i,j+1):
                    left=f(i,k-1)
                    right=f(k+1,j)
                    for l in left:
                        for r in right:
                            root=TreeNode(k)
                            root.left=l
                            root.right=r
                            ans.append(root)
                return ans
        if n==0:
            return []
        return f(1,n)
