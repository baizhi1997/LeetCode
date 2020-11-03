
# @Title: 第一个只出现一次的字符 (第一个只出现一次的字符  LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 21:27:44
# @Runtime: 92 ms
# @Memory: 13.5 MB

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = collections.Counter(s)
        for c in s:
            if dic[c] == 1:
                return c
        return " "
