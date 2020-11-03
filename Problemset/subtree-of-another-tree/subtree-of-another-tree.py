
# @Title: 另一个树的子树 (Subtree of Another Tree)
# @Author: qinxinlei
# @Date: 2018-11-02 21:32:22
# @Runtime: 88 ms
# @Memory: N/A

class Solution:
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def convert(r):
            return '^' + str(r.val) + convert(r.left) + convert(r.right) if r else '#'
        return convert(t) in convert(s)
