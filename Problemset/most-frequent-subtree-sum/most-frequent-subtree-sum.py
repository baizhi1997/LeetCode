
# @Title: 出现次数最多的子树元素和 (Most Frequent Subtree Sum)
# @Author: qinxinlei
# @Date: 2018-12-01 15:37:54
# @Runtime: 60 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        dic=collections.Counter()
        def f(root):
            if not root:
                return 0
            x=f(root.right)+f(root.left)+root.val
            dic[x]+=1
            return x
        f(root)
        x=max(dic.values())
        return [k for k in dic if dic[k]==x]
