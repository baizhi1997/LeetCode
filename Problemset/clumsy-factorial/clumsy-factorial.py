
# @Title: 笨阶乘 (Clumsy Factorial)
# @Author: qinxinlei
# @Date: 2019-03-11 21:41:46
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def clumsy(self, N: int) -> int:
        if N==1:
            return 1
        if N==2:
            return 2
        if N==3:
            return 6
        if N==4:
            return 7
        x=N%4
        if x==3:
            return N-1
        if x==0:
            return N+1
        return N+2
