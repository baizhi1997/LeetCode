
# @Title: 数字序列中某一位的数字 (数字序列中某一位的数字  LCOF)
# @Author: qinxinlei
# @Date: 2020-07-04 15:36:31
# @Runtime: 36 ms
# @Memory: 13.4 MB

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit, start, count = 1, 1, 9
        while n > count: # 1.
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        num = start + (n - 1) // digit # 2.
        return int(str(num)[(n - 1) % digit]) # 3.

