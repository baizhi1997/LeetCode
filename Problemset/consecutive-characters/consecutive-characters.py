
# @Title: 连续字符 (Consecutive Characters)
# @Author: qinxinlei
# @Date: 2020-08-02 16:18:05
# @Runtime: 52 ms
# @Memory: 13.2 MB

class Solution:
    def maxPower(self, s: str) -> int:
        maxpower = 1
        tmppower = 0
        pre = ''
        for c in s:
            if c == pre:
                tmppower += 1
                maxpower = max(tmppower, maxpower)
            else:
                tmppower = 1
                pre = c
        return maxpower
