
# @Title: 判断子序列 (Is Subsequence)
# @Author: qinxinlei
# @Date: 2020-08-02 21:17:00
# @Runtime: 40 ms
# @Memory: 13.5 MB

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
