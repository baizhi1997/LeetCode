
# @Title: 克隆图 (Clone Graph)
# @Author: qinxinlei
# @Date: 2019-05-14 18:53:59
# @Runtime: 40 ms
# @Memory: N/A

"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        def clone(node, dict):
            if node not in dict:
                dict[node] = Node(node.val, [])
                for n in node.neighbors:
                    dict[node].neighbors.append(clone(n, dict))
            return dict[node]
        
        return clone(node, {})
