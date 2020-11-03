
# @Title: 强整数 (Powerful Integers)
# @Author: qinxinlei
# @Date: 2019-03-01 19:15:22
# @Runtime: 40 ms
# @Memory: N/A

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        xs=[x**i for i in range(20) if x**i<bound]
        ys=[y**i for i in range(20) if y**i<bound]
        return list({x+y for x in xs for y in ys if x+y<=bound})
