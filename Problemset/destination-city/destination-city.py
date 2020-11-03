
# @Title: 旅行终点站 (Destination City)
# @Author: qinxinlei
# @Date: 2020-07-28 15:16:34
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        set1 = set()
        set2 = set()
        for path in paths:
            set1.add(path[0])
            set2.add(path[1])
        set3 = set2 - set1
        return set3.pop()
