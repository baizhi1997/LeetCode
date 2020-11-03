
# @Title: 二进制数转字符串 (Bianry Number to String LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 15:15:16
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def printBin(self, num: float) -> str:
        ans = "0."
        i = 0
        while num > 1e-20 and i < 32:
            num *= 2
            if num >= 1:
                num -= 1
                ans += '1'
            else:
                ans += '0'
            i += 1
        return ans if i != 32 and i != 0 else "ERROR"
