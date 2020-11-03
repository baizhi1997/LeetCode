
# @Title: 左旋转字符串 (左旋转字符串 LCOF)
# @Author: qinxinlei
# @Date: 2020-06-25 22:44:21
# @Runtime: 44 ms
# @Memory: 13.5 MB

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
