
# @Title: N叉树的前序遍历 (N-ary Tree Preorder Traversal)
# @Author: qinxinlei
# @Date: 2018-10-19 10:31:50
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
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ans=[]
        stack=root and [root]
        while stack:
            p=stack.pop()
            ans.append(p.val)
            stack+=p.children[::-1]
        return ans
