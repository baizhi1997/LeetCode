
# @Title: 两数之和 IV - 输入 BST (Two Sum IV - Input is a BST)
# @Author: qinxinlei
# @Date: 2018-10-29 20:40:23
# @Runtime: 96 ms
# @Memory: N/A

class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        q=root and [root]
        set1=set()
        while q:
            for r in q:
                if r.val in set1:
                    return True
                else:
                    set1.add(k-r.val)
            q=[x for r in q for x in (r.left,r.right) if x]
        return False
