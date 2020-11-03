
# @Title: 单词拆分 II (Word Break II)
# @Author: qinxinlei
# @Date: 2019-05-15 10:42:24
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        w = set(wordDict)
        memo = {}
        def f(s):
            if s in memo:
                return memo[s]
            ans = []
            if s in w:
                ans.append(s)
            for i in range(1, len(s)):
                if s[:i] in w:
                    for st in f(s[i:]):
                        ans.append(s[:i] + ' ' + st)
            memo[s] = ans
            return memo[s]
        return f(s)
