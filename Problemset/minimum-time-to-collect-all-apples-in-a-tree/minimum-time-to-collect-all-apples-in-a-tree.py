
# @Title: 收集树上所有苹果的最少时间 (Minimum Time to Collect All Apples in a Tree)
# @Author: qinxinlei
# @Date: 2020-10-09 15:09:54
# @Runtime: 240 ms
# @Memory: 42.8 MB

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        parents = dict()
        for edge in edges:
            if edge[1] not in parents:
                parents[edge[1]] = edge[0]
            else:
                parents[edge[0]] = edge[1]
        all_paths = set()
        for i in range(len(hasApple)):
            if(hasApple[i]):
                p = i
                while(p!=0):
                    all_paths.add((parents[p], p))
                    p = parents[p]
        return len(all_paths)*2

