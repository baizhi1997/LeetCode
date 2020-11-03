
# @Title: 分割平衡字符串 (Split a String in Balanced Strings)
# @Author: qinxinlei
# @Date: 2020-07-28 15:31:24
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                ans += 1
        return ans
