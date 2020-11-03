
# @Title: 扰乱字符串 (Scramble String)
# @Author: qinxinlei
# @Date: 2019-05-06 21:35:09
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return s1==s2 or sorted(s1)==sorted(s2) and any(self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]) or self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]) for i in range(1, len(s1)))
