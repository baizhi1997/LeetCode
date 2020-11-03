
# @Title: N叉树的层序遍历 (N-ary Tree Level Order Traversal)
# @Author: qinxinlei
# @Date: 2018-10-22 13:08:07
# @Runtime: 120 ms
# @Memory: N/A

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        ans=[]
        q=[root]
        while q:
            ans.append([x.val for x in q])
            q=[x for p in q for x in p.children if x]
        return ans
