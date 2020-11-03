
# @Title: 剪绳子 (剪绳子  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 15:04:06
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def cuttingRope(self, n: int) -> int:
        if n==2:
            return 1
        if n==3:
            return 2
        x,y=divmod(n,3)
        if y==0:
            return pow(3,x)
        if y==2:
            return pow(3,x)*2
        return pow(3,x-1)*4

