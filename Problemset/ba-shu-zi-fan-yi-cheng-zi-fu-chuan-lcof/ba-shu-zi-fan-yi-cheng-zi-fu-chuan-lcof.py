
# @Title: 把数字翻译成字符串 (把数字翻译成字符串 LCOF)
# @Author: qinxinlei
# @Date: 2020-07-03 16:42:37
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def translateNum(self, num: int) -> int:
        a = b = 1
        y = num % 10
        while num != 0:
            num //= 10
            x = num % 10
            a, b = (a + b if 10 <= 10 * x + y <= 25 else a), a
            y = x
        return a
        
