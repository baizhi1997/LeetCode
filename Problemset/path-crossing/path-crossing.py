
# @Title: 判断路径是否相交 (Path Crossing)
# @Author: qinxinlei
# @Date: 2020-08-02 22:27:31
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        set1 = set([(0, 0)])
        x, y = 0, 0
        dic = {'N': (0, 1), 'S':(0, -1), 'E':(1, 0), 'W':(-1, 0)}
        for p in path:
            x, y = x + dic[p][0], y + dic[p][1]
            if (x, y) in set1:
                return True
            set1.add((x, y))
        return False
            
