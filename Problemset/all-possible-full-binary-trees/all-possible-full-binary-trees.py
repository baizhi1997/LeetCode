
# @Title: 所有可能的满二叉树 (All Possible Full Binary Trees)
# @Author: qinxinlei
# @Date: 2018-11-21 22:00:23
# @Runtime: 172 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        if N&1==0:
            return []
        self.memo={0:[],1:[TreeNode(0)]}
        return self.f(N)
        
    def f(self,N):
        if N in self.memo:
            return self.memo[N]
        self.memo[N]=[]
        for i in range(1,N,2):
            j=N-i-1
            for left in self.f(i):
                for right in self.f(j):
                    root=TreeNode(0)
                    root.left=left
                    root.right=right
                    self.memo[N].append(root)
        return self.memo[N]
