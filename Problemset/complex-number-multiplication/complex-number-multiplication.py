
# @Title: 复数乘法 (Complex Number Multiplication)
# @Author: qinxinlei
# @Date: 2018-11-22 12:52:54
# @Runtime: 32 ms
# @Memory: N/A

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        x1,y1 = a.split('+')
        x1 = int(x1)
        y1 = int(y1[:-1])
        x2,y2 = b.split('+')
        x2 = int(x2)
        y2 = int(y2[:-1])
        x3 = x1*x2-y1*y2
        y3 = x1*y2+x2*y1
        x3 = str(x3)
        y3 = str(y3)+'i'
        return x3+'+'+y3
