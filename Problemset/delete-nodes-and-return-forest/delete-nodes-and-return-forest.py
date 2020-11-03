
# @Title: 删点成林 (Delete Nodes And Return Forest)
# @Author: qinxinlei
# @Date: 2020-10-09 19:54:39
# @Runtime: 104 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root: return None
        mapper = set(to_delete)
        ans = [] if root.val in mapper else [root]
        def dfs(node, parent, direction):
            if not node: return
            dfs(node.left, node, 'left')
            dfs(node.right, node, 'right')
            if node.val in mapper:
                if node.left: ans.append(node.left)
                if node.right: ans.append(node.right)
                if direction == 'left':
                    parent.left = None
                if direction == 'right':
                    parent.right = None
        dfs(root, None, None)
        return ans

