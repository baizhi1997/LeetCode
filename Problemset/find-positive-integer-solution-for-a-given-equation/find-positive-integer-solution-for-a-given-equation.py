
# @Title: 找出给定方程的正整数解 (Find Positive Integer Solution for a Given Equation)
# @Author: qinxinlei
# @Date: 2020-07-31 13:26:56
# @Runtime: 60 ms
# @Memory: 13.4 MB

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        x, y = 1, 1000
        while x < 1001:
            while customfunction.f(x, y) > z and y > 0:
                y -= 1
            if y == 0:
                break
            if customfunction.f(x, y) == z:
                ans.append([x, y])
            x += 1
        return ans
