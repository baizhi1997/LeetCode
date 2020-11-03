
# @Title: 所有可能的路径 (All Paths From Source to Target)
# @Author: qinxinlei
# @Date: 2020-06-02 21:57:47
# @Runtime: 124 ms
# @Memory: 14.5 MB

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        stack = [[0]]
        ans = []
        while stack:
            p = stack.pop()
            if p[-1] == len(graph)-1:
                ans.append(p)
            elif graph[p[-1]]:
                for x in graph[p[-1]]:
                    stack.append(p + [x])
        return ans

