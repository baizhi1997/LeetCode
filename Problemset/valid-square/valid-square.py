
# @Title: 有效的正方形 (Valid Square)
# @Author: qinxinlei
# @Date: 2018-11-26 20:52:54
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dis(x, y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        
        return dis(p1, p2) == dis(p3, p4) and dis(p1, p3) == dis(p2, p4) and dis(p1, p4) == dis(p2, p3)
