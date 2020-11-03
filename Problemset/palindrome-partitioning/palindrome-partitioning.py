
# @Title: 分割回文串 (Palindrome Partitioning)
# @Author: qinxinlei
# @Date: 2019-05-13 21:54:55
# @Runtime: 104 ms
# @Memory: N/A

class Solution:
    def f(self, tmp, s):
        if not s:
            self.ans.append(tmp)
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                self.f(tmp + [s[:i]], s[i:])
                
    def partition(self, s: str) -> List[List[str]]:
        self.ans = []
        self.f([], s)
        return self.ans
