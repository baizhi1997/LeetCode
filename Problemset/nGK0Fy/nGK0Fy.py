
# @Title: 速算机器人 (速算机器人)
# @Author: qinxinlei
# @Date: 2020-10-28 16:38:07
# @Runtime: 44 ms
# @Memory: 13.5 MB

class Solution:
    def calculate(self, s: str) -> int:
        x, y = 1, 0
        for c in s:
            if c == 'A':
                x = x*2+y
            else:
                y = y*2+x
        return x+y
