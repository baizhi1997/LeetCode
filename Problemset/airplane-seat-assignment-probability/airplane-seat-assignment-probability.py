
# @Title: 飞机座位分配概率 (Airplane Seat Assignment Probability)
# @Author: qinxinlei
# @Date: 2020-06-23 17:51:17
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1 if n==1 else 0.5


