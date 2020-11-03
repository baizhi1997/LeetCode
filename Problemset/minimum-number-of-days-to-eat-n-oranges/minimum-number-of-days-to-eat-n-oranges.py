
# @Title: 吃掉 N 个橘子的最少天数 (Minimum Number of Days to Eat N Oranges)
# @Author: qinxinlei
# @Date: 2020-08-17 16:24:43
# @Runtime: 52 ms
# @Memory: 13.9 MB

class Solution:
    def minDays(self, n: int) -> int:
        @lru_cache(None)
        def check(m:int):
            if m == 0:
                return 0
            if m == 1:
                return 1
            return min(check(m//2) + m%2 + 1,check(m//3) + m%3 + 1)
        return check(n)

