
# @Title: 字符串的最大公因子 (Greatest Common Divisor of Strings)
# @Author: qinxinlei
# @Date: 2019-06-24 16:51:12
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1 == str2 else ''
        if len(str2) > len(str1):
            str2, str1 = str1, str2
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        return ''
