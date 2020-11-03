
# @Title: 建立四叉树 (Construct Quad Tree)
# @Author: qinxinlei
# @Date: 2018-11-17 21:44:19
# @Runtime: 112 ms
# @Memory: N/A

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: Node
        """
        N=len(grid)
        total=sum(itertools.chain(*grid))
        if total==N**2:
            return Node(True,True,None,None,None,None)
        if not total:
            return Node(False,True,None,None,None,None)
        TL = self.construct([x[:N//2] for x in grid[:N//2]])
        TR = self.construct([x[N//2:] for x in grid[:N//2]])
        BL = self.construct([x[:N//2] for x in grid[N//2:]])
        BR = self.construct([x[N//2:] for x in grid[N//2:]])
        return Node(None,False,TL,TR,BL,BR)
