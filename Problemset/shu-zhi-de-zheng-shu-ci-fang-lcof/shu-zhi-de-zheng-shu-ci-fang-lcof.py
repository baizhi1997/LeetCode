
# @Title: 数值的整数次方 (数值的整数次方 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-04 17:34:54
# @Runtime: 36 ms
# @Memory: 13.5 MB

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n<0:
            n=-n
            x=1/x
        while n:
            if n&1:
                ans*=x
            x**=2
            n//=2
        return ans
