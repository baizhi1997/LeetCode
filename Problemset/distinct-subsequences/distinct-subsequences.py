
# @Title: 不同的子序列 (Distinct Subsequences)
# @Author: qinxinlei
# @Date: 2019-05-07 15:31:26
# @Runtime: 44 ms
# @Memory: N/A

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        chars=set(t)
        index=collections.defaultdict(list)
        dp=[1]+[0]*len(t)
        for i,c in enumerate(t):
            index[c].append(i)
        for c in s:
            if c in chars:
                for i in index[c][::-1]:
                    dp[i+1]+=dp[i]
        return dp[-1]
