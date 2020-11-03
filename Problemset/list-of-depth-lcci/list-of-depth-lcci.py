
# @Title: 特定深度节点链表 (List of Depth LCCI)
# @Author: qinxinlei
# @Date: 2020-06-01 20:47:11
# @Runtime: 44 ms
# @Memory: 13.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        if not tree:
            return []
        q = [tree]
        ans = []
        while q:
            node = p = ListNode(0)
            tmp = []
            for n in q:
                p.next = ListNode(n.val)
                p = p.next
                if n.left:
                    tmp.append(n.left)
                if n.right:
                    tmp.append(n.right)
            q = tmp
            ans.append(node.next)
        return ans
        
