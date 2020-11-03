
# @Title: 圆圈中最后剩下的数字 (圆圈中最后剩下的数字 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 21:40:34
# @Runtime: 104 ms
# @Memory: 13.4 MB

class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        ans = 0
        for i in range(2, n+1):
            ans = (m % i + ans) % i
        return ans
