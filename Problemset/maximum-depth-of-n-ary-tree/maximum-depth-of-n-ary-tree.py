
# @Title: N叉树的最大深度 (Maximum Depth of N-ary Tree)
# @Author: qinxinlei
# @Date: 2018-10-19 11:54:12
# @Runtime: 116 ms
# @Memory: N/A

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth=0
        queue=root and [root]
        while queue:
            depth+=1
            queue=[child for node in queue for child in node.children if child]       
        return depth
