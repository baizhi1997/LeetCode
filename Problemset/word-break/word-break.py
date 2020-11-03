
# @Title: 单词拆分 (Word Break)
# @Author: qinxinlei
# @Date: 2019-05-15 09:57:09
# @Runtime: 36 ms
# @Memory: N/A

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(wordDict) == 0:
            return False
        wordDict = set(wordDict)
        l = max([len(w) for w in wordDict])
        dp = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            p = i - l if i - l >= 0 else 0
            for j in range(p, i):
                if dp[j] and s[j : i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
