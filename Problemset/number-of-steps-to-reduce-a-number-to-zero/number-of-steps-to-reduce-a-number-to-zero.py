
# @Title: 将数字变成 0 的操作次数 (Number of Steps to Reduce a Number to Zero)
# @Author: qinxinlei
# @Date: 2020-07-28 12:25:45
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num >>= 1
            ans += 1
        return ans
