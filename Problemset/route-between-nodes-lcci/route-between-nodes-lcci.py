
# @Title: 节点间通路 (Route Between Nodes LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 23:27:55
# @Runtime: 472 ms
# @Memory: 46.6 MB

class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        link_table = [[] for _ in range(n)]
        for i, j in graph:
            link_table[i].append(j)
        visted = [0]*n
        que = [start]
        while que:
            cur_node = que.pop()
            if target in link_table[cur_node]: return True
            for node in link_table[cur_node]:
                if visted[node]==0:
                    que.insert(0,node)
            visted[cur_node] = 1
        return False

