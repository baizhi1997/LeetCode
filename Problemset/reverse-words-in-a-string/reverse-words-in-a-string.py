
# @Title: 翻转字符串里的单词 (Reverse Words in a String)
# @Author: qinxinlei
# @Date: 2019-03-18 10:22:37
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
