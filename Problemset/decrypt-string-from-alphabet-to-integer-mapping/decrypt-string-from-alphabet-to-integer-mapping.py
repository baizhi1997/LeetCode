
# @Title: 解码字母到整数映射 (Decrypt String from Alphabet to Integer Mapping)
# @Author: qinxinlei
# @Date: 2020-07-28 16:38:00
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s)-1
        while i > -1:
            if s[i] != '#':
                ans += chr(int(s[i])+ord('a')-1)
                i -= 1
            else:
                ans += chr(int(s[i-2:i])+ord('a')-1)
                i -= 3
        return ans[::-1]
