
# @Title: 分割字符串的最大得分 (Maximum Score After Splitting a String)
# @Author: qinxinlei
# @Date: 2020-08-02 22:20:09
# @Runtime: 48 ms
# @Memory: 13.4 MB

class Solution:
    def maxScore(self, s: str) -> int:
        x = s.count('1')
        y = 0
        ans = 0
        for c in s[:-1]:
            if c == '1':
                x -= 1
            else:
                y += 1
            ans = max(ans, x+y)
        return ans
