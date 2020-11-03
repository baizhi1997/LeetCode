
# @Title: 替换所有的问号 (Replace All ?'s to Avoid Consecutive Repeating Characters)
# @Author: qinxinlei
# @Date: 2020-10-28 22:58:10
# @Runtime: 36 ms
# @Memory: 13.5 MB

class Solution:
    def modifyString(self, s: str) -> str:
        alphabet = string.ascii_lowercase
        s = list(f'0{s}0')
        for i in range(1, len(s)):
            if s[i] == '?':
                for char in alphabet:
                    if char != s[i-1] and char != s[i+1]:
                        s[i] = char
                        break
        return ''.join(s[1:-1])

