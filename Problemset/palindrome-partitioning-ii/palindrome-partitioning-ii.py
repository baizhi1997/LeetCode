
# @Title: 分割回文串 II (Palindrome Partitioning II)
# @Author: qinxinlei
# @Date: 2019-05-14 17:06:53
# @Runtime: 52 ms
# @Memory: N/A

class Solution:
    def minCut(self, s: str) -> int:
        if not s: return -1
        if s == s[::-1]: return 0
        l = len(s)
        for i in range(1, l):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        ans = [-1] + [i for i in range(l)]
        isPal = [[False] * (i + 1) for i in range(l)]
        for i in range(l):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or isPal[i - 1][j + 1]):
                    isPal[i][j] = True
                    ans[i + 1] = min(ans[i + 1], ans[j] + 1)
        return ans[l]
