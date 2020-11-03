
# @Title: 根据二叉树创建字符串 (Construct String from Binary Tree)
# @Author: qinxinlei
# @Date: 2018-11-12 12:55:28
# @Runtime: 60 ms
# @Memory: N/A

class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        if t.left and not t.right:
            return "%d(%s)" %(t.val,self.tree2str(t.left))
        return "%d(%s)(%s)" %(t.val,self.tree2str(t.left),self.tree2str(t.right))
