
# @Title: N叉树的后序遍历 (N-ary Tree Postorder Traversal)
# @Author: qinxinlei
# @Date: 2018-10-19 10:33:34
# @Runtime: 156 ms
# @Memory: N/A

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans=[]
        stack=root and [root]
        while stack:
            p=stack.pop()
            ans.append(p.val)
            stack+=p.children
        return ans[::-1]
