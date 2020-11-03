
# @Title: 三步问题 (Three Steps Problem LCCI)
# @Author: qinxinlei
# @Date: 2020-07-10 12:46:25
# @Runtime: 308 ms
# @Memory: 13.4 MB

class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 4
        a,b,c = 1,2,4
        for i in range(4,n+1):
            a,b,c = b,c,(a+b+c)%1000000007
        return c
