
# @Title: 四叉树交集 (Logical OR of Two Binary Grids Represented as Quad-Trees)
# @Author: qinxinlei
# @Date: 2018-11-17 22:19:53
# @Runtime: 136 ms
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
    def intersect(self, q1, q2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if q1.isLeaf:
            return q1.val and q1 or q2
        elif q2.isLeaf:
            return q2.val and q2 or q1
        tL=self.intersect(q1.topLeft,q2.topLeft)
        tR=self.intersect(q1.topRight,q2.topRight)
        bL=self.intersect(q1.bottomLeft,q2.bottomLeft)
        bR=self.intersect(q1.bottomRight,q2.bottomRight)
        if tL.isLeaf and tR.isLeaf and bL.isLeaf and bR.isLeaf and tL.val==tR.val==bL.val==bR.val:
            return Node(tL.val,True,None,None,None,None) 
        return Node(False,False,tL,tR,bL,bR)
