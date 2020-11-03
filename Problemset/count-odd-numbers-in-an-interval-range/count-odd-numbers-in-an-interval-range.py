
# @Title: 在区间范围内统计奇数数目 (Count Odd Numbers in an Interval Range)
# @Author: qinxinlei
# @Date: 2020-08-02 22:33:33
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low)//2+1 if high&1 or low&1 else (high-low)//2
