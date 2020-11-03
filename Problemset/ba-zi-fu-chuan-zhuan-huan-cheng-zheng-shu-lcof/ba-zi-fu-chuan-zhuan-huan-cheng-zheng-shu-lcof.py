
# @Title: 把字符串转换成整数 (把字符串转换成整数 LCOF)
# @Author: qinxinlei
# @Date: 2020-05-14 14:11:17
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def strToInt(self, str: str) -> int:
        import re
        return max(-(1 << 31), min((1 << 31) - 1, int(*re.findall('^\s*[+-]?\d+', str))))

