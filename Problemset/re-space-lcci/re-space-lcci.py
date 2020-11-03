
# @Title: 恢复空格 (Re-Space LCCI)
# @Author: qinxinlei
# @Date: 2020-07-13 16:45:36
# @Runtime: 748 ms
# @Memory: 13.5 MB

class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        dic = {}.fromkeys(dictionary)
        l = len(sentence)
        dp = [0]*(l+1)
        for i in range(1, l+1):
            dp[i] = dp[i-1] + 1
            for j in range(i):
                if sentence[j:i] in dic:
                    dp[i] = min(dp[j], dp[i])
        return dp[-1]
