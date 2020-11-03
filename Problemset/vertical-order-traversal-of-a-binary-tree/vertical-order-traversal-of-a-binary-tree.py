
# @Title: 二叉树的垂序遍历 (Vertical Order Traversal of a Binary Tree)
# @Author: qinxinlei
# @Date: 2019-03-05 15:59:15
# @Runtime: 40 ms
# @Memory: N/A

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        dic={}
        def f(root,x,y):
            if not root:
                return
            if (x,y) not in dic:
                dic[(x,y)]=[root.val]
            else:
                dic[(x,y)].append(root.val)
            f(root.left,x-1,y+1)
            f(root.right,x+1,y+1)
        f(root,0,0)
        for x in dic:
            dic[x].sort()
        ans=[]
        pre=0.5
        for x,y in sorted(dic.keys()):
            if x==pre:
                ans[-1]+=dic[(x,y)]
            else:
                pre=x
                ans.append(dic[(x,y)])
        return ans
