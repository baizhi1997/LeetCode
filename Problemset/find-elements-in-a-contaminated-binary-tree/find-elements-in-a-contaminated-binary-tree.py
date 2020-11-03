
# @Title: 在受污染的二叉树中查找元素 (Find Elements in a Contaminated Binary Tree)
# @Author: qinxinlei
# @Date: 2020-06-04 22:16:06
# @Runtime: 108 ms
# @Memory: 18.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.set1 = {0}
        root.val = 0
        stack = [root]
        while stack:
            p = stack.pop()
            if p.right:
                p.right.val = 2 * p.val + 2
                self.set1.add(p.right.val)
                stack.append(p.right)
            if p.left:
                p.left.val = 2 * p.val + 1
                self.set1.add(p.left.val)
                stack.append(p.left)
            

    def find(self, target: int) -> bool:
        return target in self.set1


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
