
# @Title: 重新规划路线 (Reorder Routes to Make All Paths Lead to the City Zero)
# @Author: qinxinlei
# @Date: 2020-10-09 20:32:49
# @Runtime: 500 ms
# @Memory: 37.1 MB

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        this_map, que, result, visited = {}, deque([0]), 0, set([0])
        for st, goto in connections:
            this_map[st] = this_map.get(st, []) + [(goto, 1)]
            this_map[goto] = this_map.get(goto, []) + [(st, 0)]
        while que:
            temp = que.pop()
            for node, flag in this_map.get(temp, []):
                if node in visited: continue
                result += flag
                que.appendleft(node)
                visited.add(node)
        return result

